#include "Arduino_BHY2.h"


SensorBSEC gas(SENSOR_ID_GAS);

char a ;

void setup() 
{
  Serial.begin(115200);
  BHY2.begin();
  gas.begin();
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
          Serial.println(gas.value());
        }

     }s

    }
}

