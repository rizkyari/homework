tiket = input("Metode tiket yang anda pilih ? (offline/online) ").lower()
biasa = 2500
paviliun = 3500
paviliun_atas = 4500
vip = 6000
vvip = 8000

if tiket == "offline":
    seat = input('''
    Pilih jenis kursi :
    Biasa           (A)
    Paviliun        (B)
    Paviliun Atas   (C)
    VIP             (D)
    VVIP            (E)
    Pilihan hanya A, B, C, D, atau E !
    ''').lower()
elif tiket == "online":
    seat = input('''
    Pilih jenis kursi :
    Biasa           (A)
    Paviliun        (B)
    Paviliun Atas   (C)
    VIP             (D)
    VVIP            (E)
    Pilihan hanya A, B, C, D, atau E !
    ''').lower()
else :
    print('online atau offline saja')

