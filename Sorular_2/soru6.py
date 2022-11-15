kontrol=True
while kontrol:
    sifre=input("Şifrenizi girin")
    uzunluk=len(sifre)
    if uzunluk==4:
        print("Şifreniz oluşturuldu")
        kontrol=False
    else:
        print("Şifreyi yeniden girin")