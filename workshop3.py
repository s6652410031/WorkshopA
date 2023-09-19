def calculate_tax():
    product_name = input("กรุณาป้อนชื่อสินค้า: ")
    product_price = float(input("กรุณาป้อนราคาสินค้า: "))
    
    tax = product_price * 7 / 100
    
    print(f"สินค้า: {product_name}")
    print(f"ภาษีที่ต้องจ่าย: {tax:.2f} บาท")

# เรียกใช้ฟังก์ชัน
calculate_tax()

def calculate_tax(product_price):
    tax = product_price * 7 / 100
    return tax

# รับข้อมูลจากผู้ใช้
product_name = input("กรุณาป้อนชื่อสินค้า: ")
product_price = float(input("กรุณาป้อนราคาสินค้า: "))

# เรียกใช้ฟังก์ชันและรับค่าที่คืนมา
result = calculate_tax(product_price)
print(f"ภาษีที่ต้องจ่ายสำหรับสินค้า {product_name}: {result:.2f} บาท")

def calculate_tax(product_name, product_price):
    tax = product_price * 7 / 100
    print(f"สินค้า: {product_name}")
    print(f"ภาษีที่ต้องจ่าย: {tax:.2f} บาท")

# รับข้อมูลจากผู้ใช้
product_name = input("กรุณาป้อนชื่อสินค้า: ")
product_price = float(input("กรุณาป้อนราคาสินค้า: "))

# เรียกใช้ฟังก์ชันและส่งข้อมูลผ่านพารามิเตอร์
calculate_tax(product_name, product_price)
