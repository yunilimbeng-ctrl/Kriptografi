# Program: Substitusi Cipher Dinamis
# Praktikum Kriptografi Klasik
# Paska Marto Hasugian, M.Kom

def substitusi_cipher(plaintext, aturan):
    ciphertext = ''
    # Proses substitusi untuk setiap karakter di plaintext
    for char in plaintext.upper():
        if char in aturan:
            ciphertext += aturan[char]   # Ganti huruf sesuai aturan
        else:
            ciphertext += char           # Jika tidak ada di aturan, biarkan
    return ciphertext


# === Bagian utama program ===
print("=== Program Substitusi Cipher Dinamis ===")

# Input plaintext dari user
plaintext = input("Masukkan plaintext: ").upper()

# Input jumlah aturan substitusi
jumlah = int(input("Berapa banyak aturan substitusi yang ingin dimasukkan? "))

# Buat dictionary kosong untuk aturan substitusi
aturan_substitusi = {}

# Input aturan substitusi dari user
print("\nMasukkan aturan substitusi (contoh: U diganti jadi K):")
for i in range(jumlah):
    huruf_asli = input(f"  Huruf asli ke-{i+1}: ").upper()
    huruf_ganti = input(f"  Diganti menjadi : ").upper()
    aturan_substitusi[huruf_asli] = huruf_ganti

# Tampilkan aturan yang sudah dibuat
print("\nAturan substitusi yang digunakan:")
for k, v in aturan_substitusi.items():
    print(f"  {k} → {v}")

# Proses enkripsi
ciphertext = substitusi_cipher(plaintext, aturan_substitusi)

# Tampilkan hasil
print("\n=== HASIL ENKRIPSI ===")
print(f"Plaintext : {plaintext}")
print(f"Ciphertext: {ciphertext}")
