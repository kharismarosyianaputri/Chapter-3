buah = {'apel': 5000,
        'jeruk': 8500,
        'mangga': 7800,
        'duku': 6500}
def harga_max(buah):
    inverse = [(value, key) for key, value in buah.items()]
    x = (max(inverse)[1])
    return x
print("Nama buah yang harga satuannya paling mahal adalah: ", harga_max(buah))

