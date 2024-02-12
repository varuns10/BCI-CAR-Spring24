#include <SoftwareSerial.h>

// Define motor pins
int ena = 5;
int in1 = 6;
int in2 = 7;
int in3 = 8;
int in4 = 9;
int enb = 10;

// Define SoftwareSerial pins
SoftwareSerial BTSerial(0, 1); // RX, TX - Choose pins that are not used by other hardware

void setup() {
  // Initialize motor pins
  pinMode(ena, OUTPUT);
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);
  pinMode(enb, OUTPUT);
  pinMode(in3, OUTPUT);
  pinMode(in4, OUTPUT);
  
  //pinMode(11, OUTPUT);
  //digitalWrite(11, LOW);

  // Begin serial communication with PC and Bluetooth module
  Serial.begin(9600); // Start serial communication at 9600 baud rate
  BTSerial.begin(38400); // HC-05 default speed in communication mode
  Serial.println("Bluetooth Car Control Ready!");
}

void loop() {
  // Check if data is received from the Bluetooth module
  if (BTSerial.available()) {
    Serial.println("Command Received!");
    char command = BTSerial.read(); // Read the incoming byte

    switch(command) {
      case 'w': // Move forward
        moveForwardMaxSpeed();
        break;
      case 's': // Move backward
        moveBackwardMaxSpeed();
        break;
      case 'a': // Turn left
        turnLeft();
        break;
      case 'd': // Turn right
        turnRight();
        break;
      default:
        // If any other character, stop the motors
        stopMotors();
        break;
    }
  }
}

void moveForwardMaxSpeed() {
  digitalWrite(in1, HIGH);
  digitalWrite(in2, LOW);
  digitalWrite(in3, HIGH);
  digitalWrite(in4, LOW);
  analogWrite(ena, 255);
  analogWrite(enb, 255);
}

void moveBackwardMaxSpeed() {
  digitalWrite(in1, LOW);
  digitalWrite(in2, HIGH);
  digitalWrite(in3, LOW);
  digitalWrite(in4, HIGH);
  analogWrite(ena, 255);
  analogWrite(enb, 255);
}

void stopMotors() {
  digitalWrite(in1, LOW);
  digitalWrite(in2, LOW);
  digitalWrite(in3, LOW);
  digitalWrite(in4, LOW);
}

void turnLeft() {
  digitalWrite(in1, LOW);
  digitalWrite(in2, HIGH);
  digitalWrite(in3, HIGH);
  digitalWrite(in4, LOW);
  analogWrite(ena, 255);
  analogWrite(enb, 255);
}

void turnRight() {
  digitalWrite(in1, HIGH);
  digitalWrite(in2, LOW);
  digitalWrite(in3, LOW);
  digitalWrite(in4, HIGH);
  analogWrite(ena, 255);
  analogWrite(enb, 255);
}
