# untuk menentukan apakah 'number' merupakan bilangan prima / bukan 
# dalam bentuk True / False

def get_prime_number(number):
    
    is_prime = True
    middle_number = number // 2
    
    for i in range(2, (middle_number + 1)):
        if number % i == 0:
            is_prime = False
    
    return is_prime

# untuk menentukan suatu bilangan merupakan palindrome / bukan
# dalam bentuk True / False

def get_palindrome(biner):
    reversed_biner = "".join(list(reversed(biner)))
    return biner == reversed_biner

# untuk menentukan hasil dari karcis tersebut

def check_karcis(is_palindrome, is_prime):
    
    if is_palindrome and is_prime:
        karcis = "Karcis legal dan VIP."
    elif is_palindrome and not is_prime:
        karcis = "Karics legal dan biasa."
    else:
        karcis = "Karcis ilegal."
        
    return karcis

# input ukuran biner dan nomor karcis

ukuran_bit_biner = int(input("Masukkan ukuran bit biner\t: "))
nomor_karcis = int(input("Masukkan nomor karcis\t\t: "))

# konversi nomor karcis menjadi biner

biner_number = "{0:08b}".format(nomor_karcis)

# mendapatkan biner sebanyak ukuran bit yang diinginkan

deserved_biner = biner_number[-ukuran_bit_biner:]

# mendapatkan hasil dari pengecekan palindrome / bukan

is_palindrome = get_palindrome(str(deserved_biner))

# mendapatkan hasil dari pengecekan prime / bukan

is_prime = get_prime_number(nomor_karcis)

# hasil akhir dari karcis yang dicek

result = check_karcis(is_palindrome, is_prime)

# menampilkan hasil

print(f"\nBiner\t: {deserved_biner}")
print(f"Hasil\t: {result}")

