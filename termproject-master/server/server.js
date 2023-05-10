//node.js에서 socket.io모듈 등 여러 모듈을 사용하여 서버를 구현하는 코드

//require("...") 함수로 모듈 로딩
let {PythonShell} = require('python-shell');
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

//localhost:8088로 서버에 접속하면 클라이언트로 index.html을 전송
app.get('/', function(req, res) {
    res.sendFile(__dirname + '/index.html');
});

// 'connection' event handler
io.on('connection', function(socket) {
    console.log('Client connected.');
    
    socket.on('disconnect', function() { 
        console.log('Client disconnected.');
    });

    //1. client에게서 데이터 수신
    socket.on('submit', function(msg) {
        options.args = [msg];
        PythonShell.run('correcting.py',options,function(err,results_pre){
            if(err) throw err;
            let data1 = results_pre[0].replace(`b\'`, '').replace(`\'`, '');
            let buff1 = Buffer.from(data1, 'base64');
            let text1 = buff1.toString('utf-8');  //파이썬 실행 결과값
            msgArray = text1.split('.'); //문장으로 나눔
            if(msgArray[msgArray.length-1]=='') msgArray.pop();
            //split결과가 ['a','b','c','']와 같은 결과가 나올 때가 있어 마지막 줄에 ..으로 출력이 되는 문제 방지
            
            //2. 수신한 데이터 구분해서 다시 client에 송신
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
                    
                    //수신 끝남 client에 알려주기
                    if(i == (msgArray.length-1)) {
                            socket.emit('end');
                    }
                }
            });
        });
    });
});

//8080포트 할당, clinet 연결 대기 상태
server.listen(8080, function() {
    console.log('Socket IO server listening on port 8080');
});
