# face_recog.py

import face_recognition
import cv2
import camera
import os
import numpy as np
import paho.mqtt.client as mqtt

# subscriber callback


class FaceRecog():
    def __init__(self):
        # Using OpenCV to capture from device 0. If you have trouble capturing
        # from a webcam, comment the line below out and use a video file
        # instead.
        self.camera = camera.VideoCamera()

        self.known_face_encodings = []
        self.known_face_names = []

        # knowns 디렉토리에서 사진 파일을 읽습니다. 파일 이름으로부터 사람 이름을 추출합니다.

        dirname = 'knowns'
        files = os.listdir(dirname)
        for filename in files:
            name, ext = os.path.splitext(filename)
            if ext == '.jpg':
                self.known_face_names.append(name)
                pathname = os.path.join(dirname, filename)

                # 사진에서 얼굴 영역을 알아내고, face landmarks라 불리는 68개 얼굴 특징의 위치를 분석한 데이터를 known_face_encodings에 저장합니다
                img = face_recognition.load_image_file(pathname)
                face_encoding = face_recognition.face_encodings(img)[0]
                self.known_face_encodings.append(face_encoding)

        # Initialize some variables
        self.face_locations = []
        self.face_encodings = []
        self.face_names = []
        self.process_this_frame = True

    def __del__(self):
        del self.camera

    def get_frame(self):
        # Grab a single frame of video
        frame = self.camera.get_frame()

        # Resize frame of video to 1/4 size for faster face recognition processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_small_frame = small_frame[:, :, ::-1]

        # 계산 양을 더 줄이기 위해서 두 frame당 1번씩만 계산합니다.
        if self.process_this_frame:
            # 읽은 frame에서 얼굴 영역과 특징을 추출합니다.
            self.face_locations = face_recognition.face_locations(
                rgb_small_frame)
            self.face_encodings = face_recognition.face_encodings(
                rgb_small_frame, self.face_locations)

            self.face_names = []
            for face_encoding in self.face_encodings:
                # Frame에서 추출한 얼굴 특징과 knowns에 있던 사진 얼굴의 특징을 비교하여, (얼마나 비슷한지) 거리 척도로 환산합니다.
                # 거리(distance)가 가깝다는 (작다는) 것은 서로 비슷한 얼굴이라는 의미 입니다.
                distances = face_recognition.face_distance(
                    self.known_face_encodings, face_encoding)
                min_value = min(distances)

                # tolerance: How much distance between faces to consider it a match. Lower is more strict.
                # 실험상, 거리가 0.6 이면 다른 사람의 얼굴입니다. 이런 경우의 이름은 Unknown 입니다.
                name = "Unknown"
                if min_value < 0.6:
                    index = np.argmin(distances)
                    name = self.known_face_names[index]

                self.face_names.append(name)

        self.process_this_frame = not self.process_this_frame

        # Display the results
        for (top, right, bottom, left), name in zip(self.face_locations, self.face_names):
            # Scale back up face locations since the frame we detected in was scaled to 1/4 size
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            # Draw a box around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            # Draw a label with a name below the face
            cv2.rectangle(frame, (left, bottom - 35),
                          (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6),
                        font, 1.0, (255, 255, 255), 1)

        return frame

    def get_jpg_bytes(self):
        frame = self.get_frame()
        # We are using Motion JPEG, but OpenCV defaults to capture raw images,
        # so we must encode it into JPEG in order to correctly display the
        # video stream.
        ret, jpg = cv2.imencode('.jpg', frame)
        return jpg.tobytes()

    def on_message(client, userdata, message):  # message received
        print("message received ", str(
            message.payload.decode("utf-8")))  # print message
        print("message topic=", message.topic)  # print topic
        print("message qos=", message.qos)  # print qos
        print("message retain flag=", message.retain)  # print retain flag


if __name__ == '__main__':
    broker_address = "192.168.1.48"  # broker address

    face_recog = FaceRecog()
    print(face_recog.known_face_names)
    mqttc = mqtt.Client("client2")
    mqttc.connect(broker_address, 1883)

    client1 = mqtt.Client("client1")  # 구독자 이름
    client1.connect(broker_address)  # broker 주소 등록
    client1.subscribe("PIR")  # 등록하고픈 토픽 지정
    client1.on_message = face_recog.on_message()  # subscriber callback 지정
    # client1.loop_forever() #무한 반복

    while True:
        frame = face_recog.get_frame()

        if face_recog.known_face_names == "Unknown":
            mqttc.publish("security", "1")
        else:
            mqttc.publish("security", "2")

        # show the frame
        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1) & 0xFF

        # if the `q` key was pressed, break from the loop
        if key == ord("q"):
            break

    # do a bit of cleanup
    cv2.destroyAllWindows()
    print('finish')
