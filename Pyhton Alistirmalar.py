
# UYGULAMA

string1 = 'hello i am merve and i am learning pyhton'

len(string1)
range(len(string1))

def alternating (string):
    new_str= ''
    for index in range(len(string)) :
        if index  % 2 == 0:
            new_str += string[index].upper()
        else:
            new_str += string[index].lower()
    print(new_str)

alternating(string1)


# KOSULLAR VE DONGULER

# ORNEK 1

students = ['Denisa', 'Merve', 'Sinan', 'Osman']

[student[0].upper() if len(student) % 2 != 0 else student[0].lower() for student in students]

# Out[8]: ['d', 'M', 'S', 'O']

# ORNEK 2

string1= 'abracadabra'
group = []
for index, letter in enumerate(string1, 1):
    if index * 2 % 2 == 0:
        group.append(letter)

# ORNEK 3

city_name= ['Berlin', 'London', 'Paris']

def plate(cities):
    for index, cities in enumerate(cities, 1):
        print(f'{index}: {cities}')

plate(city_name)

# COMPREHENSIONS

#ORNEK

dictn= {'Denise': 10, 'Merve': 20}
new_dict= { k: v * 2 for (k, v) in dictn.items() }
new_dict

####################################### PYHTON ALISTIRMALAR #######################################

x=8
y=3.2
z= 8j+ 18
a= 'hello'
b= True
c= 23 < 22
d= {'Name': 'Jack',
    'Age': 27 }
t= ( 'Machine Learning', 'Data Science')
s= {'Machine Learning', 'Data Science'}

type(x)
type(y)
type(z)
type(a)
type(b)
type(c)
type(d)
type(t)
type(s)



######  GOREV2 ######:



# Verilen string ifadenin tüm harflerini büyük harfe çeviriniz. Virgül ve nokta yerine space koyunuz, kelime kelime ayırınız.
# 'the goal is to turn data into information, and information into insight.'

string1= 'the goal is to turn data into information, and information into insight.'

string1.replace(',' , ' ')
string1.replace('.' , ' ')
string2 = string1.upper().split()

print(string2)


string3 = [' ' if ',' and '.' in letter else letter.upper() for letter in string1.split()]
print(string3)



######  GOREV3 ######:




# Verilen listeye aşağıdaki adımları uygulayınız.

liste= ['D', 'A', 'T', 'A', 'S', 'C', 'I', 'E', 'N', 'C', 'E']

# Adım1: Verilen listenin eleman sayısına bakınız.

len(liste)

# Adım2: Sıfırıncı ve onuncu indeksteki elemanları çağırınız.

liste[0]
liste[10]

# Adım3: Verilen liste üzerinden ["D", "A", "T", "A"] listesi oluşturunuz.

liste[: 4]

# Adım4: Sekizinci indeksteki elemanı siliniz.

liste.pop(8)
del liste[8]

#remove kullanilirsa direk ciarilmak istenen de yazilabilir.


# Adım5: Yeni bir eleman ekleyiniz.

liste.append('M')

#extend ile listeye tuple vs eklenebilir. ARASTIR


# Adım6: Sekizinci indekse"N" elemanını tekrar ekleyiniz.

liste.insert(8, 'N')



######  GOREV4 ######:



#Verilensözlükyapısınaaşağıdakiadımlarıuygulayınız.

dict= {'Cristian': ['America', 18],
       'Daisy': ['England', 12],
       'Antonio': ['Spain', 22],
       'Dante': ['Italian', 25],}


#Adım1: Key değerlerine erişiniz.

dict.keys()

#Adım2: Value'lara erişiniz.

dict.values()

#Adım3: Daisy key'ine ait 12 değerini 13 olarak güncelleyiniz.'

dict['Daisy']= ['England', 13]

#Adım4: Key değeri Ahmet value değeri [Turkey,24] olan yeni bir değer ekleyiniz.

dict.update({'Ahmet': ['Turkey',24] })
dict.update({'merve': ['Turkey',24] })
dict.update({'merve': ['Turkey',28] })

#Adım5: Antonio'yu dictionary'den siliniz.

del dict['Antonio']
dict.pop('Antonio')


######  GOREV5 ######:




# Argüman olarak bir liste alan, listenin içerisindeki tek ve çift sayıları ayrı listelere atayan ve bu listeleri return eden fonksiyon yazınız.

l=[2, 13, 18, 93, 22]

def liste_fonk(liste):
    l1 = [[], []]
    for i in liste:
        if i % 2 == 0:
            l1[0].append(i)
        else:
            l1[1].append(i)
    return l1


liste_fonk(l)



######  GOREV 6 ######:



# Aşağıda verilen listede mühendislik ve tıp fakülterinde dereceye giren öğrencilerin isimleri bulunmaktadır.
# Sırasıyla ilk üç öğrenci mühendislik fakültesinin başarı sırasını temsil ederken son üç öğrencide tıp fakültesi öğrenci sırasına aittir.
# Enumarate kullanarak öğrenci derecelerini fakülte özelinde yazdırınız.

ogrenciler= ['Ali', 'Veli', 'Ayse', 'Talat', 'Zeynep', 'Ece' ]

# def ayirma (grup):
#     muh_fak = []
#     tip_fak = []
#     for index, ogrenci in enumerate(grup, 1):
#         if index < 4 :
#             muh_fak.append(ogrenci)
#         else:
#             tip_fak.append(ogrenci)
#         print(list(enumerate(muh_fak, 1)))
#         print(list(enumerate(tip_fak, 1)))
#
# ayirma(ogrenciler)
#
# def son (grup):
#     for index, ogrenci in enumerate(grup, 1):
#         if index < 4 :
#             print(f"Muhendislik fakultesi {index}. ogrenci: {ogrenci}")
#         else:
#             print(f"Tip fakultesi {index}. ogrenci: {ogrenci}")
#
# son(ogrenciler)



# [ print(f"Mühendislik Fakültesi {index+1} . öğrenci: {student}") if index < 3
#   else print(f"Tıp Fakültesi {index-2} . öğrenci: {student}")
#   for index, student in enumerate(ogrenciler)]

#

ogrenciler = ["Ali","Veli","Ayşe","Talat","Zeynep","Ece"]
for i,x in enumerate(ogrenciler):
    if i<3:
        i += 1
        print("Mühendislik Fakültesi", i, ". öğrenci: ", x)
    else:
        i -= 2
        print("Tıp Fakültesi", i, ". öğrenci: ", x)

#

ogrenciler = dict(enumerate(ogrenciler))
a = 0
for x in range(len(ogrenciler)):
    if x < 3:
        ogrenciler[f"Muhendislik Fakultesi {x+1}. ogrenci: "] = ogrenciler.pop(x)
        a += 1
    else:
        ogrenciler[f"Tip Fakultesi {x + 1 - a}. ogrenci: "] = ogrenciler.pop(x)
print(ogrenciler, sep='\n')

#

for index, derece in enumerate(ogrenciler, 1):
    if index < 4:
    print("Mühendislik Fakültesi {} . öğrenci: {}".format(index,derece))
    if index >= 4 :
    print("Tıp Fakültesi {} . öğrenci: {}".format(index -3, derece))






######  GOREV 7 ######:



# Aşağıda 3 adet liste verilmiştir.
# Listelerde sırası ile bir dersin kodu, kredisi ve kontenjan bilgileri yer almaktadır.
# Zip kullanarak ders bilgilerini bastırınız.


ders_kodu = ["CMP1005", "PSY1001","HUK1005","SEN2204"]
kredi = [3,4,2,4]
kontenjan = [30,75,150,25]

# new_list=zip(ders_kodu, kredi, kontenjan)
# for x, y, z in new_list:
#     print("Kredisi  {} olan {} kodlu dersin kontenjani {} kisidir.".format(y, x, z))


# Yasemin Hoca Cozumu

t = list(zip(ders_kodu, kredi, kontenjan))
print(t)

for i in range(len(t[0])+1):
    print(f" Kredisi {kredi[i]} olan {kredi[i]} kodlu dersin kontenjani {kontenjan[i]} kisidir. ")




######  GOREV 8 ######:


#Aşağıda 2 adet set verilmiştir.
#Sizden istenilen eğer 1. küme 2. kümeyi kapsiyor ise ortak elemanlarını eğer kapsamıyor ise 2. kümenin 1. kümeden farkını yazdıracak fonksiyonu tanımlamanız beklenmektedir
#Beklenen Çıktı: Kapsayıp kapsamadığını kontrol etmek için issuperset() metodunu, farklı ve ortak elemanlar için ise intersection ve difference metodlarını kullanınız.

kume1= set(['data', 'pyhton'])
kume2= set(['data', 'pyhton', 'qcut', 'lambda', 'function', 'miuul'])

kume3= print(kume1.intersection(kume2)) if kume1.issuperset(kume2) else print(kume2.difference(kume1))

