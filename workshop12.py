# ฟังก์ชันสำหรับคำนวณค่าใช้จ่ายในการซื้อแพ็กเกจท่องเที่ยว
def calculate_package_cost(num_people):
    if num_people <= 2:
        cost_per_person = 300
    elif num_people <= 5:
        cost_per_person = 250
    elif num_people <= 10:
        cost_per_person = 210
    else:
        cost_per_person = 150

    total_cost = num_people * cost_per_person
    average_cost = total_cost / num_people

    return total_cost, average_cost

# ฟังก์ชันสำหรับรับข้อมูลจากผู้ใช้
def get_user_input():
    tour_leader_name = input("กรุณาป้อนชื่อหัวหน้ากรุ๊ปทัวร์: ")
    contact_number = input("กรุณาป้อนเบอร์โทรศัพท์ติดต่อกลับ: ")
    num_people = int(input("กรุณาป้อนจำนวนคนที่จะไปทัวร์: "))
    return tour_leader_name, contact_number, num_people

# ฟังก์ชันสำหรับแสดงผลลัพธ์
def display_result(tour_leader_name, contact_number,num_people, total_cost, average_cost):
    print(f"ชื่อหัวหน้ากรุ๊ปทัวร์: {tour_leader_name}")
    print(f"เบอร์โทรศัพท์ติดต่อกลับ: {contact_number}")
    print(f"จำนวนคนที่จะไปทัวร์:{num_people} คน")
    print(f"ค่าใช้จ่ายทั้งหมด: {total_cost} บาท")
    print(f"ค่าเฉลี่ย: {average_cost} บาท/คน")

# เรียกใช้งานฟังก์ชันและแสดงผลลัพธ์
def main():
    tour_leader_name, contact_number, num_people = get_user_input()
    total_cost, average_cost = calculate_package_cost(num_people)
    display_result(tour_leader_name, contact_number, total_cost, average_cost)

# เรียกใช้งานฟังก์ชันหลักเพื่อเริ่มโปรแกรม
main()
