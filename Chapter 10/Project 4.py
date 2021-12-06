dataFile = open("datamahasiswa.txt", "r")
data = dataFile.readlines()

nim = input("Masukkan NIM yang mau dicari:")

for i in range(len(data)):
    readFile = data[i].split("|")
    if nim == readFile[0]:
        keterangan = "Data mahasiswa ditemukan"
        print("Data Mahasiswa")
        print("NIM     :", readFile[0])
        print("Nama    :", readFile[1])
        print("Alamat  :", readFile[2])
        break
    else:
        keterangan = "Data mahasiswa tidak ditemukan"
        
if keterangan == "Data mahasiswa tidak ditemukan":
    print("Data mahasiswa tidak ditemukan")

dataFile.close()



