mhs = ['K001:ROSIHAN ARI           :1979-09-01:SOLO', 
       'K002:DWI AMALIA FITRIANI   :1979-09-17:KUDUS',
       'K003:FAZA FAUZAN           :2005-01-28:KARANGANYAR']

print("===============================================================")
print("NIM         NAMA MAHASISWA        TGL LAHIR        TEMPAT LAHIR")
print("---------------------------------------------------------------")

for data in mhs:
    datalist     = data.split(":")
    nim          = datalist[0]
    nama         = datalist[1]
    tgl_lahir    = datalist[2].split("-")
    tgl_lahir.reverse()
    tgl_lahir    = "/".join(tgl_lahir)
    tempat_lahir = datalist[3]
    
    print(nim.ljust(12), end="")
    print(nama.ljust(14), end="")
    print(str(tgl_lahir).ljust(17), end="")
    print(tempat_lahir.ljust(20))

print("---------------------------------------------------------------")
