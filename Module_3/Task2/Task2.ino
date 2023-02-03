#include "Arduino_BHY2.h"


SensorBSEC bsec(SENSOR_ID_BSEC);

char a ;

void setup() 
{
  Serial.begin(115200);
  BHY2.begin();
  bsec.begin();
}

void loop() 
{
   a = Serial.read();
   if (a=='r')
   {

     while(1)
     {

     static auto lastCheck = millis();
     BHY2.update();

       if (millis() - lastCheck >= 10000)
        { 
          lastCheck = millis();
          Serial.println(bsec.b_voc_eq());
          Serial.print(',')
          Serial.print(bsec.co2_eq());
          Serial.print(',');
          Serial.print(bsec.accuracy());          
        }

     }s

    }
}

