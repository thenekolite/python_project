# -*- coding: utf-8 -*-
"""
author: Rizky Ramadhan

"""

# copy, agar nilai dict tidak berubah
import copy 


# untuk menentukan nilai priority yang diinputkan valid atau tidak 
def is_valid_priority(priority):
    
    return True if priority > 0 and priority <= 5 else False


# untuk menentukan code yang diinputkan valid atau tidak 
def is_valid_code(code):
    
    return True if len(code) == 5 else False


# untuk mendapatkan data yang akan digunakan 
def get_all_data(total_pakaian):
    
    daftar_pakaian = {}
    
    for i in range(0, total_pakaian):
        
        prioritas = int(input("Prioritas\t: "))
        
        while not is_valid_priority(prioritas):
            print("\nPrioritas harus > 0 and <= 5!\n")
            prioritas = int(input("Prioritas\t: "))
        
        kode_pakaian = input("Kode Pakaian\t: ")
        
        while not is_valid_code(kode_pakaian):
            print("\nKode pakaian harus 3 karakter dengan spasi!\n")
            kode_pakaian = input("Kode Pakaian\t: ")
        
        diskon = float(input("Diskon\t\t: "))
        harga_pakaian = int(input("Harga\t\t: "))
        
        print()
        
        daftar_pakaian["Pakaian " + str(i)] = [prioritas, kode_pakaian, diskon, harga_pakaian]
        
    return daftar_pakaian


# input total pakaian 
total_pakaian = int(input("Total pakaian : "))


# daftar pakaian yang diinputkan
daftar_pakaian = get_all_data(total_pakaian)


# jumlah uang 
jumlah_uang = int(input("Jumlah uang : "))


# daftar barang yang bisa dibeli dengan jumlah uang yang dimiliki.
def get_afford_stuff(jumlah_uang, daftar_pakaian):
    
    all_stuff = copy.deepcopy(daftar_pakaian)
    afford_stuff = {}
    
    for key in all_stuff.keys():
        
        if jumlah_uang >= all_stuff[key][3]:
            
            key_number = "".join(key.split()[1:])
            
            afford_stuff["Pakaian" + str(key_number)] = all_stuff[key]
    
    return afford_stuff


all_afford_stuff = get_afford_stuff(jumlah_uang, daftar_pakaian)


# untuk menentukan apakah all_afford_stuff kosong atau tidak
def is_all_afford_stuff_empty(all_afford_stuff):
    
    return bool(all_afford_stuff)


is_data_empty = is_all_afford_stuff_empty(all_afford_stuff)


# untuk mendapatkan nilai prioritas tertinggi
def get_max_priority(all_afford_stuff):
    
    if is_data_empty:
    
        daftar_nilai_prioritas = []

        for key in all_afford_stuff.keys():
    
            daftar_nilai_prioritas.append(all_afford_stuff[key][0])
        
        return min(daftar_nilai_prioritas)

priority_max = get_max_priority(all_afford_stuff)


# untuk mendapatkan pakaian yang sesuai dengan prioritas
def get_data_based_on_priority(priority_max, all_afford_stuff):
    
    if is_data_empty:
        
        recommended = []
    
        for key in all_afford_stuff.keys():
        
            if all_afford_stuff[key][0] == priority_max:
            
                recommended.append(all_afford_stuff[key])
            
        return recommended
    
data_based_on_priority = get_data_based_on_priority(priority_max, all_afford_stuff)


# untuk mendapatkan harga paling murah
def get_min_price(data_based_on_priority):
    
    if is_data_empty:
        
        daftar_harga = []
    
        for i in range(0, len(data_based_on_priority)):

            daftar_harga.append(data_based_on_priority[i][3])

        return min(daftar_harga)
    
    
harga_minimum = get_min_price(data_based_on_priority)


# untuk mendapatkan daftar rekomendasi berdasarkan harga minimum
def get_rekomendasi(data_based_on_priority, harga_minimum):
    
    if is_data_empty:
        
        rekomendasi = []
    
        for i in range(0, len(data_based_on_priority)):

            if data_based_on_priority[i][3] == harga_minimum:

                rekomendasi.append(data_based_on_priority[i])

        return rekomendasi
    
    
# menampilkan hasil    
def show_result(data_based_on_priority, harga_minimum):
    
    if is_data_empty:
        
        rekomendasi = get_rekomendasi(data_based_on_priority, harga_minimum)

        print("\nDaftar rekomendasi barang yang bisa dibeli : \n")

        for i in range(0, len(rekomendasi)):

            diskon = (rekomendasi[i][2] / 100) * rekomendasi[i][3]
            real_harga = rekomendasi[i][3] - diskon

            print(f"Direkomendasikan membeli barang dengan kode '{rekomendasi[i][1]}' seharga {real_harga}")
            
    else:
        
        print("\nTidak ada yang cocok!")
        
        
# menampilkan hasil
show_result(data_based_on_priority, harga_minimum)
