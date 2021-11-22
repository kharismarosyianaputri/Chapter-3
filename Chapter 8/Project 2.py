def dataStat(x):
    if(isinstance(x, list)):
       tupleX  = tuple(x)
       a  = sum(tupleX) / len(tupleX)
       b  = max(tupleX) 
       c  = min(tupleX)

       return [a, b, c]
      
def getListFromUser():
    try:
        inputData = int(input('Banyak angka yang ingin dimasukkan '))
        jum = 0
        data = []
        while jum < inputData:
            bilangan = int(input("Masukkan bilangan bulat ke-{0} : ".format(jum+1)))
            data.append(bilangan)
            jum += 1
        return data
    
    except ValueError:
        print('Data yang anda masukkan salah')
        return False
       
dataList = getListFromUser()
if(dataList):
    result   = dataStat(dataList)
    print("Nilai rata-rata dari list bilangan {0}        : {1}".format(dataList,result[0]))
    print("Nilai tertinggi dari list {0}  : {1}".format(dataList,result[1]))
    print("Nilai terendah dari list {0}   : {1}".format(dataList,result[2]))
