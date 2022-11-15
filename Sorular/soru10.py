#Klavyeden 0 girilene kadar, girilen sayıların kaçı negatif? kaçı pozitif? Sayıların ortalaması ? bulan algoritma

sifirMi=True
negaSayac=0
pozSayac=0
toplam=0
while sifirMi:
    sayi=int(input("Bir sayı girin"))
    if sayi ==0:
        sifirMi=False
    elif sayi<0:
        toplam+=toplam+sayi
        negaSayac=negaSayac+1
    else:
        toplam=toplam+sayi
        pozSayac=pozSayac+1
        
ort=toplam/(pozSayac+negaSayac)
print("Ortalama ",ort)