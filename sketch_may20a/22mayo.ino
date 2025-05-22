int pinBoton=2; //esp32 specific
int estado;
int estadoAnt=LOW;
int sw=0;

void setup(){
  pinMode(pinBoton,INPUT);
  Serial.begin(9600);
}

void loop() {
  estado = digitalRead(pinBoton);
  if (estado == HIGH && estadoAnt==LOW){
    estadoAnt=HIGH;
    if (sw==0) sw = 1;
    else sw = 0;
    Serial.print(sw);
  }else if (estado == LOW && estadoAnt==HIGH){
    estadoAnt=LOW;
  }
}