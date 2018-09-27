from functools import reduce

def tidak_mengandung_2_atau_6(nilai):
    return False if "2" in str(nilai) or "6" in str(nilai) else True

def get_total_number(nilai):
    number_instring = list(str(nilai))
    number_integer = list(map(int, number_instring))
    return reduce(lambda x, y: x + y, number_integer)

def generete_number(nilai, default_number):
    return False if get_total_number(nilai) == default_number else True

def get_result(perulangan):
    total = 0

    for i in range(1, (perulangan + 1)):
        if i < 10:
            if tidak_mengandung_2_atau_6(i):
                print(i, end=" ")
                total += i
        if i >= 10 and i < 100:
            if generete_number(i, 9) and tidak_mengandung_2_atau_6(i):
                print(i, end=" ")
                total += i
        if i >= 100 and i < 1000:
            if generete_number(i, 20) and tidak_mengandung_2_atau_6(i):
                print(i, end=" ")
                total += i
        if i >= 1000 and i < 10000:
            if generete_number(i, 18) and tidak_mengandung_2_atau_6(i):
                print(i, end=" ")
                total += i

    return total
    
perulangan = int(input("Masukkan 'n' kali perulangan : "))
print("")

result = get_result(perulangan)

print("")
print(f"\nTotal : {result}")

