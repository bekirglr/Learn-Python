#Net hesaplama

dogruSayisi=int(input("Doğru sayısını girin: "))
yanlisSayisi=int(input("Yanlış sayısını girin: "))

dogruPuan=0
yanlisPuan=0
toplamPuan=0

toplamSoru=dogruSayisi+yanlisSayisi

if toplamSoru==10:
    dogruPuan=dogruSayisi*10
    yanlisPuan=yanlisSayisi*-5
    toplamPuan=yanlisPuan+dogruPuan
    print("Toplam puanınız = ",toplamPuan,"'tir.")
else:
    print("Soru sayılarını kontrol edin!")