

def calculate_selling_price():
    product_name = input("กรุณาป้อนชื่อสินค้า: ")
    cost_price = float(input("กรุณาป้อนราคาสินค้าต้นทุน: "))
    
    selling_price = cost_price + (cost_price * 10 / 100)
    
    print(f"สินค้า: {product_name}")
    print(f"ราคาขายสินค้า: {selling_price:.2f} บาท")

# เรียกใช้ฟังก์ชัน
calculate_selling_price()

def calculate_selling_price():
    product_name = input("กรุณาป้อนชื่อสินค้า: ")
    cost_price = float(input("กรุณาป้อนราคาสินค้าต้นทุน: "))
    
    selling_price = cost_price + (cost_price * 10 / 100)
    
    return selling_price

# เรียกใช้ฟังก์ชันและรับค่าที่คืนมา
result = calculate_selling_price()
print(f"ราคาขายสินค้า: {result:.2f} บาท")

def calculate_selling_price(product_name, cost_price):
    selling_price = cost_price + (cost_price * 10 / 100)
    
    return selling_price

# รับข้อมูลจากผู้ใช้
product_name = input("กรุณาป้อนชื่อสินค้า: ")
cost_price = float(input("กรุณาป้อนราคาสินค้าต้นทุน: "))

# เรียกใช้ฟังก์ชันและรับค่าที่คืนมา
result = calculate_selling_price(product_name, cost_price)
print(f"ราคาขายสินค้า: {result:.2f} บาท")
