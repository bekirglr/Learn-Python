cumle="Klavyeden girilen bir kelime içindeki sesli harfleri bulan kodu yazınız."
sayac=0
harf=input("aranacak harfi girin")
for i in cumle:
    if i==harf:
        sayac=sayac+1
        
print(harf," harfi cümle içinde",sayac," tane var")