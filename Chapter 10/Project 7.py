myFile = open("teksasli.txt", "a")
teksSandi = "UCAC UWMC RAVJQP VCRK MCFCPI VKFCM RCJCO"
print(teksSandi)
i = 0
geser = int(input("Masukkan berapa banyak pergeseran sandi: "))
for i in range(len(teksSandi)):
    t = teksSandi[i]
    x = ord(t)
    if x==32:
        print(chr(x), end='')
    elif x+geser>90:
        print(chr(91+((x+geser)-65)), end='')
    elif x!=32:
        x+=int(geser)
        y = chr(x)
        print(y, end='')
    i+=1
    myFile.write(y)

myFile.close()
