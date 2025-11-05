# def cek_angka(n = 0):
#     if n % 2 == 0:
#         return "Genap"
#     else:
#         return "Ganjil"

# angka = int(input("masukan angka:  ")) 

# print("angka yang kamu masukan merupakan angka",cek_angka(angka))

# def hitung_luas_persegi(sisi = 0):
#     return print(f" Luas perseginya adalah {sisi * sisi}")
    
# hitung_luas_persegi(int(input("masukan sisi persegi: ")))

# Arbitrary Arguments
# def list_angka(*angka):
#     print(f"list angka yang sistem masukan adalah: {angka}")
#     for n in angka :
#         if n % 2 == 0:
#             print(f"angka {n} adalah Genap")
#         else:
#             print(f"angka {n} adalah Ganjil")

# list_angka(1,4,3,12,54,7,13,990,11,100.0, 53.2, 0.5)

# Arbitrary Keywoards Arguments
# def data_diri(**data): 
#     for key, value in data.items():
#         print(f"{key} : {value}")

# data_diri(nama="Syarif Ihya Izzuddin", umur=20, alamat="Jl. Mawar No. 23", jurusan="Informatika", universitas="Universitas XYZ")
