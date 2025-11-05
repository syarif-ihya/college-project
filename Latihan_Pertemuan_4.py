# ------------------- (Latihan 1) ----------------------
print("\n---------Latihan 1----------\n")

# Input
numbers = [10, 20, 20, 30, 40, 50, 50, 60]

# Harapan Output [10, 20, 30, 40, 50, 60] : x
x = set(numbers)
x = list(x)
x = sorted(x)
print(x)



# ------------------- (Latihan 2) ----------------------
print("\n---------Latihan 2----------\n")

# Input
students = {
    "Alice" : "Computer Science",
    "Bob" : "Mathematics",
    "Charlie" : "Physics",
    "David" : "Computer Science",
    "Eva" : "Mathematics",
}

# Harapan Output "Computer science": 2 orang, "mathematics": 2 orang, "physics": 1 orang
cs_students = []
math_students = []
physic_students = []
for keys in students:
    if students[keys] == "Computer Science":
        cs_students.append(keys)
    elif students[keys] == "Mathematics":
        math_students.append(keys)
    elif students[keys] == "Physics":
        physic_students.append(keys)
print("Prodi Computer Science sebanyak",len(cs_students), "Orang")
print("Prodi Mathematics sebanyak",len(math_students), "Orang")
print("Prodi Physics sebanyak",len(physic_students), "Orang")



# ------------------- (Latihan 3) ----------------------
print("\n---------Latihan 3----------\n")

# Data
student_info = {
    "Alice": {"age":20, "major":"Computer Science"},
    "Bob": {"age":21, "major":"Mathematics"},
    "Charlie": {"age":19, "major":"Physics"},
}

# Harapannya, user memberikan Input nama yang diinginkan, berdasarkan itu Outputnya haruslah sesuai dengan orang yang di input
user_input = input("Tuliskan nama Pelajar yang ingin kamu ketahui : ")
info = ""
for keys in student_info:
    if user_input.lower() == keys.lower():
        info = f"{user_input.capitalize()} berumur {student_info[keys]["age"]} Tahun, ia Prodi {student_info[keys]["major"]}"
print(info)