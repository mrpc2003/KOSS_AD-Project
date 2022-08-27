import sys #pyqt 실행에 필요한 모듈
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel #기본적인 UI 구성요소를 제공하는 모듈
from matplotlib.backends.backend_qt5agg import FigureCanvas as FigureCanvas # 그래프를 그리기 위한 모듈
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar # 그래프 툴바를 그리기 위한 모듈
from matplotlib.figure import Figure # 그래프를 그리기 위한 모듈
from pymongo import MongoClient # python에서 mongodb를 불러오기 위한 모듈
from PyQt5.QtCore import Qt #pyqt를 사용하기 위한 모듈
from PyQt5.QtGui import QIcon, QPixmap # 사진을 추가하기 위한 모듈
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("connected OK")
    else:
        print("Bad connection Returned code=", rc)


def on_disconnect(client, userdata, flags, rc=0):
    print(str(rc))


def on_subscribe(client, userdata, mid, granted_qos):
    print("subscribed: " + str(mid) + " " + str(granted_qos))


def on_message(client, userdata, msg):
    print(str(msg.payload.decode("utf-8")))

# 새로운 클라이언트 생성
client = mqtt.Client()
# 콜백 함수 설정 on_connect(브로커에 접속), on_disconnect(브로커에 접속중료), on_subscribe(topic 구독),
# on_message(발행된 메세지가 들어왔을 때)
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_subscribe = on_subscribe
client.on_message = on_message
# address : localhost, port: 1883 에 연결
client.connect('192.168.183.102', 1883)
# common topic 으로 메세지 발행
client.subscribe('test', 1)
client.loop_forever()

class MyApp(QMainWindow): #MyApp클래스 생성
  def __init__(self):
      super().__init__()

      self.main_widget = QWidget() #main 위젯 생성
      self.setCentralWidget(self.main_widget) # 가운데 정렬


      self.setWindowTitle('실내 미세먼지 농도 측정하기') #타이틀바에 나타나는 창의 제목 설정
      self.setGeometry(300, 100, 600, 600) #위젯의 위치와 크기 조절
      self.show() #위젯을 스크린에 보여줌




if __name__ == '__main__': # pyqt 실행을 위한 코드
  app = QApplication(sys.argv)
  ex = MyApp()
  sys.exit(app.exec_())

# https://developer-finn.tistory.com/1