/* Simple code to turn a remote LED on/off */

#define VERSION "1.00"

int LED = 5;
char inChar;

void setup(){
  pinMode(LED, OUTPUT);
  Serial.begin(9600);
}

void loop(){
  if (Serial.available()>0){
    inChar = Serial.read();
    if (inChar == 'H'){
      // turn on the LED
      digitalWrite(LED, HIGH);
      delay(10);
    }
    else if (inChar == 'L'){
      // turn off the LED
      digitalWrite(LED, LOW);
      delay(10);
    }
  }
}
