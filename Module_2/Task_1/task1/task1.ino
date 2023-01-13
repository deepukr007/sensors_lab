#include "Arduino_BHY2.h"


SensorXYZ magn(SENSOR_ID_MAG_PASS);
float mag_x;
float mag_y;
float mag_z;
char a;


void setup() 
{
  Serial.begin(115200);
  BHY2.begin();
  magn.begin();
}

void loop() {

   a = Serial.read();
   

   if (a=='r')
   {

     while(1)
     {

    static auto lastCheck = millis();
  
     BHY2.update();
    
  
   if (millis() - lastCheck >= 100 )
    {
      lastCheck = millis();
     
      Serial.print(magn.x());
      Serial.print(",");
      Serial.print(magn.y());
      Serial.print(",");
      Serial.print(magn.z());
      Serial.println("");
    }

     }
    

}



}