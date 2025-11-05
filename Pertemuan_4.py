print("\n---------Set----------\n")

set_data = {"apple", "banana", "cherry", 1, 2, 3}
print("Set:", set_data)   
# print("Tipe data set:", type(set_data))
# a = set_data
# print(a)
# print(len(a))
# a.add("orange") # menambahkan data di set
# print(a)
# a.remove("banana") # menghapus data di set
# print(a)
# print(set_data)

# untuk mencari item dalam set data
print("apple" in set_data) # mengecek apakah "apple" ada di set_data)
print("melon" in set_data) # mengecek apakah "melon" ada di set_data)
for i in set_data:
    print(i)


set_data.add("melon")
print(set_data)
set_data2 = {"grape", "kiwi", "strawberry"}
set_data.update(set_data2) # menggabungkan dua set
print(set_data)
print(set_data2)


set_data3 = set_data.union(set_data2) # menggabungkan dua set dan menyimpan di set baru
print("Set data 3 : ", set_data3)


set_data.intersection_update(set_data2) # menyimpan irisan (intersection) dari dua set di set pertama
print("Set data setelah intersection update dengan set_data2 : ", set_data)

set_data4 = set_data3.intersection(set_data) # menyimpan irisan (intersection) dari dua set di set baru
print("Set data 4 (irisan set_data3 dan set_data) : ", set_data4)

print("Set Data 1: ", set_data)
print("Set Data 2: ", set_data2)
print("Set Data 3: ", set_data3)
print("Set Data 4: ", set_data4)

set_data.symmetric_difference_update(set_data3) 
print("Set data 1 setelah symmetric difference update dengan set_data3 : ", set_data)

set_data4 = set_data.symmetric_difference(set_data2) # menyimpan symmetric difference dari dua set di set baru
print("Set data 4 (symmetric difference set_data dan set_data2) : ", set_data4)

# selain menambah/update dari sesama set, kita juga bisa menambah dari list atau tuple
list_data = ["apel", "jeruk", "mangga"]
set_data.update(list_data)
print("Set data setelah ditambahkan dari list_data: ", set_data)   
tupple_data = ("semangka", "kiwi", "nanas")
set_data.update(tupple_data)
print("Set data setelah ditambahkan dari tupple_data: ", set_data)

set_data.pop() # menghapus item random dari set
print("Set data setelah pop: ", set_data)
set_data.discard("kiwi") # menghapus item tertentu dari set
print("Set data setelah discard kiwi: ", set_data)
set_data.remove("melon") # menghapus item tertentu dari set, jika item tidak ada akan error
print("Set data setelah remove melon: ", set_data)
set_data4.clear() # menghapus semua item di set
print("Set data 4 setelah clear: ", set_data4)



print("\n---------Dictionary----------\n")



dictionary = {
    "nama": "Shirin",   
    "umur": 18,
    "hobi": {"membaca", "menulis", "bermain"},
    "male": True,
    "height": 165.5,
}
print("Dictionary:", dictionary)
print("Tipe data dictionary:", type(dictionary))
print("Panjang dictionary:", len(dictionary))

dict = dict(Nama = "Ramzi", Spesies = "Kucing Persia", Umur = 2)
print("Dictionary dict:", dict)

print("Nama saya:", dictionary["nama"])
print("Peliharaan saya:", dict["Spesies"], "bernama", dict["Nama"])
print("Items di dictionary:", dictionary.items())

print("Daftar kunci (keys):", dictionary.keys())
print("Daftar nilai (values):", dictionary.values())

dictionary.update({"kota": "Banten", "umur": 19}) # menambah atau mengupdate item di dictionary
print("Dictionary setelah update:", dictionary)