#!/usr/bin/python3
import tkinter as tk

class Main(tk.Frame): # Создаем класс Main, который наследует свойства класса Frame библиотеки tkinter
    def __init__(self, root):
        super().__init__(root) # Используем метод super для обращения к родительскому классу, чтобы явно не указывать его имя
        self.init_window() # Метод инициализации главного окна

    def init_window(self):
        root.title("Рассчет пластового давления")
        root.geometry("620x400+300+200")
        root.resizable(False,False)

        main_label = tk.Label(root, fg="green", height=3, font="13", text="Данная программа позволяет произвести расчет пластового давления.\nДля вычисления используется формула Р(пл) = h×r/с, где:").grid(row=0,column=0,columnspan=2)
        #класс Label библиотеки tkinter используется для отображения статичного текста
        #.grid() - метод для расположения эдементов в виде таблицы

        c_label = tk.Label(root, text="С – коэффициент, равный 102 при измерении давления в МПа.").grid(row=1,column=0,sticky="w")

        r = tk.DoubleVar() #r - плотность, тип данных это класс DoubleVar библиотеки tkinter
        r_entry = tk.Entry(root, width=8, textvariable=r).grid(row=2,column=1) #поле ввода Entry
        r_label = tk.Label(root, text="r – плотность жидкости в скважине, г/см3:").grid(row=2,column=0,sticky="w") #статичный текст Label

        h = tk.DoubleVar() #r - высота столба жидкости
        h_entry = tk.Entry(root, width=8, textvariable=h).grid(row=3,column=1)
        h_label = tk.Label(root, text="h – высота столба жидкости, уравновешивающего пластовое давление, м:").grid(row=3,column=0,sticky="w")

        p = tk.DoubleVar() #p - пластовое давление
        p_entry = tk.Entry(root, width=8, textvariable=p).grid(row=4,column=1)
        p_label = tk.Label(root, text="p - пластовое давление, МПа:").grid(row=4,column=0,sticky="w")

        info_label = tk.Label(root, height=2, text="Введите известные параметры и нажмите рассчитать").grid(row=5,column=0,columnspan=2)
        calc_btn = tk.Button(root, text='Рассчитать', command=lambda: self.calc(h,r,p,found_label)).grid(row=6,column=0,columnspan=2)
        # кнопка класса Button библиотеки tkinter, при нажатии вызывает функцию calc() с соответствующими аргументами

        found_label = tk.Label(root, height=2, font = "14")
        found_label.grid(row=7,column=0,columnspan=2)
        # Label который будет отображать ответ


        complex_label = tk.Label(root, fg="green", height=3, font="13", text="Для комплексного расчета воспользуйтесь\nсоответствующей функцией").grid(row=8,column=0,columnspan=2)
        complex_btn = tk.Button(root, text='Комплексный расчет', command=self.complex_dialog).grid(row=9,column=0,columnspan=2)
        # кнопка класса Button библиотеки tkinter, при нажатии вызывает функцию complex_dialog(), которая открывает соответствующее окно

        btn_open_table = tk.Button(root, text='Таблица плотностей', command=self.table_dialog, compound=tk.TOP).grid(row=11,column=0, columnspan=2, sticky="e")
        # кнопка класса Button библиотеки tkinter, при нажатии открывает окно с таблицей плотностей

    def calc(self,h,r,p,found_label):
        """
        Функция для расчета одного неизвестного (высоты, плотности, давления)
        Проверяет возможные комбинации ввода данных и оповещает окном с ошибкой в случае некорректного ввода.
        """
        c = 102
        try:
            h = h.get()
            r = r.get()
            p = p.get()
            if h!=0 and r!=0 and p==0:
                p_found = h*r/c
                found_label.configure(text="p, МПа = "+str(p_found))
            elif r!=0 and p!=0 and h==0:
                h_found = p*c/r
                found_label.configure(text="h, м = "+str(h_found))
            elif h!=0 and p!=0 and r==0:
                r_found = c*p/h
                found_label.configure(text="r, г/см^3 = "+str(r_found))
            else:
                self.error_dialog("Данные предоставлены неверно")
        except Exception as e:
            self.error_dialog(e)

    def complex_dialog(self):
        """
        Функция открывает окно(класс) Complex для компелексного расчета
        """
        Complex()

    def error_dialog(self,e):
        """
        Функция открывает окно(класс) ErrorWindow и передает аргумент e - ошибку, которую требуется отобразить
        """
        ErrorWindow(e)

    def table_dialog(self):
        """
        Функция открывает окно(класс) Table - таблицу плотностей
        """
        Table()


class Table(tk.Toplevel):
    """
    Таблица плотностей, состоит из множества Lablel'ов
    """
    def __init__(self):
        super().__init__(root)
        self.init_child()

    def init_child(self):
        self.title('Таблица плотностей')
        self.resizable(False, False)

        tk.Label(self, text="Материал", fg='blue',font='13').grid(row=0,column=0,sticky="w")
        tk.Label(self, text="Плотность, г/см^3", fg='blue',font='13').grid(row=0,column=1)

        tk.Label(self, text="Вода").grid(row=1,column=0,sticky="w")
        tk.Label(self, text="1").grid(row=1,column=1)
        tk.Label(self, text="Глиняный раствор").grid(row=2,column=0,sticky="w")
        tk.Label(self, text="1.12").grid(row=2,column=1)
        tk.Label(self, text="Газ").grid(row=3,column=0,sticky="w")
        tk.Label(self, text="0.06").grid(row=3,column=1)
        tk.Label(self, text="Бензин").grid(row=4,column=0,sticky="w")
        tk.Label(self, text="0.72").grid(row=4,column=1)
        tk.Label(self, text="Пластовая вода").grid(row=5,column=0,sticky="w")
        tk.Label(self, text="1.05").grid(row=5,column=1)
        tk.Label(self, text="Воздух").grid(row=6,column=0,sticky="w")
        tk.Label(self, text="0.12").grid(row=6,column=1)
        tk.Label(self, text="Нефть").grid(row=6,column=0,sticky="w")
        tk.Label(self, text="0.86").grid(row=6,column=1)


class Complex(tk.Toplevel):
    """
    Окно комплексного расчета, принимает на ввод известную плотность и уровень устья, а так же данные о близзалегающих веществах по удаленности (максимум 5, сначала близкие)
    """
    def __init__(self):
        super().__init__(root)
        self.init_child()

    def init_child(self):
        self.title('Комплексный расчет')
        self.resizable(False, False)

        main_label = tk.Label(self, height=3, font="13", fg="red", text="Данный модуль предназначен для расчета пластового\nдавления скавжины с неопределенным пьезометрическим уровнем.").grid(row=0,column=0,columnspan=3)

        p = tk.DoubleVar()
        p_entry = tk.Entry(self, width=8, textvariable=p).grid(row=1,column=2,sticky="w")
        p_label = tk.Label(self, text="Известное пластовое давление p, МПа:").grid(row=1,column=0,columnspan=2,sticky="e")

        u = tk.DoubleVar()
        u_entry = tk.Entry(self, width=8, textvariable=u).grid(row=2,column=2,sticky="w")
        u_label = tk.Label(self, text="Известная абсолютная отметка устья u, м:").grid(row=2,column=0,columnspan=2,sticky="e")

        info_label = tk.Label(self, height=2, font="13", fg="red", text="Введите информацию о граничащих веществах (сколько необходимо)").grid(row=3,column=0,columnspan=3)

        h_start_label = tk.Label(self, padx=20, text="Начальная абсолютная отметка, м").grid(row=4,column=0)
        h_end_label = tk.Label(self, padx=20, text="Конечная абсолютная отметка, м").grid(row=4,column=1)
        r_label = tk.Label(self, padx=20, text="Плотность вещества, г^см3").grid(row=4,column=2)

        h1_start = tk.DoubleVar()
        h1_start_entry = tk.Entry(self, width=8, textvariable=h1_start).grid(row=5,column=0)
        h2_start = tk.DoubleVar()
        h2_start_entry = tk.Entry(self, width=8, textvariable=h2_start).grid(row=6,column=0)
        h3_start = tk.DoubleVar()
        h3_start_entry = tk.Entry(self, width=8, textvariable=h3_start).grid(row=7,column=0)
        h4_start = tk.DoubleVar()
        h4_start_entry = tk.Entry(self, width=8, textvariable=h4_start).grid(row=8,column=0)
        h5_start = tk.DoubleVar()
        h5_start_entry = tk.Entry(self, width=8, textvariable=h5_start).grid(row=9,column=0)

        h1_end = tk.DoubleVar()
        h1_end_entry = tk.Entry(self, width=8, textvariable=h1_end).grid(row=5,column=1)
        h2_end = tk.DoubleVar()
        h2_end_entry = tk.Entry(self, width=8, textvariable=h2_end).grid(row=6,column=1)
        h3_end = tk.DoubleVar()
        h3_end_entry = tk.Entry(self, width=8, textvariable=h3_end).grid(row=7,column=1)
        h4_end = tk.DoubleVar()
        h4_end_entry = tk.Entry(self, width=8, textvariable=h4_end).grid(row=8,column=1)
        h5_end = tk.DoubleVar()
        h5_end_entry = tk.Entry(self, width=8, textvariable=h5_end).grid(row=9,column=1)

        r1 = tk.DoubleVar()
        r1_entry = tk.Entry(self, width=8, textvariable=r1).grid(row=5,column=2)
        r2 = tk.DoubleVar()
        r2_entry = tk.Entry(self, width=8, textvariable=r2).grid(row=6,column=2)
        r3 = tk.DoubleVar()
        r3_entry = tk.Entry(self, width=8, textvariable=r3).grid(row=7,column=2)
        r4 = tk.DoubleVar()
        r4_entry = tk.Entry(self, width=8, textvariable=r4).grid(row=8,column=2)
        r5 = tk.DoubleVar()
        r5_entry = tk.Entry(self, width=8, textvariable=r5).grid(row=9,column=2)

        complex_calc_btn = tk.Button(self, text='Рассчитать', command=lambda: self.complex_calc([(h1_start, h1_end),
                                                (h2_start, h2_end), (h3_start, h3_end), (h4_start, h4_end),
                                                (h5_start, h5_end)],[r1,r2,r3,r4,r5],p,u,found_label)).grid(row=10,column=0,columnspan=3)
        found_label = tk.Label(self, height=5, font = "14")
        found_label.grid(row=11,column=0,columnspan=3)


    def complex_calc(self,h_vars,r_vars,p,u,found_label):
        """
        Функция комплексного расчета, сначала проверяет правильность ввода отметок уровней, заполняя массив ненулевых (введенных пользователем) отметок.
        Затем заполняется массив ненулевых плотностей.
        Далее их длины должны совпасть (данные предоставлены верно), в обратном случае программа выдаст ошибку.
        Производится необходимый расчет, в конце данные выводятся на экран через Label
        """
        c = 102
        h_not_zero = []
        r_not_zero = []
        try:
            p = p.get()
            u = u.get()
            for h_tup in h_vars:
                h_start = h_tup[0].get()
                h_end = h_tup[1].get()
                if h_start != 0 and h_end != 0:
                    h_not_zero.append((h_start,h_end))
                elif (h_start == 0 and h_end != 0) or (h_start != 0 and h_end == 0):
                    self.error_dialog("Ошибка в представлении данных об абсолютных отметках")

            for r in r_vars:
                if r.get() !=0:
                    r_not_zero.append(r.get())

            if len(r_not_zero) == len(h_not_zero):
                p_found = p
                for r, h_tup in zip(r_not_zero, h_not_zero):
                    h_end = h_tup[1]
                    h_start = h_tup[0]
                    p_found -= r*(h_end-h_start)/c
                h_pesometr = p_found*c/r
                h_abs_level = h_pesometr+h_end
                if h_abs_level > u:
                    p_u_found = (h_abs_level-u)*r/c
                    found_label.configure(text="Пластовое давление p, МПа = "+str(p_found)+"\nПьезометрический уровень, м = "+str(h_pesometr)+"\nСкважина будет фонтанировать, давление на устье p(уст), МПа = "+str(p_u_found))
                else:
                    found_label.configure(text="Пластовое давление p, МПа = "+str(p_found)+"\nПьезометрический уровень, м = "+str(h_pesometr))
            else:
                self.error_dialog("Не указана плотность или абсолютные отметки")

        except Exception as e:
            self.error_dialog(e)

    def error_dialog(self,e):
        ErrorWindow(e)

class ErrorWindow(tk.Toplevel):
    """
    Окно для вывода ошибки
    """
    def __init__(self,e):
        super().__init__(root)
        self.e = e
        self.init_child()

    def init_child(self):
        self.title('Ошибка')
        self.resizable(False, False)
        tk.Label(self, padx=5, pady=40, font="14", text=self.e).pack()
        self.grab_set()


if __name__ == '__main__':
    root = tk.Tk() #создаем объект класса TK
    app = Main(root) #запускаем окно(класс) Main и передаем туда главный параметр root
    root.mainloop() # метод mainloop инициализирует главный цикл обработки событий
