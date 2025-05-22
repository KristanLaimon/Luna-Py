

int pin_buzzer=4;
int frecuencia = 440;
bool allow_sound = false;
String inputString = "";
unsigned int microseconds;
int dato = 0;

void setup(){
  pinMode(pin_buzzer, OUTPUT);
  Serial.begin(9600);
}

void loop(){
  if (allow_sound){
    microseconds = 1000000.0/(2.0*frecuencia);
    digitalWrite(pin_buzzer,HIGH);
    delayMicroseconds(microseconds);
    digitalWrite(pin_buzzer, LOW);
    delayMicroseconds(microseconds);
  }

    while (Serial.available()) {
    char c = Serial.read();
    if (c == '\n') {
      parseInput(inputString);
      inputString = "";
    } else {
      inputString += c;
    }
    }
}

void parseInput(String input) {
  int separatorIndex = input.indexOf(':');
  if (separatorIndex != -1) {
    frecuencia = input.substring(0, separatorIndex).toInt();
    int state = input.substring(separatorIndex + 1).toInt();
    allow_sound = (state == 1);
  }
}