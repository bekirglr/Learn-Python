#kütüphane 
import pandas as pd
#veri aktarımı 
data = pd.read_csv("data/veri.csv")
data2 = pd.read_csv("data/EskiCalisanlar.csv")
#sınıf belirtisi
print("\nVeri Sınıfı Algılandı:")
print(type(data))
print(type(data2))
anasayfa = """
1-) birinci soru : Satır ve Sütün Yazdırma
"""


menu = input(anasayfa + "\n Lütfen bir değer giriniz : ")
while 1:
	if menu == "1":
		print("Birinci Data (Veri.csv)")
		print("Satır sayısı:") #data 0 dan saymaya başladı için 1 eksik gözüküyor gibi gözüksede aslında tam sayısını veriyor
		print(len(data))
		print ("Sütun Sayısı:")
		print(len(data.columns))
		print("satır ve sütun sayısı:")
		print(data.shape)
		print(data.shape[0] * data.shape[1])
		print("İkinci Data (EskiCalisanlar.csv)")
		print(len(data2))
		print(data2.columns)
		print ("Sütun Sayısı:")
		print(len(data2.columns))
		print("satır ve sütun sayısı:")
		print(data2.shape)
		print(data2.shape[0] * data2.shape[1])
		print(data2.head())
 
		# obtaining the shape
		print("shape of dataframe", data2.shape)
	 
		# obtaining the number of rows
		print("number of rows : ", data2.shape[0])
	 
		# obtaining the number of columns
		print("number of columns : ", data2.shape[1])
		break
	else:
		print("menüde bulunamadı")