#include <Arduino.h>
#include <Servo.h>

// Pin number for the LED
Servo myservo; //ประกาศตัวแปรแทน Servo

void setup() {
  // Set the LED pin as an output
  myservo.attach(9);
  Serial.begin(115200);
}

void loop() {
  if (Serial.available() > 0) {
    String command = Serial.readStringUntil('\n');
    if (command == "RED") {
      myservo.write(180);
    } else {
      myservo.write(0);
    }
  }
}