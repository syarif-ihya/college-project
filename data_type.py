list = ["apple", "banana", "cherry", 1, 2, 3, ["a", "b", "c"]]
# print("List:", list)
# print("Tipe data list:", type(list))
# print(list[6][0])
# print(list[5:-1])
# list.append("orange") --> menambahkan data di akhir list
# list.insert(1, "orange") --> menambahkan data di index tertentu dan sisanya akan terdorong ke kanan
# list.pop(x) --> menghapus data index ke-x atau terakhir (jika kosong) di list
# list.remove("banana") --> menghapus data di list berdasarkan nilai
# list[2] = "orange" --> mengganti data di index tertentu
# list.clear() --> menghapus semua data di list
# list.copy() --> mengcopy data di list
# list.count("apple") --> menghitung jumlah kemunculan "apple" di list
# list.extend(["orange", "grape"]) --> menambahkan beberapa data di akhir list
# list.index("cherry") --> mencari index dari "cherry" di list
# list.reverse() --> membalik urutan data di list
# list.sort() --> mengurutkan data di list
# list.sort(reverse=True) --> mengurutkan data di list secara descending
# list.sort(key=str.lower) --> mengurutkan data di list tanpa memperhatikan kapitalisasi


tupple = ("apple", "banana", "cherry", 1, 2, 3, ("a", "b", "c"))
# print("Tupple:", tupple)
# print("Tipe data tupple:", type(tupple))
# print(tupple[3])
# print(len(tupple)) --> menghitung panjang (jumlah elemen) tupple


dictionary = {
    "nama": "Shirin", 
    "umur": 18,
    "kota": "Banten"
}
# print("Dictionary:", dictionary)
# print("Tipe data dictionary:", type(dictionary))
# print(dictionary["kota"])


set_data = {"apple", "banana", "cherry", 1, 2, 3}
# print("Set:", set_data)   
# print("Tipe data set:", type(set_data))
# a = set_data
# print(a)
# print(len(a))
# a.add("orange") # menambahkan data di set
# print(a)
# a.remove("banana") # menghapus data di set
# print(a)
# print(set_data)
# print("apple" in set_data) # mengecek apakah "apple" ada di set_data)
# print("melon" in set_data) # mengecek apakah "melon" ada di set_data)
# for i in set_data:
#     print(i)
# set_data.add("melon")
# print(set_data)
# set_data2 = {"grape", "kiwi", "strawberry"}
# set_data.update(set_data2) # menggabungkan dua set
# print(set_data)
# print(set_data2)
# set_data3 = set_data.union(set_data2) # menggabungkan dua set dan menyimpan di set baru
# print("Set data 3 : ", set_data3)
# set_data.intersection_update(set_data2) # menyimpan irisan (intersection) dari dua set di set pertama
# print("Set data setelah intersection update dengan set_data2 : ", set_data)
# set_data4 = set_data3.intersection(set_data) # menyimpan irisan (intersection) dari dua set di set baru
# print("Set data 4 (irisan set_data3 dan set_data) : ", set_data4)



