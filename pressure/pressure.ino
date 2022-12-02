#include "Arduino_BHY2.h"
Sensor pressure(SENSOR_ID_BARO);

void setup() {
Serial.begin(115200);
BHY2.begin();
pressure.begin();
}

void loop() {
for(int i=1;i<=1000;)
          {
            // put your main code here, to run repeatedly:
          static auto lastCheck= millis();
          BHY2.update();

          // Check sensor values every second  
          if (millis() - lastCheck >= 100) {
          lastCheck = millis();
          Serial.println(pressure.value());
          i++;
          }
          
          }
Serial.println("end");
exit(0);
}