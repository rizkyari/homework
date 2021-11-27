bilangan = int(input("Masukan bilangan : "))
list_arr = []
for p in range(2, bilangan+1):
    for i in range(2, p):
        if p % i == 0:
            break
    else:
        list_arr.append(p)

print(list_arr)