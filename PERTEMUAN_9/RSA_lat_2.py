import tkinter as tk
from tkinter import scrolledtext
import secrets
import math


# ============================================
# Fungsi Util RSA
# ============================================
def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    r = int(math.isqrt(n))
    for i in range(3, r + 1, 2):
        if n % i == 0:
            return False
    return True

def list_primes_in_range(a: int, b: int):
    return [x for x in range(a, b + 1) if is_prime(x)]

def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return abs(a)

def egcd(a: int, b: int):
    if b == 0:
        return (a, 1, 0)
    g, x1, y1 = egcd(b, a % b)
    return (g, y1, x1 - (a//b)*y1)

def modinv(e: int, phi: int):
    g, x, y = egcd(e, phi)
    if g != 1:
        return None
    return x % phi

def max_bytes_for_n(n_val: int) -> int:
    bits = n_val.bit_length()
    b = max((bits - 1) // 8, 1)
    return b

def split_bytes(data: bytes, block_size: int):
    return [data[i:i+block_size] for i in range(0, len(data), block_size)]


# ============================================
# GUI LOGIC
# ============================================
class RSAForm:
    def __init__(self, root):
        self.root = root
        root.title("RSA Random Prime - Form")

        # =============================
        # AREA INPUT
        # =============================
        tk.Label(root, text="Masukkan Plaintext:").pack()
        self.input_text = tk.Entry(root, width=50)
        self.input_text.pack()

        tk.Button(root, text="Generate Key Acak", command=self.generate_keys).pack(pady=5)
        tk.Button(root, text="Enkripsi", command=self.encrypt_text).pack(pady=5)
        tk.Button(root, text="Dekripsi", command=self.decrypt_text).pack(pady=5)

        # =============================
        # AREA OUTPUT
        # =============================
        tk.Label(root, text="Output Debug:").pack()
        self.output = scrolledtext.ScrolledText(root, width=80, height=25)
        self.output.pack()

        # Storage
        self.p = None
        self.q = None
        self.e = None
        self.d = None
        self.n = None
        self.phi = None
        self.cipher_blocks = None
        self.blocks = None

    # --------------------------------------------
    # GENERATE RANDOM KEY
    # --------------------------------------------
    def generate_keys(self):
        PRIME_MIN = 50
        PRIME_MAX = 200

        primes = list_primes_in_range(PRIME_MIN, PRIME_MAX)

        self.p = secrets.choice(primes)
        self.q = secrets.choice(primes)
        while self.q == self.p:
            self.q = secrets.choice(primes)

        self.n = self.p * self.q
        self.phi = (self.p - 1) * (self.q - 1)

        candidates = list(range(3, min(self.phi, 1000), 2))
        secrets.SystemRandom().shuffle(candidates)

        for cand in candidates:
            if gcd(cand, self.phi) == 1:
                self.e = cand
                break

        self.d = modinv(self.e, self.phi)

        self.output.delete(1.0, tk.END)
        self.output.insert(tk.END, "===== RSA Key Generated =====\n")
        self.output.insert(tk.END, f"p = {self.p}\n")
        self.output.insert(tk.END, f"q = {self.q}\n")
        self.output.insert(tk.END, f"n = {self.n}\n")
        self.output.insert(tk.END, f"phi = {self.phi}\n")
        self.output.insert(tk.END, f"e = {self.e}\n")
        self.output.insert(tk.END, f"d = {self.d}\n")
        self.output.insert(tk.END, "=============================\n")

    # --------------------------------------------
    # ENCRYPT TEXT
    # --------------------------------------------
    def encrypt_text(self):
        if not self.e:
            self.output.insert(tk.END, "\n[!] Generate key dulu!\n")
            return

        text = self.input_text.get()
        data = text.encode("utf-8")

        max_b = max_bytes_for_n(self.n)
        self.blocks = split_bytes(data, max_b)

        cipher = []
        self.output.insert(tk.END, "\n===== ENKRIPSI =====\n")

        for i, blk in enumerate(self.blocks, start=1):
            m_int = int.from_bytes(blk, "big")
            c_int = pow(m_int, self.e, self.n)
            cipher.append(c_int)
            self.output.insert(tk.END, f"Blok {i}: {blk} -> {m_int} -> {c_int}\n")

        self.cipher_blocks = cipher
        self.output.insert(tk.END, f"\nCiphertext: {cipher}\n")
        self.output.insert(tk.END, "=====================\n")

    # --------------------------------------------
    # DECRYPT
    # --------------------------------------------
    def decrypt_text(self):
        if not self.cipher_blocks:
            self.output.insert(tk.END, "\n[!] Tidak ada ciphertext!\n")
            return

        result_bytes = bytearray()
        self.output.insert(tk.END, "\n===== DEKRIPSI =====\n")

        for i, c in enumerate(self.cipher_blocks, start=1):
            m2 = pow(c, self.d, self.n)
            orig_len = len(self.blocks[i-1])
            blk_bytes = m2.to_bytes(orig_len, "big")
            result_bytes.extend(blk_bytes)
            self.output.insert(tk.END, f"Blok {i}: {c} -> {m2} -> {blk_bytes}\n")

        hasil = result_bytes.decode("utf-8")

        # --- tambahan output lengkap ---
        self.output.insert(tk.END, "\n===== HASIL DEKRIPSI LENGKAP =====\n")
        self.output.insert(tk.END, f"Ciphertext : {self.cipher_blocks}\n")
        self.output.insert(tk.END, f"n          : {self.n}\n")
        self.output.insert(tk.END, f"e          : {self.e}\n")
        self.output.insert(tk.END, f"d          : {self.d}\n")
        self.output.insert(tk.END, f"Plaintext  : {hasil}\n")
        self.output.insert(tk.END, "===================================\n")


# ============================================
# RUN PROGRAM GUI
# ============================================
root = tk.Tk()
app = RSAForm(root)
root.mainloop()
