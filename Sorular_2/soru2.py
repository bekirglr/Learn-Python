#en büyük ve en küçük olan sayıları bulma
sifirMi=True
eb=0
ek=0
while sifirMi:
    
    sayi=int(input("Bir sayı girin"))
    if sayi==0:
        break
    else:
        if sayi>eb:
            eb=sayi
        elif sayi<ek:
            ek=sayi
            
print("En büyük",eb)
print("En küçük",ek)