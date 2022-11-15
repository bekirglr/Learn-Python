vize=int(input("Vize notunu girin: "))
final=int(input("Final notunu girin: "))
ortalama=(vize*0.4)+(final*0.6)
print(ortalama)
if ortalama>40:
    print("Geçtiniz!")
else: print("Kaldınız!")