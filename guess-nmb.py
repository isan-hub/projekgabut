import random
print ("Tebak Angka!")
angka_rahasia = random.randint(1, 50)
percobaan = 0

while True:
    tebakan = int(input("Tebak Angka (1-50) : "))
    percobaan += 1

    if tebakan < angka_rahasia:
        print("Terlalu kecil!")
    elif tebakan > angka_rahasia:
        print("Terlalu besar!")
    else:
        print(f"Selamat! Kamu menebak dengan benar dalam {percobaan} percobaan.")
        