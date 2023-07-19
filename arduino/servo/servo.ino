#include <Servo.h>
Servo myservo;
const int greenLedPin = 5;
const int redLedPin = 3;
const int servoPin = 9;
const int servoUp = 0;
const int servoDown = 20;


void setup(){
  pinMode(greenLedPin, OUTPUT);
  pinMode(redLedPin, OUTPUT);
  myservo.attach(servoPin); // if using different PIN, change the number
  myservo.write(servoUp); // move servo to center position (90 degrees)
  digitalWrite(greenLedPin, LOW);
  digitalWrite(redLedPin, HIGH); // turn on red LED
  Serial.begin(9600); // for reading instructions to move servo
} 

void loop(){
  if (Serial.available() > 0){
    int incomingString = Serial.read(); // read the incoming string
    // move servo down
    if (incomingString == '1'){
      myservo.write(servoDown);
      digitalWrite(greenLedPin, HIGH);
      digitalWrite(redLedPin, LOW);
    }
    // move servo up
    if (incomingString == '0'){
      myservo.write(servoUp);
      digitalWrite(greenLedPin, LOW);
      digitalWrite(redLedPin, HIGH);
    }
    // do nothing
    else{
      digitalWrite(greenLedPin, LOW);
      digitalWrite(redLedPin, LOW);
    }
  }
}
