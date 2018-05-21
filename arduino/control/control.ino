
  int outPin2 = 2; // Open
  int outPin3 = 3; // Close
  int outPin4 = 4; // Stop
  int outPin5 = 5; // Stop
    
void turnon_port(char inChar){
  switch(inChar){
       case '0'://Open Gate
          Serial.println("Open Gate");
          toggle(outPin2);
          break;
       case '1'://Close Gate
          Serial.println("Close Gate");
          toggle(outPin3);
          break;
       case '2'://Stop Gate
          Serial.println("Stop Gate");
          toggle(outPin4);
          break;
       case '3'://Stop Gate
          Serial.println("Any");
          toggle(outPin5);
          break;
      }
}

void toggle(int inPort){
  digitalWrite(inPort, LOW);       // sets the digital pin 13 on
  delay(1000);                  // waits for a second
  digitalWrite(inPort, HIGH);        // sets the digital pin 13 off
//  delay(1000);
}

void setup() {
//  Set Port to Output Mode
  pinMode(outPin2, OUTPUT);
  pinMode(outPin3, OUTPUT);
  pinMode(outPin4, OUTPUT);
  pinMode(outPin5, OUTPUT);
//  Set to HIGH
  digitalWrite(outPin2, HIGH);
  digitalWrite(outPin3, HIGH);
  digitalWrite(outPin4, HIGH);
  digitalWrite(outPin5, HIGH);
//  Initial Serial port
  Serial.begin(9600);
}
void loop() {

     if (Serial.available())
     {
      char inChar = Serial.read();
      turnon_port (inChar);
     }
}
  

