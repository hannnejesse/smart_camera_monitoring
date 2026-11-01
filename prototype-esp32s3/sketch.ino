
const int PIR_PIN = 4;

int previousPirState = LOW;

void setup() {
  Serial.begin(115200);

  pinMode(PIR_PIN, INPUT);

  Serial.println("Smart Camera Monitoring Started");
  Serial.println("PIR activity monitoring enabled");
}

void loop() {
  int pirState = digitalRead(PIR_PIN);

  if (pirState == HIGH && previousPirState == LOW) {
    Serial.println("ACTIVITY DETECTED");
  }

  previousPirState = pirState;

  delay(50);
}
