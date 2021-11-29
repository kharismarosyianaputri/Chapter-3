import random

def shuffleString(x,n):
    listkata = []
    while True:
        if(len(listkata) <= n-1):
            kata = list(x)
            acakkata = random.sample(kata,len(kata))
            acakkata = ''.join(acakkata)
            if acakkata not in listkata:
                listkata.append(acakkata)
        else:
            print(f"randomString({x},{n}) ->", listkata)
            break
 
teks = str(input("Masukkan kata : "))
jumlah = int(input("Masukkan angka : "))
shuffleString(teks,jumlah)



