bilangan = int(input("Masukan bilangan akhiran : "))
list_arr = []
for i in range(1, bilangan + 1):
    list_arr.append(i)

total = sum(list_arr)
print(f"total penjumlahan adalah : {total}")