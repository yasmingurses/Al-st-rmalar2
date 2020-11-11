#1'den n'e rekürsif çarpım

def rekcar(n):
   if n <= 1:
       return n
   else:
       return n * rekcar(n-1)

#Buraya herhangi bir sayı ekleyebilirim
print(rekcar(5))
