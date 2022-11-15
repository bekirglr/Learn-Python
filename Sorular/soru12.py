#kelime içerisinde sesli harf bulma
i = 0
kelime =input("bir kelime giriniz:")
sesli = "aeıioöuü"
for x in kelime:
    if x in sesli:
        i +=1

print (i)