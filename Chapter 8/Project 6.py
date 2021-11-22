def sortStringByChar(myData):
    myData.sort(reverse=True, key=len)
    return(myData)

def getlistnamaBuah():
    loop = 0
    data = []
    while loop < 3:
        namabuah = (input("Masukkan nama buah:"))
        data.append(namabuah)
        loop += 1

    return data

datalist = getlistnamaBuah()

if(datalist):
    print("hasil dari list :", datalist)
    result = sortStringByChar(datalist)
    print(result)
