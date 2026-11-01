const int PIR_PIN = 4;
const int CAMERA_LED_PIN = 5;

int previousPirState = LOW;

void setup() {
  Serial.begin(115200);

  pinMode(PIR_PIN, INPUT);
  pinMode(CAMERA_LED_PIN, OUTPUT);

  digitalWrite(CAMERA_LED_PIN, LOW);

  Serial.println("Smart Camera Monitoring Started");
  Serial.println("PIR activity monitoring enabled");
}

void loop() {
  int pirState = digitalRead(PIR_PIN);

  if (pirState == HIGH && previousPirState == LOW) {
    Serial.println("ACTIVITY DETECTED");

    digitalWrite(CAMERA_LED_PIN, HIGH);
    Serial.println("CAMERA ACTIVATION SIGNAL ON");
  }

  if (pirState == LOW && previousPirState == HIGH) {
    digitalWrite(CAMERA_LED_PIN, LOW);
    Serial.println("CAMERA ACTIVATION SIGNAL OFF");
  }

  previousPirState = pirState;

  delay(50);
}