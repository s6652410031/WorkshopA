# ฟังก์ชันสำหรับคำนวณค่าโทรศัพท์
def calculate_phone_bill(minutes):
    if minutes <= 15:
        cost = minutes * 5
    elif minutes <= 30:
        cost = 15 * 5 + (minutes - 15) * 3
    else:
        cost = 15 * 5 + 15 * 3 + (minutes - 30) * 1.50
    return cost

# ฟังก์ชันสำหรับรับข้อมูลจากผู้ใช้
def get_user_info():
    user_name = input("กรุณาป้อนชื่อผู้ใช้โทรศัพท์: ")
    phone_number = input("กรุณาป้อนเบอร์โทรศัพท์: ")
    minutes = int(input("กรุณาป้อนจำนวนนาทีที่ใช้โทรศัพท์: "))
    return user_name, phone_number, minutes

# ฟังก์ชันสำหรับแสดงผลลัพธ์
def display_result(user_name, phone_number, minutes, cost):
    print(f"ชื่อผู้ใช้โทรศัพท์: {user_name}")
    print(f"เบอร์โทรศัพท์: {phone_number}")
    print(f"จำนวนนาทีที่ใช้โทรศัพท์: {minutes} นาที")
    print(f"ค่าโทรศัพท์ที่คิด: {cost:.2f} บาท")

# เรียกใช้งานฟังก์ชันและแสดงผลลัพธ์
def main():
    user_name, phone_number, minutes = get_user_info()
    cost = calculate_phone_bill(minutes)
    display_result(user_name, phone_number, minutes, cost)

# เรียกใช้งานฟังก์ชันหลักเพื่อเริ่มโปรแกรม
main()
