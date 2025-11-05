# Nama : Syarif Ihya Izzuddin
# NIM : 2503929

print("\n---------------------Latihan 1---------------------\n")

# 1. Fungsi Fibonanci
def fibonancy(n):
    x = 0
    y = 1

    for i in range(n):
        if i % 2 == 0:
            print(x)
            x += y
        elif i % 2 == 1:
            print(y)
            y += x  

fibonancy(int(input("Masukan jumlah deret angka Fibonanci yang ingin dimasukan: ")))

print("\n")

# 2. Menghitung volume tabung yang dibuat dalam fungsi
def luas_tabung(r,t):
    return 2*((22/7)*r**2) + (22/7)*2*r*t

print(f"Luas tabung untuk jari-jari dan tinggi yang sudah kamu masukan adalah: {luas_tabung(int(input("Masukan Jari-jari :")),int(input("Masukan Tinggi tabung : ")))}")

print("\n")

# 3 Input banyak angak, total, rata rata
angka = (input("Masukan beberapa angka dipisah dengan (spasi): "))
list_angka = angka.split()
total = 0
for angka in range(len(list_angka)):
    total += int(list_angka[angka])
1

print(f'''
Input : {list_angka}
Total : {total}
Rata-rata : {total/len(list_angka)}
''')
