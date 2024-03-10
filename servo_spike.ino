#include<VarSpeedServo.h>
VarSpeedServo Servo1;
int Red = 8;
int Green = 9;

void setup(){
  pinMode(Red, OUTPUT);
  pinMode(Green, OUTPUT);

  Servo1.attach(2);
}

void loop(){
  digitalWrite(Green, HIGH);
  Servo1.write(170,100);
  delay(5000);
  digitalWrite(Green,LOW);

  digitalWrite(Red,HIGH);
  Servo1.write(190,100);
  delay(5000);
  digitalWrite(Red,LOW);
}