print ("Hai.. nama saya Mr.Harry, Saya akan memilih sebuah bilangan bulat secara acak antara 0 s/d 100")
print ("Silakan ditebak ya...")
       
from random import randint
bil = randint (0,100)

while True:
    tebakan = int(input('Tebakan Anda: '))
    if tebakan < bil:
        print('Bilangan Tebakan Anda Terlalu Kecil')
    elif tebakan > bil:
        print('Bilangan Tebakan Anda Terlalu Besar')
    elif tebakan == bil:
        print('Yeeey... Tebakan Anda Benar')
        break
print ('Terimakasih Telah Bermain')
