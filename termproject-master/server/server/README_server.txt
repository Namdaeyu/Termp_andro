1. node.js 설치 https://nodejs.org/ko/download/ (나는 LTS 64bit 설치했어)

2. socket.io모듈과 express모듈 설치
3. 프로젝트 저장할 폴더 하나 만든다.
4. cmd키고 ****위에서 만든 폴더위치로 이동****
5. cmd창에 npm init --y
6. cmd창에 npm install --save --save-exact socket.io express
설치 끝

7. 프로젝트 폴더에 server.js랑 index.html 넣기
8. 에디터 쓰면 에디터에서 프로젝트 폴더열고 server.js 런한 상태로 주소창에 localhost:8088
or 에디터 안쓰고 cmd는 프로젝트 폴더위치에서 node server.js 치고 
Socket IO server listening on port 8088 뜨면 주소창에 localhost:8088 
address already in use :::8088 뜨면 포트번호 바꿔야함
//난 에디터로 visual studio code 썼음

주석이 별로니깐 socket.io 참고사이트 활용하세여
https://m.blog.naver.com/PostView.nhn?blogId=wlsdml1103&logNo=221281375575&proxyReferer=https:%2F%2Fwww.google.com%2F

https://poiemaweb.com/nodejs-socketio (1.websocket건너뛰고 밑에2.socket.io부터 보세여)
