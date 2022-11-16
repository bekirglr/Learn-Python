
print("--------------------------------------------------------------")
print("1. 1-10 arası sayıların toplamı")
print("2. 1-10 arası tek sayıların toplamı")
print("3. 1-10 arası tek ve çift sayıların ayrı ayrı toplamı")
print("4. Kullanıcının girdiği sayının rakamlarının toplamı")
print("5. Girilen sayının faktöriyelini hesaplama")
print("6. Ʃ sembolüne göre klavyeden girilen n sayısı için işlemin sonucunu hesaplayıp ekrana yazan programın kodunu yazınız.​")
print("7. İkinci dereceden bir bilinmeyenli fonksiyonlarda kök hesaplama")
print("8. Sayı tahmin oyunu")
print("9. Klavyeden 0 girilene kadar, girilen sayıların kaçı negatif? kaçı pozitif? Sayıların ortalaması ? bulan algoritma")
print("10. Asal sayı bulan kod")
print("11. Kelime içerisinde sesli harf bulma")
print("12. Kelime içerisinde kaç adet sesli harf olduğunu bulma")
print("13. Bir metin içerisnde ki sesli ve sessiz harfleri bulma")
print("14. Vize-final not ortalaması")
print("15. En büyük ve en küçük olan sayıları bulma")
print("16. Girilen kelimenin kaç karakterden oluştuğunu bulma")
print("17. Üs hesaplama")
print("18. Şifre oluşturma")
print("19. Otoparkta geçirilen süre ve ücretini hesaplama")
print("20. Şifre kontrol")
print("--------------------------------------------------------------")

soruSec=int(input("Lütfen çözmek istediğiniz algoritma sorusunu seçiniz: "))
#-----------------------------------------------------------------------------------------------
toplam=0
if soruSec==1:
    for i in range(0,11):                           # 1. SORU
        toplam=toplam+i
    print(toplam)
else:
    
#-----------------------------------------------------------------------------------------------
    toplam2=0

    if soruSec==2:
        
        for i in range(0,11):                           # 2. SORU
            if i%2==1:
                toplam2=toplam2+i
        print(toplam2)
    else:

#-----------------------------------------------------------------------------------------------
        t_toplam=0
        c_toplam=0

        if soruSec==3:
            for i in range(0,11):
                if i%2==1:
                    t_toplam=t_toplam+i                     # 3. SORU
                elif i%2==0:
                    c_toplam=c_toplam+i
            print("tek sayıların toplamı: ",t_toplam)
            print("cift sayıların toplamı: ",c_toplam)
        else:

#-----------------------------------------------------------------------------------------------
            if soruSec==4:
                sayi=int(input("Bir sayı girin: "))

                birler=sayi%10
                yuzler=(int)(sayi/100)
                onlar_1=(int)(sayi/10)                    # 4. SORU
                onlar=onlar_1%10
                print("Yüzler:",yuzler," Onlar:", onlar," Birler:",birler)
                print("Toplam: ",yuzler+onlar+birler)
            else:

#-----------------------------------------------------------------------------------------------
                if soruSec==5:
                    sayi=int(input("Sayıyı Girin : "))
                    fact = 1
                    
                    if sayi < 0:
                        print("Negatif sayıların faktoriyeli hesaplanamaz.")
                    elif sayi == 0:
                        print("0! = 1")                          # 5. SORU
                    else:
                        for i in range(1,sayi + 1):
                            fact = fact*i
                        print(sayi," sayısının faktoriyeli : ",fact)
                else:
#-----------------------------------------------------------------------------------------------
                    if soruSec==6:
                        dogruSayisi=int(input("Doğru sayısını girin: "))
                        yanlisSayisi=int(input("Yanlış sayısını girin: "))

                        dogruPuan=0
                        yanlisPuan=0
                        toplamPuan=0

                        toplamSoru=dogruSayisi+yanlisSayisi               # 6. SORU

                        if toplamSoru==10:
                            dogruPuan=dogruSayisi*10
                            yanlisPuan=yanlisSayisi*-5
                            toplamPuan=yanlisPuan+dogruPuan
                            print("Toplam puanınız = ",toplamPuan,"'tir.")
                        else:
                            print("Soru sayılarını kontrol edin!")
                    else:
#-----------------------------------------------------------------------------------------------
                        if soruSec==7:
                            n=int(input("Ʃ için bir üst sayısı giriniz: "))
                            k=0
                            for i in range(1,n+1):
                                k=k+i                                # 7. SORU
                            sonuc=(5*k)+6
                            print("sonuc: ",sonuc)
                        else:
#-----------------------------------------------------------------------------------------------
                            if soruSec==8:
                                print("2.Dereceden Bir Denklemin Kökünü Bulma")
                                a=int(input("a : "))
                                b=int(input("b : "))
                                c=int(input("c : "))
                                
                                delta=b**2-4*a*c                          # 8. SORU

                                if (delta < 0):
                                    print ("denklemin reel kökü yok.")
                                elif (delta == 0):
                                    print ("birinci kök = ikinci kök :", (-b/2*a))
                                else:  
                                    x1=(-b-delta**0.5)/(2*a)
                                    x2=(-b+delta**0.5)/(2*a)
                                    print("Birinci Kök : {}\nİkinci Kök : {}".format(x1,x2))
                            else:
#-----------------------------------------------------------------------------------------------
                                if soruSec==9:
                                    import random
                                    sayi=random.randint(0,100)
                                    for i in range(0,3):
                                        tahmin=int(input("Tahmin girin"))            # 9. SORU
                                        if sayi==tahmin:
                                            print("Tebrikler bildiniz")
                                            break
                                        else:
                                            print("Bi daha deneyin")
                                else:
#-----------------------------------------------------------------------------------------------
                                    if soruSec==10:
                                        sifirMi=True
                                        negaSayac=0
                                        pozSayac=0
                                        toplam=0
                                        while sifirMi:
                                            sayi=int(input("Bir sayı girin"))
                                            if sayi ==0:
                                                sifirMi=False                     # 10. SORU
                                            elif sayi<0:
                                                toplam+=toplam+sayi
                                                negaSayac=negaSayac+1
                                            else:
                                                toplam=toplam+sayi
                                                pozSayac=pozSayac+1
                                                
                                        ort=toplam/(pozSayac+negaSayac)
                                        print("Ortalama ",ort)
                                    else:
#-----------------------------------------------------------------------------------------------
                                        if soruSec==11:
                                            sayi=int(input("Bir sayı girin"))
                                            for i in range(2,sayi):
                                                if sayi%i==0:
                                                    print("Asal değildir")
                                                    break
                                                else:
                                                    print("Sayı asaldır")
                                        else:
#-----------------------------------------------------------------------------------------------
                                            if soruSec==12:
                                                i = 0
                                                kelime =input("bir kelime giriniz:")
                                                sesli = "aeıioöuü"
                                                for x in kelime:
                                                    if x in sesli:
                                                        i +=1

                                                print (i)
                                            else:
#-----------------------------------------------------------------------------------------------
                                                if soruSec==13:
                                                    cumle="Klavyeden girilen bir kelime içindeki sesli harfleri bulan kodu yazınız."
                                                    sayac=0
                                                    harf=input("aranacak harfi girin")
                                                    for i in cumle:
                                                        if i==harf:
                                                            sayac=sayac+1
                                                            
                                                    print(harf," harfi cümle içinde",sayac," tane var")
                                                else:
#-----------------------------------------------------------------------------------------------
                                                    if soruSec==14:
                                                        sesli_harfler = "aeıioöuü"
                                                        sessiz_harfler = "bcçdfgğhjklmnprsştvyz"
                                                        sesliler=""
                                                        sessizler=""
                                                        a=input("bir metin giriniz")

                                                        for i in a:
                                                            if i in sesli_harfler:
                                                                sesliler=sesliler+i
                                                            if i in sessiz_harfler:
                                                                sessizler=sessizler+i

                                                        print("sesli harfler",sesliler)
                                                        print("sessiz harfler",sessizler)
                                                    else:
                                                        print()
#-----------------------------------------------------------------------------------------------