//require는 java에서 import랑 비슷한거라고 생각하면 됩니다.
//socket.io로 객체 생성, 서버 구축
let {PythonShell} = require('python-shell')
const utf8 = require('utf8');
var express = require('express');
var app = express();
var server = require('http').createServer(app);
var io = require('socket.io')(server);

var options = {
    mode: 'text',
    pythonPath: '',
    pythonOptions: ['-u'],
    scriptPath: '',
    encoding: 'utf8'
}
//url(http://localhost:8088)치면 클라이언트에게 띄어주는 웹페이지(index.html)
app.get('/', function(req, res) {
    res.sendFile(__dirname + '/index.html');
});

io.on('connection', function(socket) {
    
    console.log('connected'); // 클라리언트 접속 알려줌
    socket.on('disconnect', function() { 
        console.log('disconnected'); // 클라이언트 창 닫으면 알려줌
    });
    //socket.on 수신 / socket.emit 전송
    //1. client한테 수신받음
    socket.on('chat', function(msg) {
        options.args = [msg];
        PythonShell.run('correcting.py',options,function(err,results_pre){
            if(err) throw err;
            let data1 = results_pre[0].replace(`b\'`, '').replace(`\'`, '');
            let buff1 = Buffer.from(data1, 'base64');
            let text1 = buff1.toString('utf-8');  //파이썬 실행 결과값
            msgArray = text1.split('.'); //문장으로 나눔
            if(msgArray[msgArray.length-1]=='') msgArray.pop();
            //split결과가 ['a','b','c','']와 같은 결과가 나올 때가 있어 마지막 줄에 ..으로 출력이 되는 문제 방지
            
            //2. 받은 메세지 구분해서 다시 client에 전송
            //'short','long' 이벤트명으로 구분
            //문장 길이 100보다 작으면 'short'이벤트로 전송
            //이상이면 'long'이벤트로 전송
            options.args = [text1];
            PythonShell.run('Classifier.py',options,function(err,results_con){
                if(err) throw err;
                let data2 = results_con;
                console.log(data2);
                
                for (var i=0; i<msgArray.length; i++) {
                    if (data2[0][2*i] == '0')
                        socket.emit('long', msgArray[i]);
                    else
                        socket.emit('short', msgArray[i]);
                }
            });
        });
        
    });
});

//http://localhost:8088 포트번호 설정
server.listen(8088, function() {
    console.log('Socket IO server listening on port 8088');
});