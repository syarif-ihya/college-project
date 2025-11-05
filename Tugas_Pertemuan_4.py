
# ------------------ (Kuis 1) ----------------------
print("\n---------Kuis 1----------\n")

hobi_A = {"membaca", "berenang", "musik", "traveling"}
hobi_B = {"musik", "gaming", "traveling", "fotografi"}

# gabungan hobi_A dan hobi_B
hobi_gabungan = hobi_A.union(hobi_B)
print("Hobi gabungan A dan B:", hobi_gabungan)

# hobi yang sama antara hobi_A dan hobi_B
hobi_sama = hobi_A.intersection(hobi_B)
print("Hobi yang sama antara A dan B:", hobi_sama)

# hobi yang unik di hobi_A
hobi_unik_A = hobi_A.difference(hobi_B)
print("Hobi yang unik di A:", hobi_unik_A)

# mengecek apakah "gaming" ada di hobi_A
print("Apakah A memiliki hobi gaming?",("gaming" in hobi_A))



# ------------------ (Kuis 2) ----------------------
print("\n---------Kuis 2----------\n")

semester1 = {"Matematika", "Pemrograman Dasar", "Bahasa Inggris", "Sistem Digital"}
semester2 = {"Pemrograman Dasar", "Basis Data", "Bahasa Inggris", "Jaringan Komputer"}

# mata kuliah yang diulang di semester2
mata_kuliah_ulang = semester1.intersection(semester2)
print("Mata kuliah yang diulang di semester 2:", mata_kuliah_ulang)

# seluruh mata kuliah yang diambil oleh orang itu
mata_kuliah_total = semester1.union(semester2)
print("Seluruh mata kuliah yang diambil:", mata_kuliah_total)

# mata kuliah yang hanya diambil di semester2
mata_kuliah_unik_B = semester2.difference(semester1)
print("Mata kuliah yang hanya diambil di semester 2:", mata_kuliah_unik_B)



# ------------------- (Kuis 3) ----------------------
print("\n---------Kuis 3----------\n")

hari_pertama = {"Andi", "Budi", "Citra", "Dewi", "Eka"}
hari_kedua = {"Budi", "Citra", "Fajar", "Gita", "Andi"}

# Orang yang hadir di kedua hari
hadir_kedua_hari = hari_pertama.intersection(hari_kedua)
print("Orang yang hadir di kedua hari:", hadir_kedua_hari)

# orang yang hanya hadir satu hari saja
hadir_satu_hari = hari_pertama.symmetric_difference(hari_kedua)
print("Orang yang hanya hadir satu hari saja:", hadir_satu_hari)    

# jumlah total seluruh orang yang hadir 
total_hadir = len(hari_pertama.union(hari_kedua))
print("Jumlah total seluruh orang yang hadir:", total_hadir, "orang")



# ------------------- (Kuis 4) ----------------------
print("\n---------Kuis 4----------\n")

kalimat = "python adalah bahasa pemrograman yang mudah dan python sangat populer"

# mengubah kalimat menjadi list kata yang unik
kata_set = set(kalimat.split())
print("Set kata:", kata_set)

# menghitung jumlah kata unik
jumlah_kata_unik = len(kata_set)
print("Jumlah kata unik:", jumlah_kata_unik)

# mengecek apakah kata "java" ada di dalam set
print("Apakah kata 'java' ada di dalam set?", ("java" in kata_set))



# ------------------- (Kuis 5) ----------------------
print("\n---------Kuis 5----------\n")

cabang_A = {"beras", "minyak", "gula", "kopi", "susu"}
cabang_B = {"beras", "gula", "kopi", "teh", "coklat"}

# mencari produk yang tersedia di kedua cabang
produk_tersedia = cabang_A.intersection(cabang_B)
print("Produk yang tersedia di kedua cabang:", produk_tersedia)

# produk yang hanya di cabang A
produk_unik_A = cabang_A.difference(cabang_B)
print("Produk yang hanya di cabang A:", produk_unik_A)

# membuat set baru yang berisi seluruh produk yang dijual (gabungan A dan B)
produk_yang_dijual = cabang_A.union(cabang_B)
print("Seluruh produk yang dijual:", produk_yang_dijual)



