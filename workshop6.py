# นิยามฟังก์ชันสำหรับคำนวณอัตราดอกเบี้ยเงินกู้
def calculate_interest_rate(loan_amount):
    if loan_amount >= 1000:
        interest_rate = 2.5
    else:
        interest_rate = 5.5
    return interest_rate

# ฟังก์ชันสำหรับรับข้อมูลจากผู้ใช้
def get_loan_info():
    borrower_name = input("กรุณาป้อนชื่อผู้กู้: ")
    loan_amount = float(input("กรุณาป้อนจำนวนเงินกู้ (บาท): "))
    return borrower_name, loan_amount

# ฟังก์ชันสำหรับแสดงผลลัพธ์
def display_result(borrower_name, interest_rate):
    print(f"ชื่อผู้กู้: {borrower_name}")
    print(f"อัตราดอกเบี้ยเงินกู้: {interest_rate:.2f}%")

# เรียกใช้งานฟังก์ชัน
borrower_name, loan_amount = get_loan_info()
interest_rate = calculate_interest_rate(loan_amount)
display_result(borrower_name, interest_rate)
