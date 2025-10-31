import tkinter as tk
from tkinter import messagebox

# ==== Fungsi Hitung Nilai Akhir ====
def hitung_nilai():
    try:
        sikap = float(entry_sikap.get())
        tugas = float(entry_tugas.get())
        uts = float(entry_uts.get())
        uas = float(entry_uas.get())

        total = (sikap * 0.10) + (tugas * 0.30) + (uts * 0.25) + (uas * 0.35)

        if 81 <= total <= 100:
            huruf, bobot = "A", 4
        elif 76 <= total <= 80:
            huruf, bobot = "B+", 3.5
        elif 71 <= total <= 75:
            huruf, bobot = "B", 3
        elif 66 <= total <= 70:
            huruf, bobot = "C+", 2.5
        elif 56 <= total <= 65:
            huruf, bobot = "C", 2
        elif 46 <= total <= 55:
            huruf, bobot = "D", 1
        else:
            huruf, bobot = "E", 0

        keterangan = "Lulus" if total >= 56 else "Tidak Lulus"

        hasil_text.set(
            f"Total Nilai Akhir : {total:.2f}\n"
            f"Nilai Huruf       : {huruf}\n"
            f"Bobot Nilai       : {bobot}\n"
            f"Keterangan        : {keterangan}"
        )
    except ValueError:
        messagebox.showerror("Error", "Input harus berupa angka!")

# ==== Form Nilai Akhir ====
def form_nilai():
    menu.withdraw()  # sembunyikan menu utama
    global entry_sikap, entry_tugas, entry_uts, entry_uas, hasil_text, form

    form = tk.Toplevel()
    form.title("Form Nilai Akhir Akademik")
    form.geometry("400x420")

    tk.Label(form, text="=== FORM NILAI AKADEMIK ===", font=("Arial", 12, "bold")).pack(pady=10)

    tk.Label(form, text="Nilai Sikap/Kehadiran (10%)").pack()
    entry_sikap = tk.Entry(form)
    entry_sikap.pack()

    tk.Label(form, text="Nilai Tugas (30%)").pack()
    entry_tugas = tk.Entry(form)
    entry_tugas.pack()

    tk.Label(form, text="Nilai UTS (25%)").pack()
    entry_uts = tk.Entry(form)
    entry_uts.pack()

    tk.Label(form, text="Nilai UAS (35%)").pack()
    entry_uas = tk.Entry(form)
    entry_uas.pack()

    tk.Button(form, text="Hitung Nilai Akhir", command=hitung_nilai, width=25, bg="green", fg="white").pack(pady=10)

    hasil_text = tk.StringVar()
    tk.Label(form, textvariable=hasil_text, justify="left", fg="blue").pack()


     #as Tombol kembali ke menu utama
    tk.Button(form, text="⬅ Kembali ke Menu Utama", command=lambda: kembali_menu(form), width=25, bg="orange").pack(pady=5)
    # Tombol exit
    tk.Button(form, text="Exit", command=menu.destroy, width=25, bg="red", fg="white").pack(pady=5)

# ==== Kembali ke Menu Utama ====
def kembali_menu(window):
    window.destroy()
    menu.deiconify()

# ==== Menu Utama dengan Desain Button ====
menu = tk.Tk()
menu.title("Menu Utama")
menu.geometry("320x250")

tk.Label(menu, text="=== MENU UTAMA ===", font=("Arial", 14, "bold")).pack(pady=15)

frame_menu = tk.Frame(menu)
frame_menu.pack(pady=10)

btn1 = tk.Button(frame_menu, text="Hitung Nilai Akhir", command=form_nilai, width=25, height=2, bg="#4CAF50", fg="white")
btn1.pack(pady=5)

btn2 = tk.Button(frame_menu, text="Exit", command=menu.destroy, width=25, height=2, bg="#F44336", fg="white")
btn2.pack(pady=5)

menu.mainloop()
