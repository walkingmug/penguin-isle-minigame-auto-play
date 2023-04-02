#include <Servo.h>
Servo myservo;
const int greenLedPin = 5;
const int redLedPin = 3;

void setup(){
  pinMode(greenLedPin, OUTPUT);
  pinMode(redLedPin, OUTPUT);
  myservo.attach(9); // if using different PIN, change the number
  myservo.write(0); // move servo to center position (90 degrees)
  Serial.begin(9600); // for reading instructions to move servo
} 

void loop(){
  if (Serial.available() > 0){
    int incomingString = Serial.read(); // read the incoming string
    if (incomingString == '1'){
      myservo.write(90);
      digitalWrite(greenLedPin, HIGH);
      digitalWrite(redLedPin, LOW);
    }
    if (incomingString == '0'){
      myservo.write(0);
      digitalWrite(greenLedPin, LOW);
      digitalWrite(redLedPin, HIGH);
    }
  }
}
