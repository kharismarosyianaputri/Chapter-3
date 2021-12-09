dataFile = open('bukuperpustakaan.txt', 'r')

kode  = []
nama  = []
judul = []
awal  = []
maks  = []

for pin in dataFile:
    spltpin = pin.split('|')
    kode.append(spltpin[0])
    nama.append(spltpin[1])
    judul.append(spltpin[2])
    awal.append(spltpin[3])
    maks.append(spltpin[4].strip())   

while True:
    cari = input('Masukkan Kode Member: ')
    print('')
    if cari in kode:
        data = True
        import datetime

        a = kode.index(cari)
        skrg = datetime.datetime.now()
        from datetime import datetime

        b = maks[a]
        c = datetime.strptime(b, '%Y-%m-%d')
        hasil = c - skrg
        akhir = datetime.date(skrg)
        batas = datetime.date(c)

        if data:
            d = batas - akhir
            batas = d.days
            denda = 0
            if batas <= 0:
                bayar = 0
            elif batas >= 0:
                bayar = 2000 * int(batas)
                denda += bayar
                
                print('Data Peminjaman Buku')
                print('Kode Member             : ', kode[a])
                print('Nama Member             : ', nama[a])
                print('Judul Buku              : ', judul[a])
                print('Tanggal Mulai Peminjaman: ', awal[a])
                print('Tanggal Maks Peminjaman : ', maks[a])
                print('Tanggal Pengembalian    : ', akhir)
                print('Terlambat               : ', batas, 'hari')
                print('Denda                   : ', 'Rp.', denda)
                break

       
        



