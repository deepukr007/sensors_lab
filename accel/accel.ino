#include "Arduino_BHY2.h"

SensorXYZ accelerometer(SENSOR_ID_ACC);

float accel_x;
float  accel_y;
float accel_z;


void setup() 
{
  Serial.begin(115200);
  BHY2.begin();
  accelerometer.begin();
}

void loop() {

  for(int i=1;i<=1000;)
  {

   static auto lastCheck = millis();
  
    BHY2.update();

    accel_x = (accelerometer.x() * 9.81) / 4096;
    accel_y = (accelerometer.y() * 9.81) / 4096;
    accel_z = (accelerometer.z() * 9.81) / 4096;
  
    if (millis() - lastCheck >= 100 ){
      lastCheck = millis();
      Serial.print(accel_x);
      Serial.print(",");
      Serial.print(accel_y);
      Serial.print(",");
      Serial.print(accel_z);
      Serial.println("");
      i++;
    }

  }
  
  Serial.println("end");
  exit(0);

}