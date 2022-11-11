#Sayı tahmin oyunu
import random
sayi=random.randint(0,100)
for i in range(0,3):
    tahmin=int(input("Tahmin girin"))
    if sayi==tahmin:
        print("Tebrikler bildiniz")
        break
    else:
        print("Bi daha deneyin")