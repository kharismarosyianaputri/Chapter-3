n = int(input("Berapa banyak nama yang ingin diinput?: "))  
i = 1
name= []
while (i <= n):
    inputnamamahasiswa = input("Nama mahasiswa :")
    name.append(inputnamamahasiswa)
    i = i + 1

name.sort()
for inputnamamahasiswa in name:
    print("{0} ({1} karakter)".format(
        inputnamamahasiswa, len(tuple(inputnamamahasiswa))))


