# ฟังก์ชันสำหรับตรวจสอบผลการเรียนของนักเรียน
def check_student_result(grade):
    if grade >= 2.00:
        return "สอบผ่าน"
    else:
        return "สอบไม่ผ่าน"

# ฟังก์ชันสำหรับรับข้อมูลจากผู้ใช้
def get_student_info():
    student_id = input("กรุณาป้อนรหัสนักเรียน: ")
    student_name = input("กรุณาป้อนชื่อนักเรียน: ")
    student_grade = float(input("กรุณาป้อนเกรดเฉลี่ยนักเรียน: "))
    return student_id, student_name, student_grade

# ฟังก์ชันสำหรับแสดงผลลัพธ์
def display_result(student_id, student_name, result):
    print(f"รหัสนักเรียน: {student_id}")
    print(f"ชื่อนักเรียน: {student_name}")
    print(f"ผลการเรียน: {result}")

# เรียกใช้งานฟังก์ชันและแสดงผลลัพธ์
def main():
    num_students = int(input("กรุณาป้อนจำนวนนักเรียนที่ต้องการตรวจสอบ: "))
    
    for _ in range(num_students):
        student_id, student_name, student_grade = get_student_info()
        result = check_student_result(student_grade)
        display_result(student_id, student_name, result)

# เรียกใช้งานฟังก์ชันหลักเพื่อเริ่มโปรแกรม
main()
