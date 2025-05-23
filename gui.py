import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

# Üçgen üyelik fonksiyonu
def triangular(x, a, b, c):
    return np.maximum(np.minimum((x - a) / (b - a + 1e-6), (c - x) / (c - b + 1e-6)), 0)

# Örnek fuzzy hesaplama fonksiyonu
def hesapla_fuzzy(uyku, uyanma, gurultu, gun, is_miktari):
    alarm = (uyku * 2 + uyanma * 3 + gurultu * 0.5 + is_miktari) % 100
    muzik = (100 - alarm + gun * 10) % 100
    return alarm, muzik

# Hesapla ve grafikleri çiz
def hesapla():
    try:
        uyku = float(uyku_entry.get())
        uyanma = uyanma_slider.get()
        gurultu = gurultu_slider.get()
        gun_text = gun_combobox.get()
        is_miktari = is_slider.get()

        gun_dict = {"Hafta içi": 0, "Cumartesi": 1, "Pazar": 2}
        gun = gun_dict[gun_text]

        alarm, muzik = hesapla_fuzzy(uyku, uyanma, gurultu, gun, is_miktari)

        verbal_output = f"Alarm Şiddeti: {alarm:.2f}\nMüzik Şiddeti: {muzik:.2f}"
        sonuc_label.config(text=verbal_output)

        for frame in [grafik_bar_frame, grafik_alarm_frame, grafik_muzik_frame]:
            for widget in frame.winfo_children():
                widget.destroy()

        # Bar grafik
        fig_bar, ax_bar = plt.subplots(figsize=(4, 3))
        ax_bar.bar(['Alarm Şiddeti', 'Müzik Şiddeti'], [alarm, muzik], color=['skyblue', 'lightcoral'])
        ax_bar.set_ylim(0, 100)
        ax_bar.set_title("Alarm ve Müzik Şiddeti")
        ax_bar.set_ylabel("Değer")
        canvas_bar = FigureCanvasTkAgg(fig_bar, master=grafik_bar_frame)
        canvas_bar.draw()
        canvas_bar.get_tk_widget().pack()

        # Alarm üyelik fonksiyonları
        x = np.linspace(0, 100, 500)
        tri_dusuk = triangular(x, 0, 0, 50)
        tri_orta = triangular(x, 25, 50, 75)
        tri_yuksek = triangular(x, 50, 100, 100)

        fig_alarm, ax_alarm = plt.subplots(figsize=(4, 3))
        ax_alarm.plot(x, tri_dusuk, label="Sessiz", color="blue")
        ax_alarm.plot(x, tri_orta, label="Orta", color="green")
        ax_alarm.plot(x, tri_yuksek, label="Gürültülü", color="red")
        ax_alarm.set_title("Alarm Üyelik Fonksiyonları")
        ax_alarm.set_xlabel("Değer")
        ax_alarm.set_ylabel("Üyelik")
        ax_alarm.legend()
        canvas_alarm = FigureCanvasTkAgg(fig_alarm, master=grafik_alarm_frame)
        canvas_alarm.draw()
        canvas_alarm.get_tk_widget().pack()

        # Müzik üyelik fonksiyonları
        tri_dusuk_m = triangular(x, 0, 10, 40)
        tri_orta_m = triangular(x, 30, 50, 70)
        tri_yuksek_m = triangular(x, 60, 90, 100)

        fig_muzik, ax_muzik = plt.subplots(figsize=(4, 3))
        ax_muzik.plot(x, tri_dusuk_m, label="Rahatlatıcı", color="blue")
        ax_muzik.plot(x, tri_orta_m, label="Normal", color="green")
        ax_muzik.plot(x, tri_yuksek_m, label="Enerjik", color="red")
        ax_muzik.set_title("Müzik Üyelik Fonksiyonları")
        ax_muzik.set_xlabel("Değer")
        ax_muzik.set_ylabel("Üyelik")
        ax_muzik.legend()
        canvas_muzik = FigureCanvasTkAgg(fig_muzik, master=grafik_muzik_frame)
        canvas_muzik.draw()
        canvas_muzik.get_tk_widget().pack()

    except Exception as e:
        sonuc_label.config(text=f"Hata: {str(e)}")

# Ana pencere
pencere = tk.Tk()
pencere.title("Alarm Sistemi")
pencere.geometry("1100x650")
pencere.resizable(False, False)

# Sol input alanı
input_frame = tk.Frame(pencere)
input_frame.pack(side="left", fill="y", padx=10, pady=10)

tk.Label(input_frame, text="Uyku (saat):").pack(pady=2)
uyku_entry = tk.Entry(input_frame)
uyku_entry.pack(pady=2)

tk.Label(input_frame, text="Uyanma süresi (dk):").pack(pady=2)
uyanma_slider = tk.Scale(input_frame, from_=0, to=30, orient=tk.HORIZONTAL)
uyanma_slider.pack(pady=2)

tk.Label(input_frame, text="Gürültü seviyesi:").pack(pady=2)
gurultu_slider = tk.Scale(input_frame, from_=0, to=100, orient=tk.HORIZONTAL)
gurultu_slider.pack(pady=2)

tk.Label(input_frame, text="Gün:").pack(pady=2)
gun_combobox = ttk.Combobox(input_frame, values=["Hafta içi", "Cumartesi", "Pazar"])
gun_combobox.pack(pady=2)
gun_combobox.current(0)

tk.Label(input_frame, text="İş miktarı:").pack(pady=2)
is_slider = tk.Scale(input_frame, from_=0, to=100, orient=tk.HORIZONTAL)
is_slider.pack(pady=2)

hesapla_button = tk.Button(input_frame, text="HESAPLA", command=hesapla, font=("Arial", 12, "bold"),
                           height=2, width=15, bg="#4CAF50", fg="white")
hesapla_button.pack(pady=10)

sonuc_label = tk.Label(input_frame, text="", font=("Arial", 11), justify="left", anchor="w")
sonuc_label.pack(pady=10)

# Sağ grafik alanları
right_frame = tk.Frame(pencere)
right_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

# Çubuk grafik üstte
grafik_bar_frame = tk.LabelFrame(right_frame, text="Alarm ve Müzik Şiddeti (Bar Grafik)", padx=5, pady=5)
grafik_bar_frame.pack(fill="x", expand=False, pady=5)

# Sekmeli yapı
notebook = ttk.Notebook(right_frame)
notebook.pack(fill="both", expand=True)

grafik_alarm_frame = tk.Frame(notebook)
grafik_muzik_frame = tk.Frame(notebook)

notebook.add(grafik_alarm_frame, text="Alarm Fonksiyonları")
notebook.add(grafik_muzik_frame, text="Müzik Fonksiyonları")

pencere.mainloop()
