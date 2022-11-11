#ikinci dereceden bir bilinmeyenli fonksiyonlarda kök hesaplama

print("2.Dereceden Bir Denklemin Kökünü Bulma")
a=int(input("a : "))
b=int(input("b : "))
c=int(input("c : "))
 
delta=b**2-4*a*c

if (delta < 0):
  print ("denklemin reel kökü yok.")
elif (delta == 0):
  print ("birinci kök = ikinci kök :", (-b/2*a))
else:  
  x1=(-b-delta**0.5)/(2*a)
  x2=(-b+delta**0.5)/(2*a)
  print("Birinci Kök : {}\nİkinci Kök : {}".format(x1,x2))