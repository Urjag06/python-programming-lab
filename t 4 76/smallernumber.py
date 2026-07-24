a = int(input("enter a number"))
b = int(input("enter b number"))
c = int(input("enter c number"))

if a > b:
    if a > c:
       print(a," is smaller")
    else:
       print(c,"is smaller")
else:
   if b > c:
      print(b,"is smaller")
   else:
      print(c,"is smaller")
