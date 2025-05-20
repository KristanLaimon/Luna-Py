int pinLed = 2;

void setup(){
  pinMode(pinLed, OUTPUT);
  Serial.begin(9600);
}

int dato;

void loop(){
  if (Serial.available()){
    dato = Serial.parseInt();
    if (dato == 1){
      digitalWrite(pinLed, HIGH);
    } else {
      digitalWrite(pinLed, LOW);
    } 
  }
}