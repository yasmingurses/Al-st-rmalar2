#1'den n'e rekürsif toplam

def rektop(n):
   if n <= 1:
       return n
   else:
       return n + rektop(n-1)

print(rektop(19))
