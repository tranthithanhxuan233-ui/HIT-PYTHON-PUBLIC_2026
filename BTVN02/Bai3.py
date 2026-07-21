import math
x = int(input("Nhap n = "))
giaTri = abs(x)
if giaTri == 0:
    soChuSo = 1
    tong = 0
else:
    soChuSo = 0
    tong = 0
    while giaTri != 0:
        tong += giaTri % 10
        soChuSo += 1
        giaTri //= 10
print("So chu so la:", soChuSo)
print("Tong cac chu so la:", tong)
if x >= 2:
    laSNT = True
    gioiHan = int(math.sqrt(x))
    for i in range(2, gioiHan + 1):
        if x % i == 0:
            laSNT = False
            break
    if laSNT:
        print(x, "la so nguyen to")
    else:
        print(x, "khong phai la so nguyen to")
else:
    print(x, "khong phai la so nguyen to")