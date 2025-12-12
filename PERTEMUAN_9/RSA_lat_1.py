# ============================
# PROGRAM RSA SEDERHANA
# p = 17, q = 11, e = 7
# ============================

# 1. Nilai awal
p = 17
q = 11
e = 7

# 2. Hitung n dan phi(n)
n = p * q
phi = (p - 1) * (q - 1)

# 3. Mencari nilai d (kunci privat)
def mod_inverse(e, phi):
    for d in range(1, phi):
        if (e * d) % phi == 1:
            return d
    return None

d = mod_inverse(e, phi)

# 4. Fungsi Enkripsi dan Dekripsi
def encrypt(m, e, n):
    return pow(m, e, n)

def decrypt(c, d, n):
    return pow(c, d, n)

# 5. Contoh pesan (plaintext)
m = 88   # Bebas, tetapi harus < n (187)

# 6. Proses enkripsi & dekripsi
cipher = encrypt(m, e, n)
plain  = decrypt(cipher, d, n)

# 7. Tampilkan hasil
print("===== HASIL RSA =====")
print("p =", p)
print("q =", q)
print("e =", e)
print("n =", n)
print("phi(n) =", phi)
print("d =", d)
print("----------------------")
print("Plaintext (m):", m)
print("Ciphertext   :", cipher)
print("Hasil Dekripsi:", plain)
