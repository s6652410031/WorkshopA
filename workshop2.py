def calculate_average_score():
    student_id = input("กรุณาป้อนรหัสนักเรียน: ")
    student_name = input("กรุณาป้อนชื่อนักเรียน: ")
    
    total_score = 0
    for i in range(1, 4):
        score = float(input(f"กรุณาป้อนคะแนนสอบครั้งที่ {i}: "))
        total_score += score
    
    average_score = total_score / 3
    
    print(f"รหัสนักเรียน: {student_id}")
    print(f"ชื่อนักเรียน: {student_name}")
    print(f"ค่าเฉลี่ยคะแนน: {average_score:.2f}")

# เรียกใช้ฟังก์ชัน
calculate_average_score()

def calculate_average_score():
    student_id = input("กรุณาป้อนรหัสนักเรียน: ")
    student_name = input("กรุณาป้อนชื่อนักเรียน: ")
    
    total_score = 0
    for i in range(1, 4):
        score = float(input(f"กรุณาป้อนคะแนนสอบครั้งที่ {i}: "))
        total_score += score
    
    average_score = total_score / 3
    
    return average_score

# เรียกใช้ฟังก์ชันและรับค่าที่คืนมา
result = calculate_average_score()
print(f"ค่าเฉลี่ยคะแนน: {result:.2f}")

def calculate_average_score(student_id, student_name, scores):
    total_score = sum(scores)
    average_score = total_score / len(scores)
    
    print(f"รหัสนักเรียน: {student_id}")
    print(f"ชื่อนักเรียน: {student_name}")
    print(f"ค่าเฉลี่ยคะแนน: {average_score:.2f}")

# รับข้อมูลจากผู้ใช้
student_id = input("กรุณาป้อนรหัสนักเรียน: ")
student_name = input("กรุณาป้อนชื่อนักเรียน: ")

scores = []
for i in range(1, 4):
    score = float(input(f"กรุณาป้อนคะแนนสอบครั้งที่ {i}: "))
    scores.append(score)

# เรียกใช้ฟังก์ชันและส่งข้อมูลผ่านพารามิเตอร์
calculate_average_score(student_id, student_name, scores)
