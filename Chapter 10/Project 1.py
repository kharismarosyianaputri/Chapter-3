file = open("databilangan.txt", "r")

genap = 0
ganjil = 0

for i in file:
    if int(i)%2==0:
        genap += 1     
    elif int(i)%2==1:
        ganjil += 1
        
print("Banyak bilangan genap:", genap)
print("Banyak bilangan ganjil:", ganjil)

file.close()
