kontrol=True
turkce_karakter="ığüşöçĞÜİÖÇ"

while kontrol:
    sifre=input("Şifrenizi girin")
    for i in sifre:
        if i not in turkce_karakter:
             print("Şifreniz oluşturuldu")
             kontrol=False
        else:
             kontrol=False
             print("Türkçe karakter kullanmayın")