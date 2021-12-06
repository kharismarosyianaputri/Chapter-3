dataFile = open("datamahasiswa.txt", "a")
        
while True:
    nim = input("Masukkan NIM :")
    nama = input("Masukkan Nama Mhs :")
    alamat = input("Masukkan Alamat :")

    myString = nim+"|"+nama+"|"+alamat+"\n"
           
    dataFile.write(myString)
    
    ulang = input('Ulangi input lagi (y/n) : ')
    if ulang == 'n':
            break
        
dataFile.close()

