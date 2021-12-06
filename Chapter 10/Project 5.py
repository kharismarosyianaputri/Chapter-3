myfile = open("bilangan.txt", "r")
filetujuan = open("filetujuan.txt", "a")

baca = myfile.readlines()

for i in range(len(baca)):
    replace = baca[i].replace("\n", "") 
    angka = replace.split("|")
    print(str(int(angka[0]) + int(angka[1].rstrip("\n"))))
    filetujuan.write(str(int(angka[0]) + int(angka[1]))+"\n")

myfile.close()
filetujuan.close()
