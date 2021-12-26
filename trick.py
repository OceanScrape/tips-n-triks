# Menbuat banyak variabel
a, b, c = 1, 2, 'aku'
print(a, b, c)

# Mengetahui tipe data
a = 'saya'
b = 123
print(type())

# Menukar variabel
a, b = 1, 2
a, b = b, a
print(a, b)

# slicing dari belakang
kalimat = 'saya sedang membaca'
print(kalimat[::-1]) # acabmem gnades ayas

# Memisahakan komponen yg ada pada string menjadi sebuah list yg dipisahkan menggukanan separator tertentu
data = 'saya%20sedang%20membaca'
daftar = data.split('%20')
print(daftar) # ['saya', 'sedang', 'membaca']

# ubah dari list menjadi string
daftar = ['saya', 'sedang', 'membaca']
kalimat = ' '.join(daftar)
print(kalimat) # saya sedang membaca

# menghitung banyaknya elemen dari suatu list
daftar = [1, 2, 5, 3, 4, 5, 2, 4, 7, 8, 5, 1, 4, 5, 7, 8, 0, 9, 7, 2, 4, 5]
print(daftar.count(3))
#
# menghitung elemen secara bersamaan
from collections import Counter
print(Counter(daftar)) # Counter({5: 5, 4: 4, 2: 3, 7: 3, 1: 2, 8: 2, 3: 1, 0: 1, 9: 1})

# huruf
nama = 'budi'
nama2 = 'BUDI'
print(nama.upper()) # BUDI
print(nama.capitalize()) # Budi
print(nama2.lower()) # budi

# Mengubah seluruh elemen dari suatu list
lisku = ['aku', 'seorang', 'kapiten']
lisbaru = map(str.capitalize, lisku)
print(list(lisbaru)) # ['Aku', 'Seorang', 'Kapiten']

# looping menggunakan list comprehensif
mylist = [x for x in range(1, 11)]
# pengembangan
lisku = ['data ke ' + str(x) for x in range(1, 11)]

# cara lama
lisku = ['aku', 'seorang', 'kapiten', 'mempunyai', 'pedang', 'panjang']
list_baru = []
for i in lisku:
    data = i
    list_baru.append(data)
print(list_baru)

# cara baru
new_lsit = list(map(lambda x: x, lisku))
print(new_lsit)
