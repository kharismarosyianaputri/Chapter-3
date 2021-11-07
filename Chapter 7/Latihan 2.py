try:
    NamaFile = input('Masukkan nama file: ')
    while True:
        file = open(NamaFile, 'a')
        data = input('Data yang mau ditambahkan: ')
        file.write(data)
        file.close()
        lagi = input('Mau lagi (y/n) : ')
        if lagi == 'n':
           break
except FileNotFoundError:
    print('File tidak ditemukan')
        
