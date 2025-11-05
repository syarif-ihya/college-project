# Nama : Syarif Ihya Izzuddin
# NIM : 2503929

print("\n---------------------Latihan 2---------------------\n")

try_attempt = 0

def login(password):
    if password != "Latihan" :
        return False
    elif password == "Latihan":
        return True

while try_attempt < 3 :
    input("Username : ")
    if login(input("Password: ")) == True:
        print("berhasil login")
        break
    else:
        print("Gagal login")
    try_attempt += 1
    print(f"Percobaan ke {try_attempt}")