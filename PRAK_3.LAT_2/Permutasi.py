import math
import itertools
import tkinter as tk
from tkinter import ttk, messagebox

# ===================== FUNGSI PERHITUNGAN =====================

def hitung_menyeluruh():
    try:
        n = int(entry_n1.get())
        hasil = math.factorial(n)
        langkah = f"Rumus: P = n!\nPerhitungan: {n}! = "
        for i in range(n, 0, -1):
            langkah += str(i)
            if i > 1:
                langkah += " × "
        langkah += f" = {hasil}"

        text_hasil1.config(state='normal')
        text_hasil1.delete(1.0, tk.END)
        text_hasil1.insert(tk.END, f"Permutasi Menyeluruh (n!)\n\n{langkah}")
        text_hasil1.config(state='disabled')
    except:
        messagebox.showerror("Error", "Masukkan nilai n yang valid!")


def hitung_sebagian():
    try:
        n = int(entry_n2.get())
        r = int(entry_r2.get())
        if r > n or r < 0:
            raise ValueError
        hasil = math.factorial(n) // math.factorial(n - r)
        langkah = (f"Rumus: P(n, r) = n! / (n - r)!\n"
                   f"Perhitungan:\n{n}! / ({n}-{r})! = "
                   f"{math.factorial(n)} / {math.factorial(n - r)} = {hasil}")

        text_hasil2.config(state='normal')
        text_hasil2.delete(1.0, tk.END)
        text_hasil2.insert(tk.END, f"Permutasi Sebagian P({n},{r})\n\n{langkah}")
        text_hasil2.config(state='disabled')
    except:
        messagebox.showerror("Error", "Masukkan nilai n dan r yang valid! (0 ≤ r ≤ n)")


def hitung_keliling():
    try:
        n = int(entry_n3.get())
        hasil = math.factorial(n - 1) if n > 1 else 1
        langkah = f"Rumus: P_keliling = (n - 1)!\nPerhitungan: ({n} - 1)! = "
        for i in range(n - 1, 0, -1):
            langkah += str(i)
            if i > 1:
                langkah += " × "
        langkah += f" = {hasil}"

        text_hasil3.config(state='normal')
        text_hasil3.delete(1.0, tk.END)
        text_hasil3.insert(tk.END, f"Permutasi Keliling ((n-1)!)\n\n{langkah}")
        text_hasil3.config(state='disabled')
    except:
        messagebox.showerror("Error", "Masukkan nilai n yang valid!")


def hitung_berkelompok():
    try:
        data_input = entry_data4.get().replace(" ", "")
        if not data_input:
            raise ValueError
        data = list(data_input)
        n = len(data)
        hasil_total = math.factorial(n)
        frek = {}
        for item in data:
            frek[item] = frek.get(item, 0) + 1

        penyebut_nilai_math = 1
        penyebut_text = []
        penyebut_nilai = []
        for k, v in frek.items():
            penyebut_text.append(f"{v}! ({k})")
            penyebut_nilai.append(str(math.factorial(v)))
            penyebut_nilai_math *= math.factorial(v)

        hasil_akhir = hasil_total // penyebut_nilai_math
        langkah = (f"Rumus: P = n! / (k1! × k2! × ...)\n\n"
                   f"Data: {data}\nFrekuensi: {frek}\n\n"
                   f"P = {n}! / " + " × ".join(penyebut_text) +
                   f"\n= {math.factorial(n)} / (" + " × ".join(penyebut_nilai) + ")" +
                   f"\n= {math.factorial(n)} / {penyebut_nilai_math}" +
                   f"\n\n➡️ Jumlah Permutasi Berbeda = {hasil_akhir:,}")

        text_hasil4.config(state='normal')
        text_hasil4.delete(1.0, tk.END)
        text_hasil4.insert(tk.END, langkah)
        text_hasil4.config(state='disabled')
    except:
        messagebox.showerror("Error", "Masukkan data huruf/angka dengan benar!")


def hitung_buku_rak():
    try:
        n = int(entry_n5.get())
        r = int(entry_r5.get())
        if n <= 0 or r <= 0:
            raise ValueError
        total = r ** n
        langkah = f"Rumus: Jumlah cara = rⁿ\nPerhitungan: {r}^{n} = {total}\n\n"
        langkah += f"Terdapat {total} cara menempatkan {n} buku di {r} rak.\n\n"

        if n <= 3 and r <= 3:
            buku = [f"B{i+1}" for i in range(n)]
            rak = [f"R{j+1}" for j in range(r)]
            semua = list(itertools.product(rak, repeat=n))
            langkah += "Daftar semua cara:\n"
            for i, susunan in enumerate(semua, start=1):
                pasangan = [f"{buku[k]}→{susunan[k]}" for k in range(n)]
                langkah += f"{i}. " + ", ".join(pasangan) + "\n"

        text_hasil5.config(state='normal')
        text_hasil5.delete(1.0, tk.END)
        text_hasil5.insert(tk.END, langkah)
        text_hasil5.config(state='disabled')
    except:
        messagebox.showerror("Error", "Masukkan nilai n dan r yang valid! (harus > 0)")

# ===================== GUI UTAMA =====================

root = tk.Tk()
root.title("🧮 Kalkulator Permutasi Python")
root.geometry("800x600")
root.configure(bg="#f5f5f5")

judul = tk.Label(root, text="🧮 KALKULATOR PERMUTASI PYTHON", 
                 font=("Arial", 18, "bold"), bg="#f5f5f5", fg="#333")
judul.pack(pady=10)

# Notebook = tab container
notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True, padx=10, pady=10)

# --- TAB 1 ---
tab1 = ttk.Frame(notebook)
notebook.add(tab1, text="Permutasi Menyeluruh")

tk.Label(tab1, text="Masukkan n:", font=("Arial", 11)).pack(pady=5)
entry_n1 = tk.Entry(tab1, width=10)
entry_n1.pack()
tk.Button(tab1, text="Hitung", bg="#4CAF50", fg="white", font=("Arial", 10, "bold"),
          command=hitung_menyeluruh).pack(pady=5)
text_hasil1 = tk.Text(tab1, height=7, width=80, font=("Consolas", 10))
text_hasil1.pack(pady=5)
text_hasil1.config(state='disabled')

# --- TAB 2 ---
tab2 = ttk.Frame(notebook)
notebook.add(tab2, text="Permutasi Sebagian")

frame2 = tk.Frame(tab2)
frame2.pack(pady=5)
tk.Label(frame2, text="n:", font=("Arial", 11)).grid(row=0, column=0, padx=5)
entry_n2 = tk.Entry(frame2, width=10)
entry_n2.grid(row=0, column=1, padx=5)
tk.Label(frame2, text="r:", font=("Arial", 11)).grid(row=0, column=2, padx=5)
entry_r2 = tk.Entry(frame2, width=10)
entry_r2.grid(row=0, column=3, padx=5)
tk.Button(frame2, text="Hitung", bg="#4CAF50", fg="white", font=("Arial", 10, "bold"),
          command=hitung_sebagian).grid(row=0, column=4, padx=5)
text_hasil2 = tk.Text(tab2, height=7, width=80, font=("Consolas", 10))
text_hasil2.pack(pady=5)
text_hasil2.config(state='disabled')

# --- TAB 3 ---
tab3 = ttk.Frame(notebook)
notebook.add(tab3, text="Permutasi Keliling")

tk.Label(tab3, text="Masukkan n:", font=("Arial", 11)).pack(pady=5)
entry_n3 = tk.Entry(tab3, width=10)
entry_n3.pack()
tk.Button(tab3, text="Hitung", bg="#4CAF50", fg="white", font=("Arial", 10, "bold"),
          command=hitung_keliling).pack(pady=5)
text_hasil3 = tk.Text(tab3, height=7, width=80, font=("Consolas", 10))
text_hasil3.pack(pady=5)
text_hasil3.config(state='disabled')

# --- TAB 4 ---
tab4 = ttk.Frame(notebook)
notebook.add(tab4, text="Permutasi Berkelompok")

tk.Label(tab4, text="Masukkan Data (contoh: AABBC):", font=("Arial", 11)).pack(pady=5)
entry_data4 = tk.Entry(tab4, width=20)
entry_data4.pack()
tk.Button(tab4, text="Hitung", bg="#4CAF50", fg="white", font=("Arial", 10, "bold"),
          command=hitung_berkelompok).pack(pady=5)
text_hasil4 = tk.Text(tab4, height=8, width=80, font=("Consolas", 10))
text_hasil4.pack(pady=5)
text_hasil4.config(state='disabled')

# --- TAB 5 ---
tab5 = ttk.Frame(notebook)
notebook.add(tab5, text="Buku di Rak")

frame5 = tk.Frame(tab5)
frame5.pack(pady=5)
tk.Label(frame5, text="Jumlah buku (n):", font=("Arial", 11)).grid(row=0, column=0, padx=5)
entry_n5 = tk.Entry(frame5, width=10)
entry_n5.grid(row=0, column=1, padx=5)
tk.Label(frame5, text="Jumlah rak (r):", font=("Arial", 11)).grid(row=0, column=2, padx=5)
entry_r5 = tk.Entry(frame5, width=10)
entry_r5.grid(row=0, column=3, padx=5)
tk.Button(frame5, text="Hitung", bg="#4CAF50", fg="white", font=("Arial", 10, "bold"),
          command=hitung_buku_rak).grid(row=0, column=4, padx=5)
text_hasil5 = tk.Text(tab5, height=8, width=85, font=("Consolas", 10))
text_hasil5.pack(pady=5)
text_hasil5.config(state='disabled')

root.mainloop()
