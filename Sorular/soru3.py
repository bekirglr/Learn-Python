#1-10 arası tek ve çift sayıların ayrı ayrı toplamı
t_toplam=0
c_toplam=0
for i in range(0,11):
    if i%2==1:
        t_toplam=t_toplam+i
    elif i%2==0:
        c_toplam=c_toplam+i
print("tek sayıların toplamı: ",t_toplam)
print("cift sayıların toplamı: ",c_toplam)