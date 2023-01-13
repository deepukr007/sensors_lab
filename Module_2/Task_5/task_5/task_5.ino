#include "Arduino_BHY2.h"


SensorXYZ magn(SENSOR_ID_MAG_PASS);
float mag_x;
float mag_y;
float mag_z;

float value_offset_x ;
float value_offset_y ;
float value_offset_z ;
float value_x ;
float value_y ;
float value_z ;


void setup() {
  Serial.begin(115200);
  BHY2.begin();
  magn.begin();


    Serial.println("Start figure-8 calibration after 3 seconds.");
    delay(3000);
    calibrate(10000);
    Serial.print("\n\rCalibrate done..");

}

void calibrate(uint32_t timeout) {
    int16_t value_x_min = 0;
    int16_t value_x_max = 0;
    int16_t value_y_min = 0;
    int16_t value_y_max = 0;
    int16_t value_z_min = 0;
    int16_t value_z_max = 0;
    uint32_t timeStart = 0;

    BHY2.update();
    value_x_min = magn.x();
    value_x_max = magn.x();
    value_y_min = magn.y();
    value_y_max = magn.y();
    value_z_min = magn.z();
    value_z_max = magn.z();
    delay(100);

    timeStart = millis();

    while ((millis() - timeStart) < timeout) {
      BHY2.update();

        if (value_x_min > magn.x()) {
            value_x_min =  magn.x();
  

        } else if (value_x_max <  magn.x()) {
            value_x_max =  magn.x();

        }

        if (value_y_min >  magn.y()) {
            value_y_min = magn.y();
 

        } else if (value_y_max < magn.y()) {
            value_y_max = magn.y();
         }

        if (value_z_min > magn.z()) {
            value_z_min = magn.y();
            // Serial.print("Update value_z_min: ");
            // Serial.println(value_z_min);

        } else if (value_z_max < magn.z()) {
            value_z_max = magn.z();
            // Serial.print("update value_z_max: ");
            // Serial.println(value_z_max);
        }

        Serial.print(".");
        delay(100);

    }

    value_offset_x = value_x_min + (value_x_max - value_x_min) / 2;
    value_offset_y = value_y_min + (value_y_max - value_y_min) / 2;
    value_offset_z = value_z_min + (value_z_max - value_z_min) / 2;
}

void loop() {
    
    BHY2.update();

    value_x =  magn.x() - value_offset_x;
    value_y =  magn.y() - value_offset_y;
    value_z =  magn.z() - value_offset_z;

    float xyHeading = atan2(value_x, value_y);
    float zxHeading = atan2(value_z, value_x);
    float heading = xyHeading;

    if (heading < 0) {
        heading += 2 * PI;
    }
    if (heading > 2 * PI) {
        heading -= 2 * PI;
    }
    float headingDegrees = heading * 180 / M_PI;
    float xyHeadingDegrees = xyHeading * 180 / M_PI;
    float zxHeadingDegrees = zxHeading * 180 / M_PI;

    Serial.print("Heading: ");
    Serial.println(headingDegrees);

    Serial.println(magn.x());
    Serial.println(value_x);
    Serial.println(value_offset_x);

    Serial.println(magn.y());
    Serial.println(value_y);
    Serial.println(value_offset_y);

       Serial.println(magn.z());
    Serial.println(value_z);
    Serial.println(value_offset_z);

     Serial.println("------------");


    delay(100);
}