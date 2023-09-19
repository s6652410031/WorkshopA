# นิยามฟังก์ชันสำหรับคำนวณเงินเดือนสุทธิ
def calculate_net_salary(salary):
    tax = (salary * 7) / 100
    social_security = 500
    net_salary = salary - tax - social_security
    return net_salary

# ฟังก์ชันสำหรับรับข้อมูลจากผู้ใช้
def get_employee_info():
    employee_id = input("กรุณาป้อนรหัสพนักงาน: ")
    employee_name = input("กรุณาป้อนชื่อพนักงาน: ")
    basic_salary = float(input("กรุณาป้อนเงินเดือนปกติ: "))
    return employee_id, employee_name, basic_salary

# ฟังก์ชันสำหรับแสดงผลลัพธ์
def display_result(employee_id, employee_name, net_salary):
    print(f"รหัสพนักงาน: {employee_id}")
    print(f"ชื่อพนักงาน: {employee_name}")
    print(f"เงินเดือนสุทธิ: {net_salary:.2f} บาท")

# เรียกใช้งานฟังก์ชัน
employee_id, employee_name, basic_salary = get_employee_info()
net_salary = calculate_net_salary(basic_salary)
display_result(employee_id, employee_name, net_salary)
