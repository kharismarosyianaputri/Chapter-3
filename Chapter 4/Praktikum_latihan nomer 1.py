#tarif sewa rental mobil

#untuk12jampertama
tarifawal = 200000 
#tarifperjam
tarifselanjutnya = 10000

#waktu
waktupeminjaman = 06.00
waktupengembalian = 23.50

#menghitung lama waktu sewa
lamawaktusewa = int (waktupengembalian-waktupeminjaman)
#menghitung lama waktu sewa selanjutnya
lamasewaselanjutnya = lamawaktusewa - 12
#menghitung tarif sewa selanjutnya
tarifsewaselanjutnya = lamasewaselanjutnya * tarifselanjutnya
totaltarif = tarifawal + tarifsewaselanjutnya
print(totaltarif)



