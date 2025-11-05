print("\n---------------Studi Kasus 1---------------\n")

# Studi Kasus 1
nilai_ipk = int(input("Masukan Nilai IPK mu..."))

if nilai_ipk >= 90 :
    print("IPK: A")
elif nilai_ipk < 0:
    print("Nilai IPK tidak Valid")
elif nilai_ipk > 100:
    print("Nilai IPK tidak Valid")
else:
    if nilai_ipk >= 80:
        print("IPK : B")
    else:
        if nilai_ipk >= 70:
            print("IPK : C")
        else:
            print("IPK : D")

print("\n---------------Studi Kasus 2---------------\n")

# Studi Kasus 2
model = {
    "gender" : int(input("Gender? (laki-laki = 1, wanita = 0)....")),
    "age" : int(input("Usia? (dalam tahun)....")),
    "height" : int(input("Tinggi Badan? (Cm)....")),
    "iq" : int(input("IQ?..."))
}

if model["age"] >= 18 and model["age"] <= 25:
    if model["iq"] >= 130:
        if model["gender"] == 1 :
            if model["height"] >= 177 :
                print("Orang tersebut layak jadi Model")
        else :
            if model["height"] >= 170 :
                print("Orang tersebut layak jadi Model")


print("\n---------------Studi Kasus 3---------------\n")

# Studi Kasus 3
jenis_kendaraan = int(input("Jenis kendaraan (motor = 0, mobil = 1)?..."))
waktu_parkir = int(input("Lama parkir (jam)?..."))

if(jenis_kendaraan == 0):
    biaya_parkir = 3000 #satuan rupiah
    if waktu_parkir >= 10:
        biaya_parkir= 20000
    elif waktu_parkir > 0:
        while waktu_parkir > 0 :
            waktu_parkir -= 1
            biaya_parkir += 2000
elif(jenis_kendaraan == 1):
    biaya_parkir = 5000 #satuan rupiah
    if waktu_parkir >= 10:
        biaya_parkir= 30000
    elif waktu_parkir > 0:
        while waktu_parkir > 0 :
            waktu_parkir -= 1
            biaya_parkir += 3000

print("Total biaya parkir: ", biaya_parkir)


print("\n---------------Studi Kasus 4---------------\n")

# Studi Kasus 4
hari = int(input("Masukan hari (senin = 1, selasa = 2, rabu = 3, dst..)?..."))
kategori = int(input("Masukan kategori penonton (dewasa = 1, mahasiswa = 2, anak-anak = 3)?..."))
biaya_tiket = 0

if kategori in [1,2,3]:
    if hari in [1,2,3,4,5,6,7]:
        if hari in [6,7]:
            if kategori == 1 :
                biaya_tiket = 70000
            elif kategori == 2 :
                biaya_tiket = 60000
            elif kategori == 3 :
                biaya_tiket = 40000
        else:
            if kategori == 1 :
                biaya_tiket = 50000
            elif kategori == 2 :
                biaya_tiket = 40000
            elif kategori == 3 :
                biaya_tiket = 30000

    else:
        print("Input hari tidak valid")
else:
    print("Input kategeori tidak valid")

print("Biaya tiketnya sebesar: ", biaya_tiket)


print("\n---------------Studi Kasus 5---------------\n")

# Studi Kasus 5
total_belanja = int(input("Masukan nilai rupiah total belanja (Rp)?..."))
member = int(input("apakah anda member (ya = 1, tidak = 0)?..."))
diskon = 0

if member == 1 :
    diskon += 5

if total_belanja > 0 :
    if total_belanja >= 200000:
        diskon += 5
        if total_belanja >= 500000:
            diskon +=5
            print("Total diskon: ",diskon,"%")
            print("Total potongan: ",total_belanja*diskon/100)
            print("Total belanja: Rp.", (total_belanja - (total_belanja*diskon/100)))
        else: 
            print("Total diskon: ",diskon,"%")
            print("Total potongan: ",total_belanja*diskon/100)
            print("Total belanja: Rp.", (total_belanja - (total_belanja*diskon/100)))
    else: 
        print("Total diskon: ",diskon,"%")
        print("Total potongan: ",total_belanja*diskon/100)
        print("Total belanja: Rp.", (total_belanja - (total_belanja*diskon/100)))

