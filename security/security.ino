#include <ESP8266WiFi.h>
#include <PubSubClient.h>
#include <SoftwareSerial.h>

char ssid[] = "windows11";           // your network SSID (name)
char pass[] = "00000000";           // your network password
const char* mqtt_server = "192.168.137.55"; // your MQTT broker 여기에 MQTT 브로커IP주소를 넣으세요
const char* clientName = "pi"; // client 이름

int pirSensor = D6;
int led_pin = D7;
int stat = 1;

WiFiClient esp8266Client;
PubSubClient client(esp8266Client);

void setup() {
  Serial.begin(9600);
  setup_wifi();
  client.setServer(mqtt_server,1883); 
  client.setCallback(callback); //callback 함수 세팅
  pinMode (pirSensor,INPUT);
  pinMode (led_pin,OUTPUT);
  digitalWrite(led_pin, LOW);

}

void setup_wifi() {
   delay(10);
   Serial.println();
   Serial.print("Connecting to ");
   Serial.println(ssid);
   WiFi.mode(WIFI_STA);
   WiFi.begin(ssid, pass);
   while (WiFi.status() != WL_CONNECTED) {
      delay(500);
      Serial.print(".");
   }
   Serial.println("");
   Serial.println("WiFi connected");
   Serial.println("IP address: ");
   Serial.println(WiFi.localIP());  
}
//메시지가 들어왔을 때 처리하는 callback 함수
void callback(char* topic, byte* payload, unsigned int uLen) {
  char pBuffer[uLen+1];
  int i;
  for(i = 0; i < uLen; i++)
  {
    pBuffer[i]=(char)payload[i];
  }
  Serial.println(pBuffer); // 1 or 2
  if(pBuffer[0]=='1')
  {
//    digitalWrite(led_pin, HIGH); // 1이면 led 켜기
    stat = 1;
  }
  else if(pBuffer[0]=='2')
  {
//    digitalWrite(led_pin, LOW); // 2면 led 끄기
    stat = 2;
  } 
}

void reconnect() {
   while (WiFi.status() != WL_CONNECTED) {
     delay(500);
     Serial.print(".");
     setup_wifi();
   }
   while (!client.connected()) {
     Serial.println("Attempting MQTT connection...");
     if (client.connect(clientName)) {     //MQTT client name MQTT 클라이언트 이름으로 중복되지 않도록 합니다.
       Serial.println("connected");
       client.subscribe("security");
     }
     else {
       Serial.print("MQTT connection failed, retry count: ");
       Serial.println(client.state());
       Serial.println("try again in 3 seconds");
       delay(3000);
     }
   }
}

void loop() {
  int pirValue = digitalRead(pirSensor); 
  
  // mqtt out
  if (!client.connected()) {
     reconnect();
  }
  if (stat == 1){
    if (pirValue == HIGH) {  
      client.publish ("PIR","on");
      Serial.println (": Detected");
      digitalWrite(led_pin, HIGH);
    }
    else {
        client.publish ("PIR","off");
        Serial.println (": Not detected");
        digitalWrite(led_pin, LOW);
    }
  }

  if (stat == 2){
    digitalWrite(led_pin, LOW);
    Serial.print (pirValue);
  }
  client.loop();
  delay(1000);   
}
