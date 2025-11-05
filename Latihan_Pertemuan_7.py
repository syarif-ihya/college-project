# ------Quiz 1-----
# Isilah tiga baian code ayng kosong:
print("---------------Quiz 1---------------")
buah = ["apel", "anggur", "mangga", "jeruk", "melon"]
for x in buah:
    print(x)
    


# ------Quiz 2------
# lopping dimana ketika nilai x = 5 maka program langung ke iterasi berikutnya
print("\n---------------Quiz 2---------------")
x = 0
while x < 10:
    x += 1
    if x == 5:
        continue
    print(x)


# ------Studi Kasus------
# Leni ingin sekali mengetahui deret angka dari 1 sampai 50 dimana ketika bertemu dengan kelipatan 5 maka outputnya adalah "pass". Tolong bantu Leni dengan masalahnya kali ini.
print("\n---------------Studi Kasus---------------")
for i in range(1,51):   
    if i % 5 == 0:
        print("pass", end=",")
        continue
    print(i, end=",")