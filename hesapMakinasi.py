"""
Basit bir hesap makinası uygulaması Can Doruk tarafından yapılmıştır.


python hesapMakinasi.py ya da py hesapMakinasi.py terminale yazıp çalıştırabilirsiniz 

"""


def topla(x, y):
    return x + y

def cikar(x, y):
    return x - y

def carp(x, y):
    return x * y

def bol(x, y):
    return x / y

def usAlma(x,y):
    return x**y

def modAlma(x,y):
    return x%y
    

devam_Et = "0" or 0

while devam_Et == "0" or "0":
    print("""
Lütfen yapmak istediğiniz iş
10.hasanı sikeyimdafdsfasdf.......sdgklsşdfgkşgsidf
11.cana da basim
1- Toplama 
2- Çıkarma
3- Çarpma
4- Bölme   
5- Kare Alma
6- Mod Alma
7- Çıkış
""")

    secim = input("Seçiminiz:  ")

   

    if secim <= "0" or secim >= "7":
        break
    elif secim == '1':
        sayi1 = float(input("İlk sayıyı girin: "))
        sayi2 = float(input("İkinci sayıyı girin: "))        
        print(sayi1,"+",sayi2,"=", topla(sayi1,sayi2))

    elif secim == '2':
        sayi1 = float(input("İlk sayıyı girin: "))
        sayi2 = float(input("İkinci sayıyı girin: "))
        print(sayi1,"-",sayi2,"=", cikar(sayi1,sayi2))

    elif secim == '3':
        sayi1 = float(input("İlk sayıyı girin: "))
        sayi2 = float(input("İkinci sayıyı girin: "))
        print(sayi1,"*",sayi2,"=", carp(sayi1,sayi2))

    elif secim == '4':
        sayi1 = float(input("İlk sayıyı girin: "))
        sayi2 = float(input("İkinci sayıyı girin: "))
        if sayi1 == 0 or sayi2 == 0:
            print("Bir sayı sıfıra bölünemez.")
        else:
            print(sayi1,"/",sayi2,"=", bol(sayi1,sayi2))
    elif secim == '5':
        sayi1 = float(input("Karesi alınacak sayıyı girin: "))
        sayi2 = float(input("Üst sayısını girin: "))
        print(sayi1,"**",sayi2,"=", usAlma(sayi1,sayi2))            
    elif secim == '6':
        sayi1 = float(input("Modu alınacak sayıyı girin: "))
        sayi2 = float(input("Kaça bölüneceğini girin: "))
        print(sayi1,"%",sayi2,"=", modAlma(sayi1,sayi2))
    else:
        print("Geçersiz seçim.")

