# numbers = input().split(",")
# res = list(map(int, numbers))
# list_arr = []

# print(3 ** 3)

bilangan = int(input("Masukan range bilangan : "))
list_arr = []

for i in range(1, bilangan + 1):
    pangkat = i ** 3
    list_arr.append(pangkat)

print(list_arr)