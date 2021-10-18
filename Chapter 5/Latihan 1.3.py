#Memasukkan nilai

bhsindo = int(input("Masukkan nilai Bhs Indonesia : "))
ipa = int(input("Masukkan nilai Ipa :"))
mtk = int(input("Masukkan nilai Matematika :"))

if(bhsindo >= 0) and (bhsindo <= 100) and (ipa >= 0) and (ipa <= 100) and (mtk >= 0) and (mtk <= 100):
    if(bhsindo >= 60) and (ipa >= 60) and (mtk > 70):
        print("LULUS")
    else:
        sebab = ""
        if(bhsindo < 60):
            sebab += "- Nilai Bhs Indonesia kurang dari 60"
        if(ipa < 60):
            sebab += "- Nilai IPA kurang dari 60"
        if(mtk < 70):
            sebab += "- Nilai Matematika kurang dari 70"
        print("TIDAK LULUS")
        print("Sebab : ")
        print(sebab)
    
else: print("Maaf input ada yang tidak valid")
