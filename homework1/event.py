tiket = input("Metode tiket yang anda pilih ? (offline/online/jendela) ").lower()
jumlah = int(input("Masukan jumlah tiket yang ingin dibeli : "))
a = 2500
b = 3500
c = 4500
d = 6000
e = 8000
total = 0
choosen = ''
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
        pesanan = a * jumlah
        diskon = pesanan * (8/100)
        total = pesanan - diskon
        choosen = "biasa"
    elif seat == "b":
        pesanan = b * jumlah
        diskon = pesanan * (8/100)
        total = pesanan - diskon
        choosen = "paviliun"
    elif seat == "c":
        pesanan = c * jumlah
        diskon = pesanan * (8/100)
        total = pesanan - diskon
        choosen = "paviliun atas"
    elif seat == "d":
        pesanan = d * jumlah
        diskon = pesanan * (8/100)
        total = pesanan - diskon
        choosen = "vip"
    elif seat == "e":
        pesanan = e * jumlah
        diskon = pesanan * (8/100)
        total = pesanan - diskon
        choosen = "vvip"
elif tiket == "online":
    if seat == "a":
        pesanan = a * jumlah
        diskon = pesanan * (10/100)
        total = pesanan - diskon
        choosen = "biasa"
    elif seat == "b":
        pesanan = b * jumlah
        diskon = pesanan * (10/100)
        total = pesanan - diskon
        choosen = "paviliun"
    elif seat == "c":
        pesanan = c * jumlah
        diskon = pesanan * (10/100)
        total = pesanan - diskon
        choosen = "paviliun atas"
    elif seat == "d":
        pesanan = d * jumlah
        diskon = pesanan * (10/100)
        total = pesanan - diskon
        choosen = "vip"
    elif seat == "e":
        pesanan = e * jumlah
        diskon = pesanan * (10/100)
        total = pesanan - diskon
        choosen = "vvip"
elif tiket == "jendela":
    if seat == "a":
        total = a * jumlah
        choosen = "biasa"
    elif seat == "b":
        total = b * jumlah
        choosen = "paviliun"
    elif seat == "c":
        total = c * jumlah
        choosen = "paviliun atas"
    elif seat == "d":
        total = d * jumlah
        choosen = "vip"
    elif seat == "e":
        total = e * jumlah
        choosen = "vvip"
else:
    print("error")

print(f'''
Anda akan membeli tiket secara {tiket} .
Dengan tipe seat {choosen} berjumlah {jumlah} buah
Total pesanan anda adalah Rp.{total}
''')