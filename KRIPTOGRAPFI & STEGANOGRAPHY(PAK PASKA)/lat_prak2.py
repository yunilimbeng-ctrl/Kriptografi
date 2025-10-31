import operator

# Dictionary operator aritmatika
ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
}

print("=== Program Kalkulator Sederhana ===")

while input("Apakah Anda ingin memulai operasi perhitungan? (y/n): ").lower() == 'y':
    a = float(input("Masukkan nilai a: "))
    b = float(input("Masukkan nilai b: "))
    c = input("Masukkan operator (+, -, *, /): ")

    try:
        hasil = ops[c](a, b)
        print(f"Hasil dari {a} {c} {b} = {hasil}")
    except KeyError:
        print("Operator tidak valid.")
    except ZeroDivisionError:
        print("Pembagian dengan nol tidak diperbolehkan.")

print("Program selesai. Terima kasih!")
