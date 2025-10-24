# Kalkulator Hybrid

def kalkulator_hybrid():
    print("=== Kalkulator Hybrid ===")
    ekspresi = input("Masukkan ekspresi matematika: ")

    try:
        # Hilangkan spasi agar bisa memproses input tanpa spasi juga
        ekspresi = ekspresi.replace(" ", "")
        
        # Evaluasi ekspresi matematika
        hasil = eval(ekspresi)
        
        print("Output >", hasil)
    except Exception as e:
        print("Terjadi kesalahan dalam perhitungan:", e)


# Jalankan program
if __name__ == "__main__":
    kalkulator_hybrid()
