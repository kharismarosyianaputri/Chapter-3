n = int(input("Berapa banyak bilangan yang ingin diinput?: "))  
i = 1
x = []
while(i <= n):
    bil_bulat = int(input('Masukkan bilangan bulat:'))
    x.append(bil_bulat)
    i = i + 1
x.sort(reverse = True)
print("Bilangan bulat dari besar ke kecil adalah: ", x)
    
    
