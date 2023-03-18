print("Hello World")
baslik = "kredi"
print(baslik)
#string metin
baslik1 = "ihtiyaç Kredisi"
#int
vade = 10
#bool boolean
isBool = True or False
#float
not1 = 43.5

#--------------------------

print(1 == 1) #true
print(1 != 1) #False 
print(1 < 2) #True
print(1 > 2) #False
print(1 <= 1) #True
print(1 >= 2) #False
#----------------------

#or and

print(1 > 2 or 5 > 2) #True
print(1>2 and 5 > 2)  #False
print(1>2 or 5>1 and 3>2) #True
#-----------------------------

# karar yapıları 
#if else
sayi1 = 10
sayi2 = 15
#sayi1 sayi2den büyükse ekrana sayi 1 daha büyük yazdır.

if (sayi1>sayi2):
    print("sayi1 büyük")
elif(sayi1 == sayi2):
    print("sayilar eşit")
else:
    print("sayi1 büyük değil")