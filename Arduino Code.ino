#include <Servo.h>
const int trigPin1 = 2;
const int echoPin1 = 3;
const int trigPin2 = 4;
const int echoPin2 = 5;
int pin = 6;
Servo servoMotor;
void setup() {
  servoMotor.attach(pin);
  servoMotor.write(90);
  Serial.begin(9600);
  pinMode(7,OUTPUT);
  pinMode(8,OUTPUT);
  pinMode(trigPin1, OUTPUT);
  pinMode(echoPin1, INPUT);
  pinMode(trigPin2, OUTPUT);
  pinMode(echoPin2, INPUT);
}

void loop() {
    long duration1, cm1;
  digitalWrite(trigPin1, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin1, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin1, LOW);
  duration1 = pulseIn(echoPin1, HIGH);
  cm1 = duration1 * 0.034 / 2;
   long duration2, cm2;
  digitalWrite(trigPin2, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin2, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin2, LOW);
  duration2 = pulseIn(echoPin2, HIGH);
  cm2 = duration2 * 0.034 / 2;
digitalWrite(7,HIGH);
digitalWrite(8,LOW);
servoMotor.write(0);
Serial.print("Height of waste: ");
Serial.println(cm2);
delay(1000);
if(cm1<5&&cm2>5){
digitalWrite(8,HIGH);
digitalWrite(7,LOW);
servoMotor.write(90);
delay(5000);
}

}
