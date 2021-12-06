dataFile = open("datamahasiswa.txt", "r")

data = dataFile.readlines()

dataList = []
for i in range(len(data)):
    pecahData = data[i].replace("\n", "")
    pecahData2 = pecahData.split("|")
    dataDict = {"nim": pecahData2[0], "nama": pecahData2[1], "alamat": pecahData2[2]}
    dataList.append(dataDict)
    
print(dataList)
dataFile.close()
    
    
    
    
