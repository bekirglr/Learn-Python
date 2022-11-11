cumle="Klavyeden girilen bir kelime içindeki sesli harfleri bulan kodu yazınız."
sesli="aeiıouüö"
sessiz="qwrtypğsdghjklşzxcvbnmç"  
harfler_sesli=" "
harfler_sessiz=" "   

for i in  cumle:
    if i in sesli:
        harfler_sesli=harfler_sesli+i
    elif i in sessiz:
        harfler_sessiz=harfler_sessiz+i
        
print("Sesli harfler ",harfler_sesli)
print("Sessiz harfler ",harfler_sessiz)