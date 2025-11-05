import numpy as np

print("---------------Tugas 1----------------\n")

array_id = np.array([24,28,25,30,27,28,29,32,30,29])

def celsius_to_fahrenheit(celsius):
    fahrenheit = (9/5) * celsius + 32
    return fahrenheit

array_id = celsius_to_fahrenheit(array_id)
print(array_id)


print("\n---------------Tugas 2----------------\n")

nilai_ujian = np.array([1,14,15,16,17,18,19, 2,3,4,11,12,13,5,6,7,8,9,10,27,28,29,20,21,22,23,24,25,26,30])

list = (np.sort(nilai_ujian)[::-1])

top_list = list[:5]
print(top_list)


print("\n---------------Tugas 3----------------\n")

riwayat_margin = np.array([120,180,80,90,100,130,150,250,190,215,240,280,300,330])

print(f"keuntungan rata-rata toko dalam seminggu {riwayat_margin.mean()}")
print(f"Keuntungan tertinggi: {riwayat_margin.max()} pada hari ke-{riwayat_margin.tolist().index(riwayat_margin.max())+1}")
print(f"Keuntungan terendah: {riwayat_margin.min()} pada hari ke-{riwayat_margin.tolist().index(riwayat_margin.min())+1}")