#Ʃ sembolüne göre klavyeden girilen n sayısı için işlemin sonucunu hesaplayıp ekrana yazan programın kodunu yazınız.​

n=int(input("Ʃ için bir üst sayısı giriniz: "))
k=0
for i in range(1,n+1):
    k=k+i
sonuc=(5*k)+6
print("sonuc: ",sonuc)
