tiket = input("Metode tiket yang anda pilih ? (offline/online/jendela) ").lower()
a = 2500
b = 3500
c = 4500
d = 6000
e = 8000
total = 0

seat = input('''
Pilih jenis kursi :
Biasa           (A)
Paviliun        (B)
Paviliun Atas   (C)
VIP             (D)
VVIP            (E)
Pilihan hanya A, B, C, D, atau E !
    ''').lower()

if tiket == "offline":
    if seat == "a":
        diskon = a * (8/100)
        total = a - diskon
    elif seat == "b":
        diskon = b * (8/100)
        total = b - diskon
    elif seat == "c":
        diskon = c * (8/100)
        total = c - diskon
    elif seat == "d":
        diskon = d * (8/100)
        total = d - diskon
    elif seat == "e":
        diskon = e * (8/100)
        total = e - diskon
elif tiket == "online":
    if seat == "a":
        diskon = a * (10/100)
        total = a - diskon
    elif seat == "b":
        diskon = b * (10/100)
        total = b - diskon
    elif seat == "c":
        diskon = c * (10/100)
        total = c - diskon
    elif seat == "d":
        diskon = d * (10/100)
        total = d - diskon
    elif seat == "e":
        diskon = e * (10/100)
        total = e - diskon
elif tiket == "jendela":
    if seat == "a":
        total = a
    elif seat == "b":
        total = b
    elif seat == "c":
        total = c
    elif seat == "d":
        total = d
    elif seat == "e":
        total = e
else:
    print("error")

print(f'''
total pesanan anda adalah {total}
''')