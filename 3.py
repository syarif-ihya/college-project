# Nama : Syarif Ihya Izzuddin
# NIM : 2503929

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
elif selisih_waktu < 0:
    print(f"Data yang dimasukan tidak valid ----- Terbuang dalam Waktu")
else :
    print(f"{selisih_jam} Jam - {selisih_menit} Menit - {selisih_detik} Detik")