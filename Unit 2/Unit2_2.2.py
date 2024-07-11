# ฟังก์ชัน Recursive เพื่อพิมพ์ดาวจากน้อยไปมาก
def print_stars_increasing(n):
    if n > 0:
        print_stars_increasing(n - 1)  
        print('*' * n)
 
# ฟังก์ชัน Recursive ดาวจากมากไปน้อย
def print_stars_decreasing(n):
    if n > 0:
        print('*' * n)
        print_stars_decreasing(n - 1)  
 
# ฟังก์ชัน Recursive ดาวตรงกลาง
def print_centered_pattern_recursive(n, current=1):
    if current <= n:
        print(' ' * (n - current) + '* ' * current)
        print_centered_pattern_recursive(n, current + 1)  
 
# ฟังก์ชัน Recursive ดาวตรงกลางกลับด้าน
def print_reversed_centered_pattern_recursive(n, current=None):
    if current is None:
        current = n
    if current > 0:
        print(' ' * (n - current) + '* ' * current)
        print_reversed_centered_pattern_recursive(n, current - 1)  
 
# ฟังก์ชัน Recursive ดาวจากน้อยไปมาก
def print_stars_increasing_no_space(n, current=1):
    if current <= n:
        print(' ' * (n - current) + '*' * current)
        print_stars_increasing_no_space(n, current + 1)  
 
# รับค่าจากผู้ใช้
rows = int(input("กรอกแถว : "))
 
# ตรวจสอบความถูกต้องของค่าที่กรอก
if rows < 1 :
    print("กรอกเฉพาะ 1 ถึง 5 เท่านั้น")
else:
    print("\nดาวจากน้อยไปมาก:")
    print_stars_increasing(rows)
 
    print("\n---------------------------------------")
 
    print("ดาวจากมากไปน้อย:")
    print_stars_decreasing(rows)
 
    print("\n---------------------------------------")
 
    # แบบดาวที่จัดกลาง
    print("ดาวที่อยู่ตรงกลาง:")
    print_centered_pattern_recursive(rows)
 
    print("\n---------------------------------------")
 
    print("ดาวที่อยู่ตรงกลางกลับด้าน :")
    print_reversed_centered_pattern_recursive(rows)
 
    print("\n---------------------------------------")
 
    print("ดาวจากน้อยไปมาก :")
    print_stars_increasing_no_space(rows)