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



print("\n---------------------Latihan 2---------------------\n")

try_attempt = 0

def login(password):
    if password != "Latihan" :
        return False
    elif password == "Latihan":
        return True

while try_attempt < 3 :
    input("Username : ")
    if login(input("Password: ")) == True:
        print("berhasil login")
        break
    else:
        print("Gagal login")
    try_attempt += 1
    print(f"Percobaan ke {try_attempt}")


print("\n---------------------Latihan 3---------------------\n")

print("Input Mulai")
jam_mulai = int(input("Jam: "))
menit_mulai = int(input("Menit: "))
detik_mulai = int(input("Detik:"))

print("\nInput Selesai")
jam_selesai = int(input("Jam: "))
menit_selesai = int(input("Menit: "))
detik_selesai = int(input("Detik: "))


total_waktu_mulai = jam_mulai*3600 + menit_mulai*60 + detik_mulai
total_waktu_selesai = jam_selesai*3600 + menit_selesai*60 + detik_selesai

selisih_waktu = total_waktu_selesai - total_waktu_mulai

selisih_jam = selisih_waktu // 3600
selisih_menit = selisih_waktu % 3600 // 60
selisih_detik = selisih_waktu  % 3600 % 60

if (jam_mulai or jam_selesai > 24) and (menit_mulai or menit_selesai >= 60) and (detik_mulai or detik_selesai >= 60):
    print(f"Data yang dimasukan tidak valid")
elif (jam_mulai or jam_selesai < 0) and (menit_mulai or menit_selesai < 0) and (detik_mulai or detik_selesai < 0):
    print(f"Data yang dimasukan tidak valid ----- Terbuang dalam Waktu")
else :
    print(f"{selisih_jam} Jam - {selisih_menit} Menit - {selisih_detik} Detik")