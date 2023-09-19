import random

# ฟังก์ชันสำหรับสร้างตัวเลขสุ่มที่โปรแกรมกำหนด
def generate_bingo_number():
    return 25

# ฟังก์ชันสำหรับรับตัวเลขจากผู้ใช้
def get_user_guess():
    user_guess = int(input("กรุณาป้อนตัวเลขของคุณ: "))
    return user_guess

# ฟังก์ชันสำหรับตรวจสอบว่าตัวเลขที่ผู้ใช้ทายตรงกับตัวเลขของโปรแกรมหรือไม่
def check_bingo(user_guess, bingo_number):
    if user_guess == bingo_number:
        return True
    else:
        return False

# เรียกใช้งานฟังก์ชันและเริ่มเกม
def main():
    bingo_number = generate_bingo_number()
    user_guess = get_user_guess()
    
    if check_bingo(user_guess, bingo_number):
        print("Correct, You are the winner!")
    else:
        print("Not Correct !!!")

# เรียกใช้งานฟังก์ชันหลักเพื่อเริ่มเกม
main()
