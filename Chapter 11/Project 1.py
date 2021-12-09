from datetime import *

def diffDate(x):
    skrg    = datetime.now()
    tglskrg = str(skrg.year)+ '-' + str(skrg.month) + '-' + str(skrg.day)
    tgl     = datetime.strptime(str(tglskrg), '%Y-%m-%d')
    date    = datetime.strptime(str(x), '%Y-%m-%d')
    selisih = date-tgl
    return selisih.days

print(diffDate('2021-12-13'))


 


      
