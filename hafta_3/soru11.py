#Asal sayı bulan kod
sayi=int(input("Bir sayı girin"))
for i in range(2,sayi):
    if sayi%i==0:
        print("Asal değildir")
        break
    else:
        print("Sayı asaldır")
