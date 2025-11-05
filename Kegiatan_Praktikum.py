# NAMA : Syarif Ihya Izzuddin
# NIM : 2503929


print("\n---------Kuis 1----------\n")

nilai = [78, 85, 62, 90, 70, 88, 95, 60, 72 ]
# 1. Tampilkan jumlah mahasiswa dalam kelas
jumlah_mahasiswa = len(nilai)
print("Jumlah mahasiswa dalam kelas:", jumlah_mahasiswa)
# 2. Hitung rata-rata nilai 
rata_rata = sum(nilai) / jumlah_mahasiswa
print("Rata-rata nilai:", rata_rata)
# 3. Cari nilai tertinggi dan terendah
sorted_nilai = nilai.copy()
sorted_nilai.sort()
max_nilai = sorted_nilai[-1]
min_nilai = sorted_nilai[0]
print("Nilai tertinggi:", max_nilai, "\nNilai terendah:", min_nilai)
# 4. Buat list baru berisi nilai yang lulus (nilai >= 70)
nilai_lulus = []
for nilai in nilai_lulus:
    if nilai >= 70:
        nilai_lulus.append(nilai)
print("Nilai yang lulus:", nilai_lulus)


print("\n---------Kuis 2----------\n")


belanja = ["beras", "minyak", "gula", "kopi", "susu"]
# 1. Tambahkan item "teh" kedalam daftar
belanja.append("teh")
# 2. Hapus item "kopi" dari daftar
belanja.remove("kopi") # atau belanja.pop(3)
# 3. Cetak item ke-2 dan item terakhir
print("Item ke-2:", belanja[1], "\nItem terakhir:", belanja[-1])
# 4. Urutkan daftar belanja secara alfabet
belanja.sort()
print("Daftar belanja terurut:", belanja)


print("\n---------Kuis 3----------\n")


kehadiran = [1,1,0,1,1,0,1]
# 1. Hitung jumlah hari hadir dan tidak hadir
print("Jumlah hari hadir:", kehadiran.count(1), "\nJumlah hari tidak hadir:", kehadiran.count(0))
# 2. Tentukan apakah mahasiswa ini layak ikut ujian (syarat: hadir >= 75% )
print("Layak ikut ujian:", (kehadiran.count(1)/len(kehadiran)) >= 0.75)
# 3. Ubah nilai hari ke-3 menjadi 1 (misalnya ada kesalahan input data)
kehadiran[2] = 1
print("Kehadiran setelah koreksi:", kehadiran)


print("\n---------Kuis 4----------\n")


mahasiswa = ["Andi", "Budi", "Citra", "Dewi", "Eka"]
# 1. Cetak nama mahasiswa ke-3
print("Nama mahasiswa ke-3:", mahasiswa[2])
# 2. Tambahkan 2 nama baru ke dalam list
mahasiswa.extend(["Fajar", "Gina"])
print("Daftar mahasiswa setelah penambahan:", mahasiswa)
# 3. Hapus nama "Budi"
mahasiswa.remove("Budi"); print("Daftar mahasiswa setelah penghapusan:", mahasiswa)
# 4. Buat list baru hanya 3 nama pertama
grup_a = mahasiswa[0:3]
print("Grup A (3 nama pertama):", grup_a)


print("\n---------Kuis 5----------\n")


transaksi = [50000, -20000, -15000, 30000, -10000]
# 1. Hitung total saldo akhir 
print("Total saldo akhir:", sum(transaksi))
# 2. Hitung berapa kali mahasiswa melakukan transaksi pengeluaran (negatif)
jumlah_transaksi = 0
for i in transaksi:
    if i < 0:
        jumlah_transaksi += 1
print("Jumlah transaksi pengeluaran:", jumlah_transaksi)
# 3. Simpan transaksi baru -25000 ke dalam list
transaksi.append(-25000)
# 4. Tampilkan semua transaksi dari terbesar ke terkecil
transaksi.sort(reverse=True)
print("Semua transaksi (terbesar ke terkecil):", transaksi)


print("\n---------Studi Kasus----------\n")


buah = ['apel', 'jeruk', 'ceri', 'durian', 'apel', 'mangga']
# 1. Ganti item dengan nama "ceri" menjadi "cherry"
ceri = buah.index("ceri")
buah[ceri] = "cherry"
# 2. Tambahkan item dengan nama dan index yang ditentukan oleh user
nama_buah = input("Pilih buah yang ingin kamu tambahkan: ")
index_buah = input("pilih index (0-6) untuk menambahkan buah: ")
buah.insert(int(index_buah), nama_buah)
print("Daftar buah setelah penambahan:", buah)
# 3. Urutkan item pada list sesuai dengan abjadnya
buah.sort()
print("Daftar buah setelah diurutkan:", buah)

