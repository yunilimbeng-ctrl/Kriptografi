print("=== Program Logika Kombinasi IF, Aritmatika, dan Logika ===")

# Input nilai dari pengguna
x = int(input("Masukkan nilai x: "))
y = int(input("Masukkan nilai y: "))
z = int(input("Masukkan nilai z: "))

# Logika 1
if x >= 18 and x <= 30:
    print("x berada di antara 18 dan 30")
else:
    print("x tidak berada di antara 18 dan 30")

# Logika 2
if y < 10 or y > 20:
    print("y berada di luar rentang 10 hingga 20")
else:
    print("y berada di dalam rentang 10 hingga 20")

# Logika 3
if z == 5:
    print("z sama dengan 5")
else:
    print("z tidak sama dengan 5")

# Logika 4
if x != y:
    print("x tidak sama dengan y")
else:
    print("x sama dengan y")

# Logika 5
if x > y:
    print("x lebih besar dari y")
else:
    print("x tidak lebih besar dari y")

# Logika 6
if z < y:
    print("z lebih kecil dari y")
else:
    print("z tidak lebih kecil dari y")

# Logika 7
if y >= 15 and z <= 5:
    print("y lebih besar atau sama dengan 15, dan z lebih kecil atau sama dengan 5")
else:
    print("Salah satu kondisi tidak terpenuhi (y < 15 atau z > 5)")

print("\n=== Program selesai. Terima kasih! ===")
