try:
    NamaFile = input('Masukkan nama file: ')
    file = open('d:/anyfiles.txt', 'r')
    print('isi file d:/anyfiles.txt', 'adalah: ')
    print(file.read())
except FileNotFoundError:
    print('File tidak ditemukan')
    
    
    
 
