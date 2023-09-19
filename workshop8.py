# ฟังก์ชันสำหรับตรวจสอบค่า pH และคืนผลลัพธ์
def check_ph_value(ph_value):
    if 7 <= ph_value <= 8:
        return "Result is Normal"
    elif ph_value > 8:
        return "Result is Acid"
    else:
        return "Result is Alkali"

# ฟังก์ชันสำหรับรับข้อมูลจากผู้ใช้
def get_input():
    province_name = input("กรุณาป้อนชื่อจังหวัด: ")
    ph_value = float(input("กรุณาป้อนค่า pH ของน้ำประปา: "))
    return province_name, ph_value

# ฟังก์ชันสำหรับแสดงผลลัพธ์
def display_result(province_name, result):
    print(f"จังหวัด: {province_name}")
    print(f"ผลลัพธ์: {result}")

# เรียกใช้งานฟังก์ชันและแสดงผลลัพธ์
def main():
    province_name, ph_value = get_input()
    result = check_ph_value(ph_value)
    display_result(province_name, result)

# เรียกใช้งานฟังก์ชันหลักเพื่อเริ่มโปรแกรม
main()
