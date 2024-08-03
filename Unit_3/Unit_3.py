height = int(input("กรุณาใส่จำนวนแถวสำหรับ pattern ที่ต้องการ: "))

def pyramid_pattern(x):
    # Pattern 1
    pattern1 = []
    for i in range(1, x + 1):
        ans1 = '*' * i
        pattern1.append(ans1)

    # Pattern 2
    pattern2 = []
    for n in range(height, 1, -1):
        ans2 = '*' * n
        pattern2.append(ans2)

    # Pattern 3
    pattern3 = []
    for i in range(height):
        line = ""
        for j in range(height - i - 1):
            line += " "
        for k in range(i + 1):
            line += "* "
        pattern3.append(line.rstrip())

    # Pattern 4
    pattern4 = []
    for i in range(height, 0, -1):
        line = ""
        for j in range(height - i):
            line += ""
        for k in range(i):
            line += "* "
        pattern4.append(line.rstrip()) #rstrip() ลบช่องว่างหรืออักขระที่ระบุทางด้านขวาสุด (ขอบขวา)

    # Pattern 5
    pattern5 = []
    for i in range(height):
        line = ""
        for J in range(height - i - 1):
            line += ""
        for K in range(i + 1):
            line += "*"
        pattern5.append(line.rstrip())
    
    return pattern1, pattern2, pattern3, pattern4, pattern5

result1, result2, result3, result4, result5 = pyramid_pattern(height)

allR = [result1, result2, result3, result4, result5]

for i, pattern in enumerate(allR): #enumerate เป็นตัวช่วยการวนผ่านรายการทั้งหมดของ allR
    for line in pattern:
        print(line)
    if i < len(allR) - 1:  # เพิ่มบรรทัดคั่นยกเว้นหลังแพทเทิร์นสุดท้าย
        print('-------------')