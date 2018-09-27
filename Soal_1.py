def jogjakarta(kode_paket):
    return {
        "S": [150000, 0.025],
        "K": [500000, 0.05],
        "R": [1000000, 0.1]
    }[kode_paket]

def semarang(kode_paket):
    return {
        "S": [200000, 0.03],
        "K": [700000, 0.06],
        "R": [1300000, 0.12]
    }[kode_paket]

def jakarta(kode_paket):
    return {
        "S": [350000, 0.04],
        "K": [1200000, 0.08],
        "R": [2300000, 0.12]
    }[kode_paket]

def get_harga_paket(kode_tujuan, kode_paket):
    if kode_tujuan == "JGJ":
        result = jogjakarta(kode_paket)[0]
    elif kode_tujuan == "SMR":
        result = semarang(kode_paket)[0]
    elif kode_tujuan == "JKT":
        result = jakarta(kode_paket)[0]
    return result

def get_pajak(kode_tujuan, kode_paket):
    if kode_tujuan == "JGJ":
        result = jogjakarta(kode_paket)[1]
    elif kode_tujuan == "SMR":
        result = semarang(kode_paket)[1]
    elif kode_tujuan == "JKT":
        result = jakarta(kode_paket)[1]
    return result

def get_tujuan(kode_tujuan):
    return {
        "JGJ": "Jogjakarta",
        "SMR": "Semarang",
        "JKT": "Jakarta"
    }[kode_tujuan]

def get_paket(kode_paket):
    return {
        "S": "Sendiri",
        "K": "Keluarga",
        "R": "Regu"
    }[kode_paket]

print(">> Agen Bus Sinar Cemerlang\n")

print("--------------------------------\n")

nama_petugas = input("Masukkan Nama Petugas : ")
nama_pelanggan = input("Masukkan Nama Pelanggan : ")
kode_tujuan = input("Masukkan Kode Tujuan [JGJ, SMR, JKT] : ")
kode_paket = input("Masukkan Kode Paket [S/K/R] : ")
tanggal_berangkat = input("Masukkan Tanggal Keberangkatan : ")

print("\n=========>> Struk Pembayaran <<==========")
print("=====>> Agen Bus Sinar Cemerlang <<=====\n")

print(f"\tNama Petugas : {nama_petugas}")
print(f"\tNama Pelanggan : {nama_pelanggan}")
print(f"\tTanggal Keberangkatan : {tanggal_berangkat}")

print("\n--------------------------------\n")

harga_paket = get_harga_paket(kode_tujuan, kode_paket)
pajak = get_pajak(kode_tujuan, kode_paket) * harga_paket
total_biaya = harga_paket + pajak

print(f"Tujuan : {get_tujuan(kode_tujuan)}")
print(f"Paket : {get_paket(kode_paket)}")
print(f"Harga : {harga_paket}")
print(f"Biaya Pajak : {pajak}")
print(f"Total Biaya : {total_biaya}")
