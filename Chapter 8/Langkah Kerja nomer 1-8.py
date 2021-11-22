#1
a = [1, 5, 6, 3, 6, 9, 11, 20, 12]
b = [7, 4, 5, 6, 7, 1, 12, 5, 9]

#2
a.insert(3, 10)
b.insert(2, 15)

#3
a.append(4)
b.append(8)

#4
a.sort()
print(a)
b.sort()
print(b)

#5
c = list(a[0:8])
print(c)
d = list(b[2:10])
print(d)

#6
for x in c and d:
    i = 0
    e = []
    while(i <= 7):
        x = (c[i] + d[i])
        e.append(x)
        i = i + 1

#7
myTuple = tuple(e)
print(myTuple)

#8
print('Nilai minimum dari elemen e', min(e))
print('Nilai maksimum dari elemen e', max(e))
print('Nilai jumlahan seluruh elemen dari e', sum(e))









