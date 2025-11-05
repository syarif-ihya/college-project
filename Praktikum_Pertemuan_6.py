x = 0
# Arithmetic Operator
print("x = ", x)
print("x + 1 = ", x+1)
print("x - 3 = ", x-3)
print("(x + 10)*2 = ", (x+10)*2)
print("(x + 10)**2 = ", (x+10)**2)
print("(x + 50)/3 = ", (x+50)/3)
print("(x + 50)//3 = ", (x+50)//3)
print("(x + 125)%7 = ", (x+125)%7)

# Comparison Operator
print("x == 0,", x == False & x == 0)
print("x != 0,", x != 0)
print("x > 0,", x > 0)
print("x < 0,", x < 0)
print("x >= 0,", x >= 0)
print("x <= 0,", x <= 0)

# Assignment Operator
x += 5
print("x += 5, x =", x)
x -= 2
print("x -= 2, x = ", x)
x *= 3
print("x *= 3, x = ", x)
x **= 2
print("x **= 2, x = ", x)
x /= 3
print("x /= 3, x = ", x)
x //= 2
print("x //= 2, x = ", x)
x %= 5
print("x %= 5, x = ", x)

y = -x

# Conditional Operator
print(x>0 and y>0)
print(x>0 or y>0)
print(not(x>0 and y>0))
print(not(x>0 or y>0))

a = [1,2,3]
b = (1,2,3)
c = {1,2,3}
d = {1:"Satu", 2:"Dua", 3:"Tiga"}
e = [1,2,3]
f = a

# Membership Operator
print("did x in a? ", x in a)
print("did y not in b? ", y not in b)
print("did x in c? ", x in c)
print("did x not in d? ", x not in d)
# Identity Operator
print("did a is e? ", a is e)
print("did a is f? ", a is f)
print("did b is not e? ", b is not e)

print("a = ", a)
if(1 not in a):
    print("1 bukan bagian dari a")
else :
    print("1 bagian dari a")
if(10 not in a):
    print("10 bukan bagian dari a")
else :
    print("10 bagian dari a")
if(-1 not in a):
    print("-1 bukan bagian dari a")
else :
    print("-1 bagian dari a")

kehadiran = 80 #dalam satuan persen (%)
nilai_akhir = 55 
bayar_ukt = "sudah"

if (not(nilai_akhir < 75) and kehadiran >= 80 and bayar_ukt == "sudah"):
    print("Mahasiswa Lulus dan dapat ikut Wisuda")
elif ((nilai_akhir < 75 and nilai_akhir > 50) and kehadiran >= 80 and bayar_ukt == "sudah"):
    print("Mahasiswa Belum Lulus tapi dapat ikut Wisuda")
else :
    print("Mahasiswa Tidak Lulus dan belum dapat ikut Wisuda")

print("Mahasiswa Lulus") if nilai_akhir >= 75 else print("Mahasiswa tidak Lulus"), print("Mahasiswa Miskin atau Malas Bayar UKT") if bayar_ukt != "sudah" else print("Mahasiswa hebat, sudah bayar UKT!")



print("\n------------------------\n")

# Soal 1 (Lebih besar)
# A = int(input("Masukan variabel A..."))
# print("A = ", A)
# B = int(input("Masukan variabel B..."))
# print("B = ", B)
# print("Nilai A > B : ", A>B)

# # Soal 2 (Ganji Genap)
# C = int(input("Masukan variabel C..."))
# print("C = ", C)
# print("Nilai C Genap : ", C%2==0)

print("\n------------------------\n")



