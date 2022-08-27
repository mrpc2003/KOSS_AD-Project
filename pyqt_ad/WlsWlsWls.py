import sys
import pygame
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QMessageBox, QLineEdit, QInputDialog, QApplication
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
import paho.mqtt.client as mqtt


class Button(QWidget):  # Button class

    data = "OFF"  # 변수 선언

    def __init__(self):  # 생성자
        super().__init__()  # 상위 클래스의 생성자 호출
        self.UIinit()  # UI 초기화
        vbox = QVBoxLayout()  # 레이아웃 설정
        vbox.addLayout(self.vbox1)  # 레이아웃에 레이아웃 추가
        vbox.addLayout(self.vbox2)  # 레이아웃에 레이아웃 추가
        vbox.addLayout(self.vbox3)  # 레이아웃에 레이아웃 추가

        self.btn1.clicked.connect(self.mqtt_pub)  # 버튼1을 누르면 mqtt_pub 함수 호출
        # 버튼1을 누르면 disconnect_mqtt 함수 호출
        self.btn1.clicked.connect(self.disconnect_mqtt)
        self.btn1.clicked.connect(self.Text)  # 버튼1을 누르면 Text 함수 호출

        self.btn2.clicked.connect(self.Player)  # 버튼2를 누르면 Player 함수 호출
        # 버튼2를 누르면 disconnect_mqtt 함수 호출
        self.btn2.clicked.connect(self.disconnect_mqtt)

        # 버튼3을 누르면 passwordClass 함수 호출
        self.btn3.clicked.connect(self.passwordClass)
        # 버튼3을 누르면 disconnect_mqtt 함수 호출
        self.btn3.clicked.connect(self.disconnect_mqtt)

        self.mqtt_sub()  # mqtt_sub 함수 호출

    def passwordClass(self):  # 비밀번호 입력창
        widget.setCurrentIndex(widget.currentIndex()+1)  # 다음 위젯으로 이동

    def mqtt_pub(self):  # mqtt_pub 함수
        mqttc = mqtt.Client("python_pub")  # mqttc 생성
        mqttc.connect("192.168.137.55", 1883)  # mqttc 연결
        mqttc.publish("test", "box")  # test 이라는 토픽에 box 메시지 전송
        print("pub")  # pub 출력
        mqttc.disconnect()  # mqttc 연결 해제
        print("disconnect")  # disconnect 출력

    def security_off_mqtt_pub(self):  # security_off_mqtt_pub 함수
        mqttc = mqtt.Client("python_pub")  # mqttc 생성
        mqttc.connect("192.168.137.55", 1883)  # mqttc 연결
        mqttc.publish("security", "2")  # security 이라는 토픽에 2 메시지 전송
        print("pub")  # pub 출력
        mqttc.disconnect()  # mqttc 연결 해제
        print("disconnect")  # disconnect 출력

    def mqtt_sub(self):  # mqtt_sub 함수
        client = mqtt.Client("python_sub")  # client 생성
        client.connect("192.168.137.55", 1883, 60)  # client 연결
        client.on_connect = self.on_connect  # on_connect 이벤트 함수 연결
        client.on_message = self.on_message  # on_message 이벤트 함수 연결
        client.subscribe("security")  # security 이라는 토픽에 구독
        print("sub")  # sub 출력
        client.loop_start()  # 루프 시작

    def disconnect_mqtt(self):  # disconnect_mqtt 함수
        client = mqtt.Client("python_sub")  # client 생성
        client.disconnect()  # client 연결 해제
        print("disconnect")  # disconnect 출력
        client.loop_stop()  # 루프 종료
        print("loop_stop")  # loop_stop 출력

    def on_connect(self, client, userdata, flags, rc):  # on_connect 이벤트 함수
        # Connected with result cod 출력
        print("Connected with result cod", str(rc))

    def on_message(self, client, userdata, msg):  # on_message 이벤트 함수
        byteToStr = msg.payload  # byteToStr 에 msg.payload 저장
        result = byteToStr.decode('utf-8')  # result 에 byteToStr 디코딩
        if result == "1":  # result 가 1 이면
            Button.data = "ON"  # Button.data 에 ON 저장
            print(Button.data)  # Button.data 출력
            self.label1.setText(Button.data)  # label1 에 Button.data 저장

        if result == "2":  # result 가 2 이면
            Button.data = "OFF"  # Button.data 에 OFF 저장
            print(Button.data)  # Button.data 출력
            self.label1.setText(Button.data)  # label1 에 Button.data 저장

    def UIinit(self):  # UIinit 함수

        self.label1 = QLabel(Button.data, self)  # label1 에 Button.data 저장
        self.label1.move(350, 100)  # label1 의 위치 설정
        font1 = self.label1.font()  # font1 에 label1 의 폰트 저장
        font1.setPointSize(30)  # font1 의 폰트 크기 설정
        font1.setFamily('NotoSansKR-Black')  # font1 의 폰트 종류 설정
        font1.setBold(True)  # font1 의 폰트 굵게 설정
        self.label1.setFont(font1)  # label1 의 폰트 설정

        # label2 에 "택배 아저씨 버튼 눌러 주세요~" 저장
        self.label2 = QLabel("택배 아저씨 버튼 눌러 주세요~", self)
        self.label2.move(3, 5)  # label2 의 위치 설정
        font2 = self.label2.font()  # font2 에 label2 의 폰트 저장
        font2.setPointSize(15)  # font2 의 폰트 크기 설정
        self.label2.setFont(font2)  # label2 의 폰트 설정

        self.label1.adjustSize()  # label1 의 크기 조절
        self.label2.adjustSize()  # label2 의 크기 조절

        self.btn1 = QPushButton('택배/배달', self)  # btn1 에 "택배/배달" 저장
        self.btn2 = QPushButton('도둑', self)  # btn2 에 "도둑" 저장
        self.btn3 = QPushButton('풀기', self)  # btn3 에 "풀기" 저장

        self.btn1.move(50, 600)  # btn1 의 위치 설정
        self.btn2.move(300, 600)  # btn2 의 위치 설정
        self.btn3.move(550, 600)  # btn3 의 위치 설정
        self.btn1.setFixedSize(210, 100)  # btn1 의 크기 설정
        self.btn2.setFixedSize(210, 100)  # btn2 의 크기 설정
        self.btn3.setFixedSize(210, 100)  # btn3 의 크기 설정

        self.btn1.setFont(QtGui.QFont(
            "NotoSansKR-Regular", 30))  # btn1 의 폰트 설정
        self.btn2.setFont(QtGui.QFont(
            "NotoSansKR-Regular", 30))  # btn2 의 폰트 설정
        self.btn3.setFont(QtGui.QFont(
            "NotoSansKR-Regular", 30))  # btn3 의 폰트 설정

        self.vbox1 = QHBoxLayout()  # vbox1 에 HBoxLayout 저장
        self.vbox2 = QHBoxLayout()  # vbox2 에 HBoxLayout 저장
        self.vbox3 = QHBoxLayout()  # vbox3 에 HBoxLayout 저장

        self.vbox1.addWidget(self.label1)  # vbox1 에 label1 저장
        self.vbox2.addWidget(self.label2)  # vbox2 에 label2 저장
        self.vbox3.addWidget(self.btn1)  # vbox3 에 btn1 저장
        self.vbox3.addWidget(self.btn2)  # vbox3 에 btn2 저장
        self.vbox3.addWidget(self.btn3)  # vbox3 에 btn3 저장

        self.setGeometry(500, 300, 800, 700)  # 위치와 크기 설정
        self.setWindowTitle('Main Door')  # 창 제목 설정
        self.show()  # 창 보이기

    def Player(self):  # Player 함수
        pygame.init()  # pygame 초기화
        p = pygame.mixer.Sound('curse.mp3')  # p 에 curse.wav 저장
        p.play()  # p 재생

    def Text(self):  # Text 함수
        # QMessageBox 에 "BOX" 저장, "택배 왔습니다~~" 저장
        QMessageBox.about(self, "BOX", "택배 왔습니다~~")


class password(QWidget):  # password 클래스 선언

    def __init__(self):  # __init__ 초기화 함수
        super().__init__()  # super().__init__() 실행
        self.initUI()  # initUI 함수 실행

    def initUI(self):  # initUI 함수 선언
        self.btn = QPushButton('Password', self)  # btn 에 "Password" 저장
        self.btn.move(30, 30)  # btn 의 위치 설정
        # btn 을 클릭하면 showDialog 함수 실행
        self.btn.clicked.connect(self.showDialog)

        self.le = QLineEdit(self)  # le 에 QLineEdit 저장
        self.le.move(120, 35)  # le 의 위치 설정

        self.setWindowTitle('Input password')  # 창 제목 설정
        self.setGeometry(400, 400, 400, 400)  # 위치와 크기 설정
        self.show()  # 창 보이기

    def showDialog(self):  # showDialog 함수 선언
        # QInputDialog 에 'Input password' 저장, 'Enter password:' 저장
        text, ok = QInputDialog.getText(
            self, 'Input password', 'Enter password:')

        if ok:  # ok 이 True 일 때
            self.le.setText(str(text))  # le 에 str(text) 저장

        if text == "koss":  # text 와 "koss" 일 때
            # QMessageBox 에 "OK" 저장, "Correct!" 저장
            QMessageBox.about(self, "OK", "Correct!")
            self.passwordCorrect()  # passwordCorrect 함수 실행

        else:  # text 와 "koss" 이 아닐 때
            # QMessageBox 에 "NO" 저장, "Incorrect!!!" 저장
            QMessageBox.warning(self, "NO", "Incorrect!!!")
            pygame.init()  # pygame 초기화
            p = pygame.mixer.Sound('curse.mp3')  # p 에 curse.wav 저장
            p.play()  # p 재생

    def passwordCorrect(self):  # passwordCorrect 함수 선언
        my_instance = Updater(button.label1)  # my_instance 에 Updater 함수 전달
        run_mqtt = Updater(button)  # run_mqtt 에 Updater 함수 전달
        # security_off_mqtt_pub 에 Updater 함수 전달
        security_off_mqtt_pub = Updater(button)
        my_instance.settext()  # my_instance 의 settext 함수 실행
        run_mqtt.start()  # run_mqtt 의 start 함수 실행
        # security_off_mqtt_pub 의 security_off 함수 실행
        security_off_mqtt_pub.security_off()
        # widget 의 currentIndex() - 1 실행
        widget.setCurrentIndex(widget.currentIndex() - 1)


class Updater:  # Updater 클래스 선언
    def __init__(self, label):  # __init__ 초기화 함수
        self.label = label  # self.label 에 label 저장

    def settext(self):  # settext 함수 선언
        self.label.setText('off')  # self.label 에 'off' 저장

    def start(self):  # start 함수 선언
        button.mqtt_sub()  # button 의 mqtt_sub 함수 실행

    def security_off(self):  # security_off 함수 선언
        button.security_off_mqtt_pub()  # button 의 security_off_mqtt_pub 함수 실행


if __name__ == "__main__":  # __main__ 이라는 문자열이 있을 때
    # QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)  # app 에 QApplication 저장

    # 화면 전환용 Widget 설정
    widget = QtWidgets.QStackedWidget()  # widget 에 QtWidgets.QStackedWidget 저장

    # 레이아웃 인스턴스 생성
    button = Button()  # button 에 Button 저장
    passWord = password()  # passWord 에 password 저장

    # Widget 추가
    widget.addWidget(button)  # widget 에 button 추가
    widget.addWidget(passWord)  # widget 에 passWord 추가

    # 프로그램 화면을 보여주는 코드
    widget.setFixedHeight(1000)  # widget 의 높이 설정
    widget.setFixedWidth(1000)  # widget 의 넓이 설정
    widget.show()  # widget 보이기

    # 프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    sys.exit(app.exec_())
