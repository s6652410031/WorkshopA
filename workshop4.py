# นิยามฟังก์ชันสำหรับคำนวณค่า y จาก x
def calculate_y(x):
    y = 2 * x**2 + 2 * x + 1
    return y

# ฟังก์ชันสำหรับรับค่า x จากผู้ใช้
def get_input():
    x = float(input("กรุณาป้อนค่า x: "))
    return x

# ฟังก์ชันสำหรับแสดงผลลัพธ์
def display_result(x, y):
    print(f"สำหรับ x = {x}, y = {y}")

# เรียกใช้งานฟังก์ชัน
x_value = get_input()
y_value = calculate_y(x_value)
display_result(x_value, y_value)
