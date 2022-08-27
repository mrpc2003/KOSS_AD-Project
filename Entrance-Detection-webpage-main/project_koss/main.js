const express = require("express")
const app = express()
const { WebSocketServer } = require("ws")
const mqtt = require('mqtt'); // mqtt 모듈 가져오기
const { text } = require("express");
var template = require('./template.js');

app.use(express.static("KOSS_AD"))

app.get('/', function(request, response){
  var html = template.first();
  response.send(html);
});

app.get('/switch', function(request, response){
  var html = template.switch();
  response.send(html);
});

app.get('/noinvasion', function(request, response){
  var html = template.noinvasion();
  response.send(html);
});

app.get('/invasion', function(request, response){
  var html = template.invasion();
  response.send(html);
});

app.listen(3000, () => {
  console.log(`Example app listening on port 3000`)
})

// 웹소켓 서버 생성
const wss = new WebSocketServer({ port: 3001 })

// 웹소켓 서버 연결 이벤트 바인드
wss.on("connection", ws => {
  // 데이터 수신 이벤트 바인드
  ws.on("message", data => {
    console.log(`Received from user: ${data}`)
    client.publish("security", data); // id의 내용으로 led 토픽으로 메세지 전송
  })
})

const options = { // 브로커 ip 입력과 프로토콜 입력
  host: '192.168.137.55',
  protocol: 'mqtt',
};

const client = mqtt.connect(options); // client 클래스 반환

client.on("connect", () => { // mqtt 연결
  // 연결됐을 때 실행
  console.log("connected client: "+ client.connected); //  console에 출력
  client.subscribe("PIR"); // 토픽에 구독
  client.subscribe("test"); // 토픽에 구독
});


client.on('message', (topic, message, packet) => { // 해당 topic에서 message 받기
  message = message.toString();
  if (topic === "PIR"){
    console.log('PIR에서 받았아요:  ' + message);
  }
  else if (topic === "test"){
    console.log('test에서 받았아요:  ' + message);
  }
  // wss.on("connection", ws => {
  //   // 데이터 수신 이벤트 바인드
  //     ws.send(`Received ${message}`); // 서버의 답장
  // })
  wss.clients.forEach(text =>{
    text.send(`${topic}: ${message}`, err => {
      if(err) {
        console.error(err);
      }
    });
  });
});


/*
https://hudi.blog/websocket-with-nodejs/
https://curryyou.tistory.com/348
https://meaningone.tistory.com/316
https://developer.mozilla.org/ko/docs/Web/API/WebSockets_API/Writing_WebSocket_client_applications
https://www.delftstack.com/ko/howto/javascript/change-image-src-javascript/

style 변경하는데 - 있을 때
https://hi098123.tistory.com/256

JavaScript를 사용하여 CSS 속성 변경
https://www.delftstack.com/ko/howto/javascript/change-css-property-using-javascript/
https://opentutorials.org/course/3085/18792

setTimeout() 강제종료
https://jjanddakdevlogg.tistory.com/entry/setTimeout%EC%A2%85%EB%A3%8C%EC%8B%9C%ED%82%A4%EA%B8%B0-clearTimeout-EventListener-%EC%97%90-%ED%8C%8C%EB%9D%BC%EB%AF%B8%ED%84%B0%EC%9E%88%EB%8A%94-%ED%95%A8%EC%88%98-%EB%93%B1%EB%A1%9D

js로 이미지 추가
https://ko.code-paper.com/javascript/examples-how-to-add-image-in-js



*/