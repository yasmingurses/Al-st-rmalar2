#Kendi tanım aralığıma uyan random fonksyionu yaratma
# 10 ve 98 dahil iki basamağı aynı olan sayılar hariç

import random
def yenirandom():
  haric=[11,22,33,44,55,66,77,88]
  aralik = randint(10,98)
  return yenirandom() if aralik in haric else aralik 

#Kullanıcıdan sayı isteme
dogruyer = 0
x = int(input("Tahmin ettiğin sayıyı gir: "))

#Burada işler karıştı soruya tekrar bak


while 10 <= x <= 98 and x[0] != x[1] :
    if x[0] == int(yenirandom()[0]) or x[1] == int(yenirandom()[1]) :
        dogruyer = dogruyer + 1
    else :
        dogruyer = dogruyer - 1

print("Nizami sayı girmelisin!")
print("Sonuç: " , dogruyer)
