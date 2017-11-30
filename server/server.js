const WebSocket = require('ws');

/*
 * Bind Server on 8081 port
 */
const wss = new WebSocket.Server({ port: 8081 });

/* 
 * onConnection Listener
 */
wss.on(
    'connection',
    function connection(ws, req) {
        const ip = req.connection.remoteAddress;
        ioLogger("New client.", ip, "Connection");
        ws.send('connected');

        /* 
         * onMessage Listener
         */
        ws.on(
            'message',
            function incoming(message) {
                ioLogger(message, ip, "Message");
                ws.send('echoing: ' + message);
            });
    }
);



/* 
 * Utils
 */

function addZero(i) {
    if (i < 10) {
        i = "0" + i;
    }
    return i;
}

function getDateString() {
    var now = new Date();
    var day = addZero(now.getDate());
    var month = addZero(now.getMonth() + 1);
    var year = now.getFullYear();
    var hour = addZero(now.getHours());
    var min = addZero(now.getMinutes());
    var sec = addZero(now.getSeconds());

    return day + "/" + month + "/" + year + " - " + hour + ":" + min + ":" + sec;
}

function ioLogger(msg, ip, desc) {
    console.log('[' + getDateString() + ' :: ' + ip + ' :: ' + desc + ']: %s', msg);
}
