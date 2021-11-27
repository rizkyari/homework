numbers = input("Masukan angka yang diinginkan pisahkan dengan koma (',')\n").split(",")
res = list(map(int, numbers))
list_arr = []

for i in reversed(res):
    list_arr.append(i)

print(f"Hasil balikan bilangan {list_arr}")