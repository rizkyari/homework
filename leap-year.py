# year = int(input("Input year"))

# jawaban 1
# if year % 4 == 0:
#     print("Tahun Kabisat")
#     if year % 100 == 0 and year % 400 != 0:
#         print("Bukan")
# else:
#     print("Bukan")

# jawaban 2
year = int(input("Input year"))
if year % 4 == 0 and year % 100 !=0 or year % 400 == 0:
    print(year, "adalah tahun kabisat")
else:
    print(year, "bukanlah tahun kabisat")