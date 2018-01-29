#define ON   0
#define OFF  1

int lightPIN = 2;
int fan1PIN = 4;
int fan2PIN = 7;

void relay_setStatus(int numPin,  unsigned char statusCode)
{
  digitalWrite(numPin, statusCode);
}

void setup() {

  pinMode(lightPIN, OUTPUT);
  pinMode(fan1PIN, OUTPUT);
  pinMode(fan2PIN, OUTPUT);
  relay_setStatus(lightPIN, OFF); //turn off all the relay
  relay_setStatus(fan1PIN, OFF); 
  relay_setStatus(fan2PIN, OFF); 

  Serial.begin(9600);     
}

void loop() {
  if (Serial.available() > 0)
  {
    Serial.readStringUntil(',');
    String cmd = Serial.readStringUntil(',');
    Serial.println(cmd);

    if (cmd == "LIGHTON") {
      relay_setStatus(lightPIN, ON);
    }
    else if (cmd == "LIGHTOFF")
    {
      relay_setStatus(lightPIN, OFF);
    }
    else if (cmd == "FAN1ON")
    {
      relay_setStatus(fan1PIN, ON);
    }
    else if (cmd == "FAN1OFF")
    {
      relay_setStatus(fan1PIN, OFF);
    }
    else if (cmd == "FAN2ON")
    {
      relay_setStatus(fan2PIN, ON);
    }
    else if (cmd == "FAN2OFF")
    {
      relay_setStatus(fan2PIN, OFF);
    }
    cmd = "";
  }
}
