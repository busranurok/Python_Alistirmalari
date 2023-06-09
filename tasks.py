###############################################
# Python Alıştırmalar
###############################################

###############################################
# GÖREV 1: Verilen değerlerin veri yapılarının tipleriniz inceleyiniz.
###############################################

x = 8
print(type(x))
print("\n")

y = 3.2
print(type(y))
print("\n")

z = 8j + 18
print(type(z))
print("\n")

a = "Hello World"
print(type(a))
print("\n")

b = True
print(type(b))
print("\n")

c = 23 < 22
print(type(c))
print("\n")

"""
 Sıralıdır
 Kapsayıcıdır
 Değiştirilebilir
"""
l = [1, 2, 3, 4]
print(type(l))
print("\n")

"""
 Değiştirilebilir
 Kapsayıcı
 Sırasız
 Key değerleri farklı olacak
"""
d = {"Name": "Büşra Nur",
     "Age": [38, 56],
     "Address": "Türkiye"}
print(type(d))
print("\n")

"""
 Değiştirilemez
 Kapsayıcı
 Sıralı
"""
t = ("Macnine Learning", "Data Science")
print(type(t))
print("\n")

"""
 Değiştirilebilir
 Sırasız + Eşsiz
 Kapsayıcı
"""
s = {"Python", "Machine Learning", "Data Science"}
print(type(s))
print("\n")

###############################################
# GÖREV 2: Verilen string ifadenin tüm harflerini büyük harfe çeviriniz. Virgül ve nokta yerine space koyunuz,
# kelime kelime ayırınız.
###############################################
#Yöntem 1
text = "The goal is to turn data into information, and information into insight."
print(text.upper().replace(",", " ").replace(".", " ").split())
print("\n")

#Yöntem 2
text = "The goal is to turn data ,into information, end information into insgiht."
text = text.replace(",", " ")
text = text.replace(".", " ")
text = text.split()
print(text)
print("\n")
print(text[0])
print("\n")

text2 = []

for index in range(len(text)):
    text2.append(text[index].upper())

print(text2)
print("\n")

###############################################
# GÖREV 3: Verilen liste için aşağıdaki görevleri yapınız.
###############################################

lst = ["D","A","T","A","S","C","I","E","N","C","E"]

# Adım 1: Verilen listenin eleman sayısına bakın.
print(len(lst))
print("\n")

# Adım 2: Sıfırıncı ve onuncu index'teki elemanları çağırın.
print(lst[0])
print("\n")
print(lst[10])
print("\n")

# Adım 3: Verilen liste üzerinden ["D","A","T","A"] listesi oluşturun.
#Çözüm 1
new_list = []
for index in range(len(lst)):
     if index < 4:
          new_list.append(lst[index])
print(new_list)
print("\n")

#Çözüm 2:
new_list = lst[0:4]
print(new_list)
print("\n")

# Adım 4: Sekizinci index'teki elemanı silin.
print(lst.pop(8))
print("\n")
print(lst)
print("\n")

# Adım 5: Yeni bir eleman ekleyin.
print(lst.append("HBO"))
print("\n")
print(lst)
print("\n")

# Adım 6: Sekizinci index'e  "N" elemanını tekrar ekleyin.
print(lst.insert(8, "N"))
print("\n")
print(lst)
print("\n")

###############################################
# GÖREV 4: Verilen sözlük yapısına aşağıdaki adımları uygulayınız.
###############################################

dict = {'Christian': ["America",18],
        'Daisy':["England",12],
        'Antonio':["Spain",22],
        'Dante':["Italy",25]}


# Adım 1: Key değerlerine erişiniz.
print(dict.keys())
print("\n")

# Adım 2: Value'lara erişiniz.
print(dict.values())
print("\n")

# Adım 3: Daisy key'ine ait 12 değerini 13 olarak güncelleyiniz.
#Yöntem 1
dict.update({"Daisy": ["England", 13]})
print(dict)
print("\n")

#Yöntem 2
dict["Daisy"][1] = 14
print(dict["Daisy"][1])
print("\n")

# Adım 4: Key değeri Ahmet value değeri [Turkey,24] olan yeni bir değer ekleyiniz.
dict.update({"Ahmet": ["Turkey", 24]})
print(dict)
print("\n")

# Adım 5: Antonio'yu dictionary'den siliniz.
dict.pop("Antonio")
print(dict)
print("\n")

###############################################
# GÖREV 5: Arguman olarak bir liste alan, listenin içerisindeki tek ve çift sayıları
# ayrı listelere atıyan ve bu listeleri return eden fonskiyon yazınız.
###############################################
l = [2,13,18,93,22]

#Yöntem 1
def tek_cift_bul(l):
    tek_list = []
    cift_list = []
    for index in l:
        if index % 2 == 0:
           cift_list.append(index)
        else:
            tek_list.append(index)

    return cift_list, tek_list

c, t = tek_cift_bul(l)
print(c)
print("\n")
print(t)
print("\n")

#Yöntem 2 (List Comprehension ile)
cift = [c for index in l if index % 2 == 0 ]
print(cift)
print("\n")
tek = [t for index in l if index % 2 != 0]
print(tek)
print("\n")

# Yöntem 3 (Enumerate ile)
def tek_cift_bul(l):
    cift= []
    tek = []
    for index, number in enumerate(l):
        if number % 2 == 0:
            cift.append(l[index])
        else:
            tek.append(l[index])
    return cift, tek

cift, tek = tek_cift_bul(l)
print(cift)
print("\n")
print(tek)
print("\n")

###############################################
# GÖREV 6: Aşağıda verilen listede mühendislik ve tıp fakülterinde dereceye giren öğrencilerin isimleri bulunmaktadır.
# Sırasıyla ilk üç öğrenci mühendislik fakültesinin başarı sırasını temsil ederken son üç öğrenci de tıp fakültesi öğrenci sırasına aittir.
# Enumarate kullanarak öğrenci derecelerini fakülte özelinde yazdırınız.
###############################################
"""
Beklenen Çıktı: Mühendislik Fakültesi 1. öğrenci: Ali
          Mühendislik Fakültesi 2. öğrenci: Veli
          Mühendislik Fakültesi 3. öğrenci: Ayşe
          Tıp Fakültesi 1. öğrenci: Talat
          Tıp Fakültesi 2. öğrenci: Zeynep
          Tıp Fakültesi 3. öğrenci: Ece
"""

ogrenciler = ["Ali","Veli","Ayşe","Talat","Zeynep","Ece"]

#Yöntem 1
for index, ogrenci in enumerate(ogrenciler, 1):
    if index < 4:
        print(f"Mühendislik Fakültesi {index}. öğrenci: {ogrenci}")
    else:
        print(f"Tıp Fakültesi {index-3}. öğrenci: {ogrenci}")

#Yöntem2
for i, x in enumerate(ogrenciler):
    if i<3:
        i += 1
        print("Mühendislik Fakültesi", i, ". öğrenci: ", x)
    else:
        i -= 2
        print("Tıp Fakültesi", i, ". öğrenci: ", x)


###############################################
# GÖREV 7: Aşağıda 3 adet liste verilmiştir.
# Listelerde sırası ile bir dersin kodu, kredisi ve kontenjan bilgileri yer almaktadır.
# Zip kullanarak ders bilgilerini bastırınız.
"""Beklenen Çıktı: Kredisi 3 olan CMP1005 kodlu dersin kontenjanı 30 kişidir.
                Kredisi 4 olan PSY1001 kodlu dersin kontenjanı 75 kişidir.
                Kredisi 2 olan HUK1005 kodlu dersin kontenjanı 150 kişidir.
                Kredisi 4 olan SEN2204 kodlu dersin kontenjanı 25 kişidir."""

ders_kodu = ["CMP1005","PSY1001","HUK1005","SEN2204"]
kredi = [3,4,2,4]
kontenjan = [30,75,150,25]

#Yöntem 1
new_list = list(zip(kredi, ders_kodu, kontenjan))
print(new_list)
print(new_list[0])
print(new_list[0][0])

for index, tuple in enumerate(new_list):
    print(f"Kredisi {tuple[0]} olan {tuple[1]} kodlu dersin kontenjanı {tuple[2]} kişidir.")

#Yöntem 2
for ders_kodu, kredi, kontenjan in zip(ders_kodu, kredi, kontenjan):
  print(f"Kredisi {kredi} olan {ders_kodu} kodlu dersin kontenjanı {kontenjan} kişidir.")


###############################################
# GÖREV 8: Aşağıda 2 adet set verilmiştir.
# Sizden istenilen eğer 1. küme 2. kümeyi kapsiyor ise ortak elemanlarını eğer kapsamıyor ise 2. kümenin 1. kümeden farkını yazdıracak fonksiyonu tanımlamanız beklenmektedir.
###############################################
"""
Beklenen çıktı:
{"function", "qcut", "miuul", "lambda"}
"""
kume1 = set(["data", "python"])
kume2 = set(["data", "function", "qcut", "lambda", "python", "miuul"])

def kume(set1,set2):
    if set1.issuperset(set2):
        print(set1.intersection(set2))
    else:
        print(set2.difference(set1))

kume(kume1,kume2)



