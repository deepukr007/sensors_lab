#include "Arduino_BHY2.h"

SensorXYZ accelerometer(SENSOR_ID_ACC);
Sensor pressure(SENSOR_ID_BARO);
Sensor temperature(SENSOR_ID_TEMP);



float accel_z;
float abs_temp;


void setup() 
{
  Serial.begin(115200);
  BHY2.begin();
  accelerometer.begin();
  pressure.begin();
  temperature.begin();


}

void loop() {

  for(int i=1;i<=1000;)
  {

   static auto lastCheck = millis();
  
    BHY2.update();
    
    accel_z = (accelerometer.z() * 9.81) / 4096;
    abs_temp = ((int(temperature.value()) - 32) * 5/9 ) + 273.15; 
  
    if (millis() - lastCheck >= 100 ){
      lastCheck = millis();
      Serial.print(millis());
      Serial.print(",");
      Serial.print(pressure.value());
      Serial.print(",");
      Serial.print(accel_z);
      Serial.print(",");
      Serial.print(abs_temp);
      Serial.println("");
      i++;
    }

  }
  
  Serial.println("end");
  exit(0);

}