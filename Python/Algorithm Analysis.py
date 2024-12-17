import time #นำเข้า time 
import matplotlib.pyplot as plt #นำเข้าฟังก์ชั่นการสร้างกราฟ
import numpy as np #นำเข้าnumpyเพื่อใช้งานตัวเลขได้เร็วขึ้น
list_time = [] #สร้างlistไว้เก็บข้อมูลก่อนเพื่อความง่ายในการเก็บก่อนเปลี่ยนเป็นข้อมูล numpy

def timeeeeeeee(x): #ฟังค์ชั่นคำนวณเวลาที่ใช้ในการรันโปรแกรม
    start = time.perf_counter() #บันทึกเวลาก่อนเริ่มโปรแกรม
    x #คำสั่งให้โปรแกรมทำงาน
    end = time.perf_counter() #บันทึกเวลาหลังโปรแกรมทำงานเสร็จ
    remain = end-start #นำเวลาก่อนและหลังมาลบกันเพื่อให้ได้เวล่าที่โปรแกรมใช้ในการทำงาน
    print(remain, "seconds") #พิมพ์เวลาที่คำนวณได้ออกมา
    list_time.append(remain) #นำเวลาที่คำนวณได้เข้าใน list

def constant(data): #O(1)
    return len(data) #+1ทุกครั้งที่มีการเพิ่มของข้อมูล ทำให้สามารถเรียกข้อมูลได้ทันที

def linear(data): #O(n)
    return data.reverse() #เรียกข้อมูลที่ละตัวเพื่อทำงาน

def quadratic(data): #O(n**2)
    max = 0 #กำหนดตัวแปรขึ้นมาตัวหนึ่ง
    for i in range(len(data)): #วนการทำงานเป็นจำนวนรอบเท่ากับขนาดของข้อมูล
        for j in range(len(data)): #วนการทำงานเป็นจำนวนรอบเท่ากับขนาดของข้อมูล
            if data[j] > max: 
                max = data[j] #ถ้าข้อมูลที่ดึงออกมามีค่ามากกว่าค่า max ในปัจจุบัน ให้แทนที่ข้อมูลนั้นลงไปในค่า max

def logarithmic_linear(data): #O(nlogn)
    return data.sort() #เป็นการวนหาข้อมูล 2 รอบ โดยรอบแรกวนข้อมูลทั้งหมดทีละตัว ส่วนรอบที่สองเป็นการวนข้อมูลที่ไม่เกี่ยวข้องออกไปทีละครึ่ง

n1 = list(range(0,500,3)) #ตัวอย่างข้อมูล 1
n2 = list(range(6000)) #ตัวอย่างข้อมูล 2
n3 = list(range(10000,-1,-10)) #ตัวอย่างข้อมูล 3
n4 = list(range(8000,0,-5)) #ตัวอย่างข้อมูล 4

#นำเข้าตัวอย่างข้อมูลทั้งหมดไว้ในฟังก์ชั่นที่ต้องการคำนวณหาเวลาการทำงาน และสั่งให้ทำงานในฟังก์ชั่นคำนวณเวลาอีกทีเพื่อให้สามารถทำงานได้ในบรรทัดเดียว
print("Constant: ")
timeeeeeeee(constant(n1))
timeeeeeeee(constant(n2))
timeeeeeeee(constant(n3))
timeeeeeeee(constant(n4))

print("Linear: ")
timeeeeeeee(linear(n1))
timeeeeeeee(linear(n2))
timeeeeeeee(linear(n3))
timeeeeeeee(linear(n4))

print("Quadratic: ")
timeeeeeeee(quadratic(n1))
timeeeeeeee(quadratic(n2))
timeeeeeeee(quadratic(n3))
timeeeeeeee(quadratic(n4))

print("Logarithmic Linear: ")
timeeeeeeee(logarithmic_linear(n1))
timeeeeeeee(logarithmic_linear(n2))
timeeeeeeee(logarithmic_linear(n3))
timeeeeeeee(logarithmic_linear(n4))

arr = np.array(list_time) # เปลี่ยนข้อมูล list เป็น numpy เพื่อเข้าถึงข้อมูลตัวเลขได้รวดเร็วขึ้น
plt.title('Execution Times') #ตั้งชื่อกราฟ
plt.plot(arr[0:4], label ='Constant') 
#ดึงข้อมูลตัวที่ 0-3 ซึ่งเป็นข้อมูลที่ได้จากการคำนวณเวลาการทำงานของฟังก์ชั่นแบบ O(1) พร้อมระบุว่าเป็นเส้นข้อมูลของฟังก์ชั่นไหน
plt.plot(arr[4:8], label='Linear') 
#ดึงข้อมูลตัวที่ 4-7 ซึ่งเป็นข้อมูลที่ได้จากการคำนวณเวลาการทำงานของฟังก์ชั่นแบบ O(n) พร้อมระบุว่าเป็นเส้นข้อมูลของฟังก์ชั่นไหน
plt.plot(arr[8:12], label ='Quadratic') 
#ดึงข้อมูลตัวที่ 8-11 ซึ่งเป็นข้อมูลที่ได้จากการคำนวณเวลาการทำงานของฟังก์ชั่นแบบ O(n**2) พร้อมระบุว่าเป็นเส้นข้อมูลของฟังก์ชั่นไหน
plt.plot(arr[12:], label='Logarithmic Linear') 
#ดึงข้อมูลตัวที่ 12 ถึงตัวสุดท้าย ซึ่งเป็นข้อมูลที่ได้จากการคำนวณเวลาการทำงานของฟังก์ชั่นแบบ O(nlogn) พร้อมระบุว่าเป็นเส้นข้อมูลของฟังก์ชั่นไหน
plt.legend() #สร้างพื้นที่เพื่อใส่รายละเอียดของเส้นข้อมูลแต่ละเส้น
plt.show() #คำสั่งแสดงผลกราฟที่ใส่ข้อมูลเข้าไปเรียบร้อยแล้ว