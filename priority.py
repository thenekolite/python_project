# -*- coding: utf-8 -*-
"""
author: Rizky Ramadhan

"""

def check_prioritas(prioritas):
    return True if prioritas > 0 and prioritas <= 5 else False


def check_kode_barang(kode_barang):
    return True if len(kode_barang) == 5 else False


def get_data(jumlah):
    daftar_barang = []

    for i in range(jumlah):

        print(f"Barang ke {i + 1} : \n")

        prioritas = int(input("Prioritas\t: "))

        while not check_prioritas(prioritas):
            print("\nPrioritas harus dalam rentang 1 - 5!\n")

            prioritas = int(input("Prioritas\t: "))

        kode_barang = input("Kode Barang\t: ")

        while not check_kode_barang(kode_barang):
            print("\nKode barang harus 3 karakter dan diinputkan dengan spasi!\n")
            kode_barang = input("Kode Barang\t: ")

        diskon = float(input("Diskon\t\t: "))
        harga_barang = int(input("Harga Barang\t: "))

        daftar_barang.append([prioritas, kode_barang, diskon, harga_barang])

        print("")

    return daftar_barang


def check_uang_mencukupi(jumlah_uang, harga_terendah):
    return jumlah_uang >= harga_terendah


def harga_setelah_diskon(harga_barang, diskon):
    return harga_barang - ((diskon / 100) * harga_barang)


jumlah_barang = int(input("Jumlah Barang : "))

daftar_barang = get_data(jumlah_barang)

jumlah_uang = int(input("Jumlah Uang : "))

prioritas_tertinggi = min(list(map(lambda barang: barang[0], daftar_barang)))

barang_berdasarkan_prioritas = list(filter(lambda barang: barang[0] == prioritas_tertinggi, daftar_barang))

harga_terendah = min(list(map(lambda barang: barang[3], barang_berdasarkan_prioritas)))

uang_mencukupi = check_uang_mencukupi(jumlah_uang, harga_terendah)

if uang_mencukupi:
    
    rekomendasi_barang = list(filter(lambda barang: 
                                     (barang[0] == prioritas_tertinggi) and (barang[3] == harga_terendah), 
                                     barang_berdasarkan_prioritas))
    
    print("Rekomendasi barang yang bisa dibeli : \n")
    
    for barang in rekomendasi_barang:
            
            harga_akhir = harga_setelah_diskon(barang[3], barang[2])
            
            print(f"- Direkomendasikan membeli barang dengan kode {barang[1]} seharga Rp {harga_akhir}")
            
else:
    
    print("Uang tidak mencukupi!")
