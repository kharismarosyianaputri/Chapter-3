#Memasukkan nilai
bhsindo = int(input("Masukkan nilai Bhs Indonesia : "))
ipa = int(input("Masukkan nilai Ipa :"))
mtk = int(input("Masukkan nilai Matematika :"))

if(bhsindo >= 60) and (ipa >= 60) and (mtk > 70): 
          print("LULUS")
else:
          print("TIDAK LULUS")
