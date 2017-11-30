"""
Websockets client for micropython

Based very heavily off
https://github.com/aaugustin/websockets/blob/master/websockets/client.py
"""

import logging
import usocket as socket
import ubinascii as binascii
import urandom as random

from .protocol import Websocket

LOGGER = logging.getLogger(__name__)


class WebsocketClient(Websocket):
    is_client = True


def connect(hostname, port, path):
    """
    Connect a websocket.
    """
    print('!!! client.py :: connect')

    #if __debug__: LOGGER.debug("open connection %s:%s",
    #                            uri.hostname, uri.port)

    sock = socket.socket()
    addr = socket.getaddrinfo(hostname, port)
    addr = addr[0][-1]
    sock.connect(addr)

    def send_header(header, *args):
        if __debug__: LOGGER.debug(str(header), *args)
        sock.send(header % args + '\r\n')

    # Sec-WebSocket-Key is 16 bytes of random base64 encoded
    key = binascii.b2a_base64(bytes(random.getrandbits(8)
                                    for _ in range(16)))[:-1]

    send_header(b'GET %s HTTP/1.1', path or '/')
    send_header(b'Host: %s:%s', hostname, port)
    send_header(b'Connection: Upgrade')
    send_header(b'Upgrade: websocket')
    send_header(b'Sec-WebSocket-Key: %s', key)
    send_header(b'Sec-WebSocket-Version: 13')
    send_header(b'Origin: http://localhost')
    send_header(b'')

    header = sock.readline()[:-2]
    assert header == b'HTTP/1.1 101 Switching Protocols', header

    # We don't (currently) need these headers
    # FIXME: should we check the return key?
    while header:
        if __debug__: LOGGER.debug(str(header))
        header = sock.readline()[:-2]

    return WebsocketClient(sock)
