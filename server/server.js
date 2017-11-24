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
        console.log('New client: %s', ip);
        ws.send('connected');

        /* 
         * onMessage Listener
        */
        ws.on(
            'message',
            function incoming(message) {
                console.log('received: %s', message);
                ws.send('echoing: ' + message);
            });        
    }
);
