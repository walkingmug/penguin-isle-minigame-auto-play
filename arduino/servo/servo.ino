#include <Servo.h>
Servo myservo;

void setup(){
  myservo.attach(9); // if using different PIN, change the number
  myservo.write(0); // move servo to center position (90 degrees)
  Serial.begin(9600); // for reading instructions to move servo
} 

void loop(){
  if (Serial.available() > 0){
    String incomingString = Serial.readString(); // read the incoming string
    if (incomingString == "ServoDown"){
      myservo.write(90);
    }
    else if (incomingString == "ServoUp"){
      myservo.write(0);
    }
  }
}
