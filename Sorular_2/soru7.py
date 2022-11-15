#otoparkta geçirilen süre ve ücretini hesaplama
kalinan_saat=int(input("Kaldığınız saati girin"))
toplam_ucret=0
if kalinan_saat<=1:
    toplam_ucret=5
elif (kalinan_saat>1) and (kalinan_saat<=5):
    toplam_ucret=kalinan_saat*4
elif kalinan_saat>5:
    toplam_ucret=kalinan_saat*3
    
print("Ödeyeceğiniz miktar =",toplam_ucret)