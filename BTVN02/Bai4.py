tien = int(input("Nhap so tien: "))
soBia = tien // 28
tongBia = soBia
vo = soBia
while vo >= 3:
    biaMoi = vo // 3
    tongBia += biaMoi
    vo = vo % 3 + biaMoi
print("Tong so bia co the uong:", tongBia)