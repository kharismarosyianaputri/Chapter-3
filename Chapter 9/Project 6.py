nilai = [{'nim' : 'A01', 'nama' : 'Agustina', 'mid' : 50, 'uas' : 80}, 
 	 {'nim' : 'A02', 'nama' : 'Budi',     'mid' : 40, 'uas' : 90}, 
         {'nim' : 'A03', 'nama' : 'Chicha',   'mid' : 100,'uas' : 50}, 
         {'nim' : 'A04', 'nama' : 'Donna',    'mid' : 20, 'uas' : 100}, 
	 {'nim' : 'A05', 'nama' : 'Fatimah',  'mid' : 70, 'uas' : 100}]

print("==================================================================")
print("NIM       NAMA        N.MID      N.UAS      N.AKHIR      STATUS   ")
print("------------------------------------------------------------------")

for i in range(len(nilai)):
     nilaiakhir = (nilai[i]["mid"] + 2* nilai[i]["uas"])/3
     nilaiakhir = round(nilaiakhir)
     if nilaiakhir >= 60:
         statuskelulusan = "LULUS"
     else:
         statuskelulusan = "TIDAK LULUS"
     print(nilai[i]["nim"].ljust(10), end="")
     print(nilai[i]["nama"].ljust(9), end="")
     print(str(nilai[i]["mid"]).rjust(8), end="")
     print(str(nilai[i]["uas"]).rjust(11), end="")
     print(str(nilaiakhir).rjust(13), end="")
     print(statuskelulusan.rjust(12))

print("------------------------------------------------------------------")

