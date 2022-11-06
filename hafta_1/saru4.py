#Kullanıcının girdiği sayının rakamlarının toplamı

sayi=int(input("Bir sayı girin: "))

birler=sayi%10
yuzler=(int)(sayi/100)
onlar_1=(int)(sayi/10)
onlar=onlar_1%10
print("Yüzler:",yuzler," Onlar:", onlar," Birler:",birler)
print("Toplam: ",yuzler+onlar+birler)