import cv2
import serial
import asyncio
import numpy as np
import time

# กำหนดการเชื่อมต่อ Serial กับ ESP32
ser = serial.Serial('COM7', 115200, timeout=0.1)  # เปลี่ยน COM_PORT เป็นพอร์ต 8 ที่ ESP32 เชื่อมต่อ # 115200 คือ อัตราการส่งข้อมูล # timeout=1 คือ รอข้อมูล 1 วินาที
ser.flush() # ล้างข้อมูลใน buffer ของ serial port แปลว่าล้างข้อมูลที่เคยส่งไปแล้ว

async def detect_red_color(image):
    # กำหนดช่วงค่าสีแดงใน HSV
    lower_red = np.array([0, 120, 70])
    upper_red = np.array([10, 255, 255])
    lower_red2 = np.array([170, 120, 70])
    upper_red2 = np.array([180, 255, 255])
    
    # แปลงจาก BGR เป็น HSV
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    # สร้างมาสก์สำหรับสีแดง
    mask1 = cv2.inRange(hsv, lower_red, upper_red)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    mask = mask1 + mask2
    
    # นับจำนวน pixel ที่มีสีแดง
    red_count = cv2.countNonZero(mask)
    print(red_count)
    return red_count > 400  # ถ้ามีสีแดงมากกว่า 400 pixels ให้ถือว่าตรวจจับได้

async def main():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # ตรวจจับสีแดง
        red_detected = await detect_red_color(frame)

        if red_detected:
            ser.write("RED\n".encode('utf-8'))
        else:
            ser.write("NOT_RED\n".encode('utf-8'))

        # แสดงผลภาพ
        cv2.imshow('Frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        await asyncio.sleep(1)

    cap.release()
    cv2.destroyAllWindows()
    ser.close()

if __name__ == "__main__":
    asyncio.run(main())
    
