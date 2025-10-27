# Konversi Biner ke Desimal dan Hexadesimal
print("=== Konversi Bilangan Biner ===")
biner = input("Masukkan bilangan biner: ")

# Konversi
desimal = int(biner, 2)
hexadesimal = hex(desimal)

# Output
print(f"Bilangan Desimal: {desimal}")
print(f"Bilangan Hexadesimal: {hexadesimal[2:].upper()}")
