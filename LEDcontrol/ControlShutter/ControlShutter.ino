int incomingByte = 0;
int ShutterPin=2;//ShutterPin to which the shutter is connected in the Arduino board (core). Other ShutterPin goes to ground.
int LEDPin1=3;
int LEDPin2=4;
int LEDPin3=5;
int LEDPin4=6;
int LEDPin5=7;
int LEDPin6=8;
int LEDPin7=9;

void setup() {
  Serial.begin(9600);
  pinMode(ShutterPin, OUTPUT);
  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(LEDPin1, OUTPUT);
  pinMode(LEDPin2, OUTPUT);
  pinMode(LEDPin3, OUTPUT);
  pinMode(LEDPin4, OUTPUT);
  pinMode(LEDPin5, OUTPUT);
  pinMode(LEDPin6, OUTPUT);
  pinMode(LEDPin7, OUTPUT);
  digitalWrite(ShutterPin,HIGH);

}

void loop() {   
  if (Serial.available() > 0) {
    // read the incoming byte:
    incomingByte = Serial.read();

    Serial.println(incomingByte,DEC);
    if (incomingByte==48){
      digitalWrite(ShutterPin,HIGH);
      digitalWrite(LED_BUILTIN, LOW); 
    }else if (incomingByte==49){
      digitalWrite(ShutterPin,LOW);
      digitalWrite(LED_BUILTIN, HIGH); 
    }
    else if (incomingByte==50){
      digitalWrite(LEDPin1, LOW);
      digitalWrite(LEDPin2, LOW);
      digitalWrite(LEDPin3, LOW);
      digitalWrite(LEDPin4, LOW);
      digitalWrite(LEDPin5, LOW);
      digitalWrite(LEDPin6, LOW);
      digitalWrite(LEDPin7, LOW);
      digitalWrite(LED_BUILTIN, LOW); 
    }
    else if (incomingByte==51){
      digitalWrite(LEDPin1, HIGH);
      digitalWrite(LEDPin2, HIGH);
      digitalWrite(LEDPin3, HIGH);
      digitalWrite(LEDPin4, HIGH);
      digitalWrite(LEDPin5, HIGH);
      digitalWrite(LEDPin6, HIGH);
      digitalWrite(LEDPin7, HIGH);
      digitalWrite(LED_BUILTIN, HIGH); 
    }
    else if (incomingByte==57){
      Serial.print("Arduino");
    }
    else{
      Serial.println("Error");
    }
  }
}
