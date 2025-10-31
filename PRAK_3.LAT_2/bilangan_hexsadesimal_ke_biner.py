# Konversi Hexadesimal ke Desimal, Biner, dan Oktal
print("\n=== Konversi Bilangan Hexadesimal ===")
hexa = input("Masukkan bilangan hexadesimal: ")

# Konversi
desimal = int(hexa, 16)
biner = bin(desimal)
oktal = oct(desimal)

# Output
print(f"Bilangan Desimal: {desimal}")
print(f"Bilangan Biner: {biner[2:]}")
print(f"Bilangan Oktal: {oktal[2:]}")
