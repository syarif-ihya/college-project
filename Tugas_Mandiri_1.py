print("\n---------Tugas Mandiri----------\n")

print("Nama: Syarif Ihya Izzuddin")
print("NIM: 2503929")

print("\n---------Soal no 1-----------\n")
# 1. Diketahui list dengan nilai 10 mahasiswa sebagai berikut: 88, 75, 63, 97, 82, 74, 91, 80, 81, 63
nilai_mahasiswa = [88, 75, 63, 97, 82, 74, 91, 80, 81, 63]
    # a. Tampilkan
max_nilai = max(nilai_mahasiswa)
min_nilai = min(nilai_mahasiswa)
rata_rata = sum(nilai_mahasiswa) / len(nilai_mahasiswa)
print("Nilai tertinggi:", max_nilai)
print("Nilai terendah:", min_nilai)    
print("Rata-rata nilai:", rata_rata)
    # b. Tampilkan angka terbesar kedua daalam daftar nilai tersebut
nilai_mahasiswa.sort()
print("Nilai terbesar kedua:", nilai_mahasiswa[-2])

print("\n---------Soal no 2-----------\n")
# 2. Dikethui tuple yang berisi daftar pasangan (latitude, longitude) sebuah lokasi sebagai berikut:
Jakarta = (-6.2088, 106.8456)
Bandung = (-6.9175, 107.6191)
Surabaya = (-7.2575, 112.7521)
    # a. Tampilkan koordinat kota Bandung
print("Koordinat kota Bandung:", Bandung)
    # b. Tampilkan jumlah lokasi yang tersimpan
lokasi = [Jakarta, Bandung, Surabaya]
print("Jumlah lokasi yang tersimpan:", len(lokasi))