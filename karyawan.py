gender = input("apa jenis kelamin anda ? (L/P) ").lower()

if gender == "l":
    status = input("apakah anda sudah menikah ? (Y/T)").lower()
    if status == "y" or status == "t":
        age = input("berapa umur anda : ")
        if age.isnumeric():
            age = int(age)
            if age >= 20 and age <=40:
                print("anda cocok bekerja dimana saja")
            elif age >= 40 and age <= 60:
                print("anda cocok kerja di perkantoran")
            else:
                print("ERROR")
        else:
            print("anda salah")
    else:
        print('anda jomblo')
elif gender == "p":
    print("Anda cocok kerja di perkantoran")
else: 
    print("gender hanya ada dua (L/P)")

