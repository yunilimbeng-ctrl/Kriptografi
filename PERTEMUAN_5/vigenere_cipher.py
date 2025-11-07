class VigenereCipher:
    def __init__(self, key):
        self.key = key.upper()

    def _format_key(self, text):
        """Menyesuaikan panjang kunci dengan teks"""
        key_repeated = ""
        key_index = 0
        for char in text:
            if char.isalpha():
                key_repeated += self.key[key_index % len(self.key)]
                key_index += 1
            else:
                key_repeated += char
        return key_repeated

    def encrypt(self, plaintext):
        """Proses enkripsi Vigenere Cipher"""
        plaintext = plaintext.upper()
        key = self._format_key(plaintext)
        ciphertext = ""
        detail = []

        for p, k in zip(plaintext, key):
            if p.isalpha():
                c = chr(((ord(p) - 65 + ord(k) - 65) % 26) + 65)
                ciphertext += c
                detail.append(f"{p} + {k} -> {c}")
            else:
                ciphertext += p
                detail.append(f"{p} (tidak diubah)")

        print("\n=== DETAIL ENKRIPSI ===")
        for step in detail:
            print(step)
        return ciphertext

    def decrypt(self, ciphertext):
        """Proses dekripsi Vigenere Cipher"""
        ciphertext = ciphertext.upper()
        key = self._format_key(ciphertext)
        plaintext = ""
        detail = []

        for c, k in zip(ciphertext, key):
            if c.isalpha():
                p = chr(((ord(c) - 65 - (ord(k) - 65)) % 26) + 65)
                plaintext += p
                detail.append(f"{c} - {k} -> {p}")
            else:
                plaintext += c
                detail.append(f"{c} (tidak diubah)")

        print("\n=== DETAIL DEKRIPSI ===")
        for step in detail:
            print(step)
        return plaintext

if __name__ == "__main__":
    print("===== PROGRAM VIGENERE CIPHER =====")
    key = input("Masukkan Kunci: ")
    vc = VigenereCipher(key)

    while True:
        print("\n1. Enkripsi")
        print("2. Dekripsi")
        print("3. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            plaintext = input("Masukkan plaintext: ")
            hasil = vc.encrypt(plaintext)
            print(f"\nCiphertext: {hasil}")

        elif pilihan == "2":
            ciphertext = input("Masukkan ciphertext: ")
            hasil = vc.decrypt(ciphertext)
            print(f"\nPlaintext: {hasil}")

        elif pilihan == "3":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid!")
