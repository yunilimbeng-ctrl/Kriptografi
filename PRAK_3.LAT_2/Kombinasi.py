import tkinter as tk
from tkinter import messagebox
from itertools import combinations

# Fungsi faktorial
def faktorial(x):
    if x == 0 or x == 1:
        return 1
    hasil = 1
    for i in range(2, x + 1):
        hasil *= i
    return hasil

# Fungsi kombinasi (menghitung jumlah)
def kombinasi(n, r):
    if r > n:
        return 0
    return faktorial(n) // (faktorial(r) * faktorial(n - r))

# Fungsi untuk menampilkan semua kombinasi dari daftar objek
def tampilkan_kombinasi(objek, r):
    semua_kombinasi = list(combinations(objek, r))
    return ["".join(k) for k in semua_kombinasi]

# Fungsi dijalankan saat tombol klik
def hitung():
    try:
        n = int(entry_n.get())
        r = int(entry_r.get())
        if n <= 0 or r <= 0:
            messagebox.showerror("Error", "Masukkan angka positif!")
            return
        if r > n:
            messagebox.showerror("Error", "r tidak boleh lebih besar dari n!")
            return
        
        # Buat daftar huruf
        objek = [chr(65 + i) for i in range(n)]
        
        # Hitung jumlah kombinasi
        jumlah = kombinasi(n, r)
        
        # Tampilkan daftar kombinasi
        list_kombinasi = tampilkan_kombinasi(objek, r)
        
        # Update label dan text widget
        label_objek.config(text=f"Objek tersedia: {', '.join(objek)}")
        label_hasil.config(text=f"Jumlah kombinasi C({n}, {r}) = {jumlah}")
        text_kombinasi.delete("1.0", tk.END)
        for k in list_kombinasi:
            text_kombinasi.insert(tk.END, k + "\n")
        
    except ValueError:
        messagebox.showerror("Error", "Masukkan angka valid!")

# Membuat window utama
root = tk.Tk()
root.title("Kombinasi Huruf")
root.geometry("450x550")
root.configure(bg="#e6f2ff")  # Background biru muda

# Judul
tk.Label(root, text="KALKULATOR KOMBINASI HURUF", bg="#e6f2ff",
         font=("Arial", 14, "bold")).pack(pady=10)

# Input n
tk.Label(root, text="Jumlah total objek (n):", bg="#e6f2ff", font=("Arial", 12)).pack(pady=5)
entry_n = tk.Entry(root, font=("Arial", 12))
entry_n.pack(pady=5)

# Input r
tk.Label(root, text="Jumlah objek yang dipilih (r):", bg="#e6f2ff", font=("Arial", 12)).pack(pady=5)
entry_r = tk.Entry(root, font=("Arial", 12))
entry_r.pack(pady=5)

# Tombol hitung
tk.Button(root, text="Hitung Kombinasi", command=hitung, bg="#4caf50", fg="white",
          font=("Arial", 12), padx=10, pady=5).pack(pady=10)

# Label untuk objek tersedia
label_objek = tk.Label(root, text="", bg="#e6f2ff", font=("Arial", 12))
label_objek.pack(pady=5)

# Label untuk hasil kombinasi
label_hasil = tk.Label(root, text="", bg="#e6f2ff", font=("Arial", 12, "bold"))
label_hasil.pack(pady=5)

# Text widget untuk menampilkan kombinasi
text_kombinasi = tk.Text(root, width=35, height=15, font=("Arial", 12))
text_kombinasi.pack(pady=10)

# Scrollbar untuk text widget
scroll = tk.Scrollbar(root, command=text_kombinasi.yview)
text_kombinasi.configure(yscrollcommand=scroll.set)
scroll.pack(side=tk.RIGHT, fill=tk.Y)

# Jalankan aplikasi
root.mainloop()
