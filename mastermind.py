import random
a = random.randrange(10,99)
while a%11 ==0 :
    a= random.randrange(10,99)

x = (input("10 ile 98 arası bir sayı giriniz: "))

dogruyer= 0
yanlısyer= 0

if int(x)<10 or int(x)>98 or int(x)%11 == 0:
    print("Düzgün sayı gir!")
    x = (input("10 ile 98 arası bir sayı giriniz: "))
else:
    if str(x)[0]== str(a)[0] or str(x)[1]== str(a)[1]:
        dogruyer = dogruyer + 1
    elif str(x)[0]==str(a)[1] or str(x)[1]==str(a)[0]:
        yanlısyer = yanlısyer + 1
print("Sayı şuydu: ", a)
print("Tahmin ettiğiniz sayı: {}".format(dogruyer))
print("Tahmin edemediginiz sayı: {}".format(yanlısyer))


