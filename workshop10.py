# ฟังก์ชันสำหรับแสดงข้อความต้อนรับ
def welcome_message(year):
    if year == 1:
        return "Welcome Freshman"
    elif year == 2:
        return "Welcome Sophomore"
    elif year == 3:
        return "Welcome Junior"
    elif year == 4:
        return "Welcome Senior"
    else:
        return "Invalid Year"

# ฟังก์ชันสำหรับรับข้อมูลจากผู้ใช้
def get_year():
    year = int(input("กรุณาป้อนชั้นปี (1-4): "))
    return year

# ฟังก์ชันสำหรับแสดงผลลัพธ์
def display_result(message):
    print(message)

# เรียกใช้งานฟังก์ชันและแสดงผลลัพธ์
def main():
    year = get_year()
    message = welcome_message(year)
    display_result(message)

# เรียกใช้งานฟังก์ชันหลักเพื่อเริ่มโปรแกรม
main()
