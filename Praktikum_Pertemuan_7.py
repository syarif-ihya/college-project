# Looping 
for i in range(5):
    print("(1) Perulangan ke-", i)
for i in range(3,8):
    print("(2) Perulangan ke-", i)
for i in range(3,15,3):
    print("(3) Perulangan ke-", i)

# While
count = 0   
while count < 5:
    print("(4) Perulangan ke-", count)
    count += 1 
while count < 10:
    print("(5) Perulangan ke-", count)
    count += 1
    if count == 7:
        break
while count < 15:
    count += 1
    if count % 2 == 0:
        continue
    print("(6) Perulangan ke-", count)

# For with Continue
string="teteh"
for i in string:
    if i == "t":
        continue
    print(i)

# Nested Loop
for i in range(1,6):
    for j in range(i):
        print("*", end="")
    print()

# Nested While
baris =0
bintang =0
while baris<10:
    if (bintang >= baris):
        print(".")
        baris += 1
        bintang = 0
        continue
    print("*",end="")
    bintang += 1
else: 
    print("berhenti")

# Looping di List
daftar = [1, 2, 3, 4, 5]
for i in daftar:
    print("(List) Perulangan ke-", i)

# looping di Tuple
tuple_data = (1, 2, 3, 4, 5)
for i in tuple_data:
    print("(Tuple) Perulangan ke-", i)

# loooping di Set
set_data = {1, 2, 3, 4, 5}
for i in set_data:
    print("(Set) Perulangan ke-", i)

# looping di Dictionary
dict_data = {
    "nama": "Syarif",
    "umur": 20,
    "asal": "Bandung",
    "male": False,
    "hobi": ["membaca", "menulis", "bermain"]
}
for i in dict_data:
    print("(Dictionary) Data", i, "=", dict_data[i])


kucing = {
    "nama": "Luka",
    "umur": 2,
    "warna": "putih",
    "jenis": "persia"
}

print(kucing.items())

for x,y in kucing.items():
    print(x, ":", y)