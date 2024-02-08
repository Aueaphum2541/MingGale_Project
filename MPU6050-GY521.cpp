#include <Arduino.h>
#include "I2Cdev.h"
#include "MPU6050.h"
#include "Wire.h"

MPU6050 mpu;
int16_t ax, ay, az;
int16_t gx, gy, gz;
int valx , valy , valz;

void setup() 
{

Wire.begin(); // กำหนดให้ใช้ I2C

Serial.begin(115200);

Serial.println("Initialize MPU");

mpu.initialize(); // กำหนดค่าเริ่มต้นให้ MPU6050

Serial.println(mpu.testConnection() ? "Connected" : "Connection failed"); // ทดสอบการเชื่อมต่อกับ MPU6050 ว่าสามารถเชื่อมต่อได้หรือไม่ ? คือ if แบบสั้น

}

void loop() 

{

mpu.getMotion6(&ax, &ay, &az, &gx, &gy, &gz); // อ่านค่า Accelerometer และ Gyroscope จาก MPU6050

valx = map(ax, -17000, 17000, 0, 179); // ค่าที่ได้จาก Accelerometer จะอยู่ในช่วง -17000 ถึง 17000 แปลงค่า Accelerometer ให้อยู่ในช่วง 0-179 โดยใช้คำสั่ง map

valy = map(ay, -17000, 17000, 0, 179);

valz = map(az, -17000, 17000, 0, 179);

Serial.print("axis x = ") ; 

Serial.print(valx) ; 

Serial.print(" axis y = ") ; 

Serial.print(valy) ; 

Serial.print(" axis z = ") ; 

Serial.println(valz) ; 

delay(2000);

}