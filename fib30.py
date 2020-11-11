#İlk 30 Fibonacci sayısı yazdırma

def fib(n):
    if n == 1 :
        return n
    elif n == 0 :
        return 0
    else :
        return (fib(n-1) + fib(n-2))
kacsayi= int(input("İlk kaç sayıyı yazdıracaksınız? "))
if kacsayi <= 0 :
    print("Pozitif sayı giriniz")
    kacsayi= int(input("İlk kaç sayıyı yazdıracaksınız? "))
else :
    for i in range(kacsayi) :
        print(fib(i), end=" ")
          
