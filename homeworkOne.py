#Pythonda dört veri tipi vardır
#1. string yani yazı tipi kullanıcıya bir metin vermek istediğimizde kullanıyoruz.
print("Çift tirnağin içine bu şekilde yazdığım her şey birer string'dir")

#2. int veri tipi sayılar için kullanılır bu sayılarla matematiksel hesaplar yaparız.
print(5**3)  # eğer çift tırnak içine alsaydım string olarak görecekti ve bu şekilde gözükecekti
print("5**3") #yani hesabı yapmadı ve yazı olarak bize aktardı

#3. Float bu veri tipini ise ondalıklı sayıları yazarken kullanıyoruz.
x = type(45.5)
print(x)  #<class Float>

#4. Bool diğer adıyla Boolen bu veri tipi ise bize True ya da False'u verir(Filmlerdeki 01011110 gibi)
isBool = True
print(type(isBool)) #<class bool>
#--------------------------------------------------------------------------------------------------------------
#Kodlama.io sitesinde değişken olarak kullanıldığını düşündüğünüz verileri, veri tipleriyle birlikte örneklendiriniz.

#string için 
print("(2023) Yazılım Geliştirici Yetiştirme Kampı - Python & Selenium")

# int ve float için başarım yüzdesi
x = float(input("bir sayi giriniz:"))
print("% ", x)

#boolen ile bir puan sistemi yapabiliriz
kullaniciPuan = 0
isOdev = False
if(isOdev):
    print("Puaniniz",( kullaniciPuan + 5))
else:
    print("puaniniz", kullaniciPuan) 
#-------------------------------------------------------------------------------------------------------------
#Kodlama.io sitesinde şart blokları kullanıldığını düşündüğünüz kısımları örneklendiriniz ve Python dilinde bu örnekleri koda dökünüz.
#Kullanıcı giriş ekranını if bloklarıyla bu şekilde yazabiliriz en sondaki güvenlik açığını lütfen patrona söylemeyin :)

username = "kty"
password = "kty"
x = str(input("Kullanici adinizi giriniz:"))
y = str(input("Şifrenizi giriniz:"))
isbool = username == x and password == y

if (isbool):
    print("Hoş geldin", username)
else:
    print("Hatali giriş şifreniz şu olabilir mi?",password)