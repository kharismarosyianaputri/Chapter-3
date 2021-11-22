#9
myString = "python adalah bahasa pemrograman yang menyenangkan"
print(myString)

#10
myString = ("python adalah bahasa pemrograman yang menyenangkan")
hurufPenyusun = set(myString)
print(hurufPenyusun)

#11
myString = list(hurufPenyusun)
myString.sort()
print("himpunan karakter huruf yang diperoleh : ", myString)
