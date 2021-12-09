dataFile = open('bukuperpustakaan.txt', 'a')

from datetime import *

x    = datetime.date(datetime.now())
skrg = str(str(x.year) + '-' + str(x.month) + '-' + str(x.day))
y    = str(x + timedelta(days=7))
       
while True:
    kode  = input('Masukkan Kode Member: ')
    nama  = input('Masukkan Nama Member: ')
    judul = input('Masukkan Judul Buku:  ')

    myString = kode+'|'+nama+'|'+judul+'|'+skrg+'|'+y+'\n'
    dataFile.write(myString)

    ulang = input('Ulangi lagi (y/n): ')
    if ulang == 'n':
        break
        
dataFile.close()

