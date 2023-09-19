# ฟังก์ชันสำหรับคำนวณค่าคอมมิชชัน
def calculate_commission(sales_amount):
    if sales_amount <= 1000:
        commission = 0.0
    elif 1001 <= sales_amount <= 2000:
        commission = sales_amount * 0.01
    elif 2001 <= sales_amount <= 3000:
        commission = sales_amount * 0.03
    else:
        commission = sales_amount * 0.05
    return commission

# ฟังก์ชันสำหรับรับข้อมูลจากผู้ใช้
def get_employee_info():
    employee_id = input("กรุณาป้อนรหัสพนักงาน: ")
    employee_name = input("กรุณาป้อนชื่อพนักงาน: ")
    sales_amount = float(input("กรุณาป้อนยอดขาย (บาท): "))
    return employee_id, employee_name, sales_amount

# ฟังก์ชันสำหรับแสดงผลลัพธ์
def display_result(employee_id, employee_name, commission):
    print(f"รหัสพนักงาน: {employee_id}")
    print(f"ชื่อพนักงาน: {employee_name}")
    print(f"ค่าคอมมิชชัน: {commission:.2f} บาท")

# เรียกใช้งานฟังก์ชันและแสดงผลลัพธ์
def main():
    employee_id, employee_name, sales_amount = get_employee_info()
    commission = calculate_commission(sales_amount)
    display_result(employee_id, employee_name, commission)

# เรียกใช้งานฟังก์ชันหลักเพื่อเริ่มโปรแกรม
main()
