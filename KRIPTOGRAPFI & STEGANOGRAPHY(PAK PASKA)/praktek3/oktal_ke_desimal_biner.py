# Konversi Oktal ke Desimal, Biner, dan Hexadesimal
print("\n=== Konversi Bilangan Oktal ===")
oktal = input("Masukkan bilangan oktal: ")

# Konversi
desimal = int(oktal, 8)
biner = bin(desimal)
hexadesimal = hex(desimal)

# Output
print(f"Bilangan Desimal: {desimal}")
print(f"Bilangan Biner: {biner[2:]}")
print(f"Bilangan Hexadesimal: {hexadesimal[2:].upper()}")
