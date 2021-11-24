baterai = float(input("Masukkan harga total pesanan dari mainan baterai : "))
kunci = float(input("Masukkan harga total pesanan dari mainan kunci : "))
listrik = float(input("Masukkan harga total pesanan dari mainan listrik : "))

if baterai > 1000:
    diskon = baterai * (10/100)
    total_baterai = baterai - diskon
    print(total_baterai) 

if kunci > 100:
    diskon = kunci * (5/100)
    total_kunci = kunci - diskon
    print(total_kunci)

if listrik > 500:
    diskon = listrik * (10/100)
    total_listrik = listrik - diskon
    print(total_listrik)

grand_total = total_baterai + total_kunci + total_listrik

print(f"""
Berikut ini adalah pesanan anda :
Total pesanan mainan berbasis baterai : Rp{total_baterai}
Total pesanan mainan berbasis kunci : Rp {total_kunci}
Total pesanan mainan berbasis listrik : Rp {total_listrik}
Jadi seluruh pesanan anda berjumlah Rp{grand_total}
""")