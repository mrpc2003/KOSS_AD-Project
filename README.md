# KOSS_AD-Entrance_Detection

* 조원
    * 김우현, 남궁희, 최선우 
* 의의
    * 현대의 방범 장치를 간소화한 IoT 장치를 아두이노 회로와 서버를 이용하여 구현하고자 한다.
    * 백엔드, 프로트엔드, 아두이노를 아우르는 경험을 쌓을 수 있는 주제를 선정하였다.

* 맡은 분야
    * 최선우
        + 백엔드
            - MQTT 브로커
            - WEB SERVER(Node.js, express)
    * 남궁희
        + 프론트엔드
            - WEB
            - PYQT
    * 김우현
        + 아두이노
            - 회로구성

* 주요 기능
기능1: web에서 보안(센서) 키고 끄기

Web: 웹 소켓으로 node와 연결, 버튼으로 node한테 보내기

Node: web에서 보낸 정보 받기, web에서 받은 정보 아두이노, pyqt로 보내기

Pyqt: node한테 정보 받으면 off로 바꾸기

아두이노: node한테 정보 받으면 통신 전송 중단



기능2: 아두이노 센서가 감지했을 때

Web: 받은 데이터로 상태 변하기(경보 울리기)

Node: 아두이노한테 데이터 받기, 받은 데이터 웹소켓으로 웹에 보내기

Pyqt: 없음

아두이노: node에 데이터 보내기



기능3: pyqt에서 택배 버튼 눌렀을 때

Web: node에서 받은 데이터 보고 택배 이미지 올리기(버튼 누르면 사라지기)

Node: pyqt에서 받은 데이터 웹으로 보내기

Pyqt: node로 데이터 보내기

아두이노: 없음


기능4: pyqt에서 도둑 버튼 눌렀을 때

Web: 없음

Node: 없음

Pyqt: 음악 재생

아두이노: 없음


기능5: pyqt에서 풀기 버튼 눌렀을 때
(비밀번호 맞았을 때)

Web: 웹에서 데이터 받고 보안 안되는 상태로 바꾸기

Node: pyqt한테 데이터 받고 웹에 보내기

Pyqt: node랑 아두이노한테 보안 멈췄다고 보내기

아두이노: 통신 전송 중단


기능5: pyqt에서 풀기 버튼 눌렀을 때
(비밀번호 틀렸을 때)

Web: 없음

Node: 없음

Pyqt: 음악 재생

아두이노: 없음




* 결과물
  * 웹페이지
  
    ![image](https://user-images.githubusercontent.com/104904309/198509471-b18d3650-1c3c-417e-8585-4a7ad8e0c896.png)
    ![image](https://user-images.githubusercontent.com/104904309/198509115-cdaf4417-9154-4491-8c80-7fb817e99915.png)
    ![image](https://user-images.githubusercontent.com/104904309/198509151-8169e47a-f815-4ef9-9f41-f83618a359ca.png)
    ![image](https://user-images.githubusercontent.com/104904309/198509227-40607476-6b73-40fb-b07b-690c5451c7ab.png)
    ![image](https://user-images.githubusercontent.com/104904309/198509273-03c79095-cf3d-4bc9-82ea-05b576240918.png)
    
  * pyqt
  
