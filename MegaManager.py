import tkinter as tk
from tkinter import ttk


def calculate(event=None):
    try:
        plo = float(plo_entry.get().replace(",", "."))
        truba = plo * 10
        kontur = truba / 80
        truba2 = plo * 6.7
        kontur2 = truba2 / 80
        truba3 = plo * 5
        kontur3 = truba3 / 80
        truba_label.config(text="Метраж трубы: {:.1f} (шаг трубы через 10см)".format(truba))
        kontur_label.config(text="Количество контуров: {:.1f} (рекомендуемая длина контура 80м)".format(kontur))
        truba2_label.config(text="Метраж трубы: {:.1f} (шаг трубы через 15см)".format(truba2))
        kontur2_label.config(text="Количество контуров: {:.1f} (рекомендуемая длина контура 80м)".format(kontur2))
        truba3_label.config(text="Метраж трубы: {:.1f} (шаг трубы через 20см)".format(truba3))
        kontur3_label.config(text="Количество контуров: {:.1f} (рекомендуемая длина контура 80м)".format(kontur3))
    except ValueError:
        truba_label.config(text="Некорректный ввод")
        kontur_label.config(text="")
        truba2_label.config(text="")
        kontur2_label.config(text="")
        truba3_label.config(text="")
        kontur3_label.config(text="")


def calculate2(event=None):
    try:
        plo2 = float(plo2_entry.get().replace(",", "."))
        radiator1 = plo2 * 100 / 191
        radiator11 = plo2 * 120 / 191
        radiator1_label.config(text="Количество секций: {:.1f} (для квартиры)".format(radiator1))
        radiator11_label.config(text="Количество секций: {:.1f} (для дома)".format(radiator11))
    except ValueError:
        radiator1_label.config(text="Некорректный ввод")
        radiator11_label.config(text="")


def calculate3(event=None):
    try:
        plo3 = float(plo3_entry.get().replace(",", "."))
        radiator2 = plo3 * 100 / 137
        radiator22 = plo3 * 120 / 137
        radiator2_label.config(text="Количество секций: {:.1f} (для квартиры)".format(radiator2))
        radiator22_label.config(text="Количество секций: {:.1f} (для дома)".format(radiator22))
    except ValueError:
        radiator2_label.config(text="Некорректный ввод")
        radiator22_label.config(text="")


def calculate4(event=None):
    try:
        plo4 = float(plo4_entry.get().replace(",", "."))
        radiator3 = plo4 * 100 / 258
        radiator33 = plo4 * 120 / 258
        radiator3_label.config(text="Количество секций: {:.1f} (для квартиры)".format(radiator3))
        radiator33_label.config(text="Количество секций: {:.1f} (для дома)".format(radiator33))
    except ValueError:
        radiator3_label.config(text="Некорректный ввод")
        radiator33_label.config(text="")


def calculate5(event=None):
    try:
        plo5 = float(plo5_entry.get().replace(",", "."))
        radiator4 = plo5 * 100 / 182
        radiator44 = plo5 * 120 / 182
        radiator4_label.config(text="Количество секций: {:.1f} (для квартиры)".format(radiator4))
        radiator44_label.config(text="Количество секций: {:.1f} (для дома)".format(radiator44))
    except ValueError:
        radiator4_label.config(text="Некорректный ввод")
        radiator44_label.config(text="")


def calculate6(event=None):
    try:
        age = float(age_entry.get().replace(",", "."))
        mars = age / 1.8808476
        mars_label.config(text="Тебе: {:.1f} марсианских солов (лет)".format(mars))
    except ValueError:
        mars_label.config(text="Некорректный ввод")


def calculate7(event=None):
    try:
        d1 = float(d1_entry.get().replace(",", "."))
        h1 = float(h1_entry.get().replace(",", "."))
        Pi = 3.1415926535
        r = h1 * Pi * d1 ** 2 / 4
        v = r / 1000
        v_label.config(text="Объём равен: {:.3f} лит.".format(v))
    except ValueError:
        v_label.config(text="Некорретный ввод")



root = tk.Tk()
root.title("Супер менеджер")
root.geometry("700x450")

notebook = ttk.Notebook(root)
notebook.pack(fill='both', expand=True)

page_1 = ttk.Frame(notebook)
notebook.add(page_1, text="Теплый пол")

page_2 = ttk.Frame(notebook)
notebook.add(page_2, text="Радиаторы Fondital")

page_4 = ttk.Frame(notebook)
notebook.add(page_4, text="Объём")

page_5 = ttk.Frame(notebook)
notebook.add(page_5, text="Марс")

plo_label = tk.Label(page_1, text="Расчет теплого пола "
                                  "\nУкажите площадь:", justify="left", font=("Calibri", 10, "bold"))
plo_entry = tk.Entry(page_1)
truba_label = tk.Label(page_1)
kontur_label = tk.Label(page_1)
truba2_label = tk.Label(page_1)
kontur2_label = tk.Label(page_1)
truba3_label = tk.Label(page_1)
kontur3_label = tk.Label(page_1)

plo2_label = tk.Label(page_2, text="Радиатор Fondital Calidor Super B4 500/100 191 Вт "
                                   "\nУкажите площадь:", justify="left", font=("Calibri", 10, "bold"))
plo2_entry = tk.Entry(page_2)
radiator1_label = tk.Label(page_2)
radiator11_label = tk.Label(page_2)

plo3_label = tk.Label(page_2, text="Радиатор Fondital Calidor Super B4 350/100 137 Вт "
                                   "\nУкажите площадь:", justify="left", font=("Calibri", 10, "bold"))
plo3_entry = tk.Entry(page_2)
radiator2_label = tk.Label(page_2)
radiator22_label = tk.Label(page_2)

plo4_label = tk.Label(page_2, text="Радиатор Fondital EXCLUSIVO B3 800/100, 258 Вт "
                                   "\nУкажите площадь:", justify="left", font=("Calibri", 10, "bold"))
plo4_entry = tk.Entry(page_2)
radiator3_label = tk.Label(page_2)
radiator33_label = tk.Label(page_2)

plo5_label = tk.Label(page_2, text="Радиатор Fondital ALUSTAL 500/100  182 Вт "
                                   "\nУкажите площадь:", justify="left", font=("Calibri", 10, "bold"))
plo5_entry = tk.Entry(page_2)
radiator4_label = tk.Label(page_2)
radiator44_label = tk.Label(page_2)

age_label = tk.Label(page_5, text="Укажи свой земной возраст:", justify="left", font=("Calibri", 10, "bold"))
age_entry = tk.Entry(page_5)
mars_label = tk.Label(page_5)

d1_label = tk.Label(page_4, text="Укажите внутренний диаметр в мм:", justify="left", font=("Calibri", 10, "bold"))
d1_entry = tk.Entry(page_4)
h1_label = tk.Label(page_4, text="Укажите длину в метрах:", justify="left", font=("Calibri", 10, "bold"))
h1_entry = tk.Entry(page_4)
v_label = tk.Label(page_4)

calculate_button = tk.Button(page_1, text="Рассчитать", command=calculate)
calculate2_button = tk.Button(page_2, text="Рассчитать", command=calculate2)
calculate3_button = tk.Button(page_2, text="Рассчитать", command=calculate3)
calculate4_button = tk.Button(page_2, text="Рассчитать", command=calculate4)
calculate5_button = tk.Button(page_2, text="Рассчитать", command=calculate5)
calculate6_button = tk.Button(page_5, text="Рассчитать", command=calculate6)
calculate7_button = tk.Button(page_4, text="Рассчитать", command=calculate7)


def focus_on_plo(event=None):
    plo_entry.focus_set()


def focus_on_plo2(event=None):
    plo2_entry.focus_set()


def focus_on_plo3(event=None):
    plo3_entry.focus_set()


def focus_on_plo4(event=None):
    plo4_entry.focus_set()


def focus_on_plo5(event=None):
    plo4_entry.focus_set()


def focus_on_age(event=None):
    age_entry.focus_set()


def focus_on_d1(event=None):
    d1_entry.focus_set()


def focus_on_h1(event=None):
    h1_entry.focus_set()


plo_entry.bind("<Return>", calculate)
plo2_entry.bind("<Return>", calculate2)
plo3_entry.bind("<Return>", calculate3)
plo4_entry.bind("<Return>", calculate4)
plo5_entry.bind("<Return>", calculate5)
age_entry.bind("<Return>", calculate6)
d1_entry.bind("<Return>", calculate7)
h1_entry.bind("<Return>", calculate7)

plo_label.place(x=20, y=30)
plo_entry.place(x=20, y=70)
calculate_button.place(x=20, y=100)
truba_label.place(x=20, y=130)
kontur_label.place(x=20, y=150)
truba2_label.place(x=20, y=180)
kontur2_label.place(x=20, y=200)
truba3_label.place(x=20, y=230)
kontur3_label.place(x=20, y=250)

plo2_label.place(x=20, y=30)
plo2_entry.place(x=20, y=70)
calculate2_button.place(x=20, y=100)
radiator1_label.place(x=20, y=130)
radiator11_label.place(x=20, y=150)

plo3_label.place(x=340, y=30)
plo3_entry.place(x=340, y=70)
calculate3_button.place(x=340, y=100)
radiator2_label.place(x=340, y=130)
radiator22_label.place(x=340, y=150)

plo4_label.place(x=340, y=220)
plo4_entry.place(x=340, y=260)
calculate4_button.place(x=340, y=290)
radiator3_label.place(x=340, y=320)
radiator33_label.place(x=340, y=340)

plo5_label.place(x=20, y=220)
plo5_entry.place(x=20, y=260)
calculate5_button.place(x=20, y=290)
radiator4_label.place(x=20, y=320)
radiator44_label.place(x=20, y=340)

age_label.place(x=20, y=30)
age_entry.place(x=20, y=70)
calculate6_button.place(x=20, y=100)
mars_label.place(x=20, y=130)

d1_label.place(x=20, y=30)
d1_entry.place(x=20, y=70)
h1_label.place(x=20, y=100)
h1_entry.place(x=20, y=130)
calculate7_button.place(x=20, y=150)
v_label.place(x=20, y=180)


plo_label.bind("<Button-1>", focus_on_plo)
plo2_label.bind("<Button-1>", focus_on_plo2)
plo3_label.bind("<Button-1>", focus_on_plo3)
plo4_label.bind("<Button-1>", focus_on_plo4)
plo5_label.bind("<Button-1>", focus_on_plo5)
age_label.bind("<Button-1>", focus_on_age)
d1_label.bind("<Button-1>", focus_on_d1)
h1_label.bind("<Button-1>", focus_on_h1)

root.mainloop()
