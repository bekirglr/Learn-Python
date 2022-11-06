 
sayi=int(input("Sayıyı Girin : "))
fact = 1
 
if sayi < 0:
   print("Negatif sayıların faktoriyeli hesaplanamaz.")
elif sayi == 0:
   print("0! = 1")
else:
   for i in range(1,sayi + 1):
       fact = fact*i
   print(sayi," sayısının faktoriyeli : ",fact)