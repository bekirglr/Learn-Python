ad_soyad=input("Adınız ve soyadınızı girin")
yas=int(input("Yaşınızı girin"))
if yas>40:
    print("Yas sınırını aştınız.")
    print("Mülakat başarısız")
else:
    cevap=input("İngilizce ve ya Fransızca biliyor musunuz? E/H")
    if cevap=="H":
        print("Dil şartını sağlamıyorsunuz")
        print("Mülakat başarısız")
    elif cevap=="E":
        print("Tebrikler" , ad_soyad," Mülakat başarılı")
    else: print("Yanlış giriş")
