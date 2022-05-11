import Logic as t
from tkinter import *


class GUI:
    def __init__(self, window):
        self.window = window

        self.frame_choose = Frame(self.window)
        self.label_choose = Label(self.frame_choose, text='Choose Function')
        self.radio_1 = IntVar()
        self.radio_1.set(0)
        self.radio_one = Radiobutton(self.frame_choose, text='adding n to all lower numbers', variable=self.radio_1, value=1)
        self.radio_two = Radiobutton(self.frame_choose, text='n to the p power', variable=self.radio_1, value=2)
        self.radio_three = Radiobutton(self.frame_choose, text='listing n and all lower numbers', variable=self.radio_1, value=3)
        self.label_choose.pack(padx=5, side='top')
        self.radio_one.pack(side='left')
        self.radio_two.pack(side='left')
        self.radio_three.pack(side='left')
        self.frame_choose.pack(pady=5)

        self.button_choose = Button(self.window, text='CHOOSE', command=self.choose)
        self.button_choose.pack(side='top')

    def choose(self):
        radget = self.radio_1.get()

        if radget == 1:
            new_window = Toplevel()
            new_window.geometry('250x180')
            new_window.resizable(False, False)
            self.window2 = new_window

            self.frame_label = Frame(self.window2)
            self.label_label = Label(self.frame_label, text='n + (n - 1)')
            self.label_label.pack(padx=5, side='top')
            self.frame_label.pack(pady=5)

            self.frame_top = Frame(self.window2)
            self.label_num = Label(self.frame_top, text='Enter n')
            self.entry_num = Entry(self.frame_top)
            self.label_num.pack(padx=5, side='left')
            self.entry_num.pack(padx=5, side='left')
            self.frame_top.pack()

            self.label_message = Label(self.window2, text=' ')
            self.label_message.pack(side='top')

            self.button_submit = Button(self.window2, text='SUBMIT', command=self.clicked1)
            self.button_submit.pack(side='bottom')



        elif radget == 2:
            new_window = Toplevel()
            new_window.geometry('250x180')
            new_window.resizable(False, False)
            self.window3 = new_window

            self.frame_label2 = Frame(self.window3)
            self.label_label2 = Label(self.frame_label2, text='n to the p power')
            self.label_label2.pack(padx=5, side='top')
            self.frame_label2.pack(pady=5)

            self.frame_top2 = Frame(self.window3)
            self.label_num2 = Label(self.frame_top2, text='Enter n')
            self.entry_num2 = Entry(self.frame_top2)
            self.label_num2.pack(padx=5, side='left')
            self.entry_num2.pack(padx=5, side='left')
            self.frame_top2.pack()

            self.frame_top3 = Frame(self.window3)
            self.label_num3 = Label(self.frame_top3, text='Enter p')
            self.entry_num3 = Entry(self.frame_top3)
            self.label_num3.pack(padx=5, side='left')
            self.entry_num3.pack(padx=5, side='left')
            self.frame_top3.pack()

            self.label_message2 = Label(self.window3, text=' ')
            self.label_message2.pack(side='top')

            self.button_submit2 = Button(self.window3, text='SUBMIT', command=self.clicked2)
            self.button_submit2.pack(side='bottom')

        elif radget == 3:
            new_window = Toplevel()
            new_window.geometry('250x180')
            new_window.resizable(False, False)
            self.window4 = new_window

            self.frame_label4 = Frame(self.window4)
            self.label_label4 = Label(self.frame_label4, text='n, n - 1')
            self.label_label4.pack(padx=5, side='top')
            self.frame_label4.pack(pady=5)

            self.frame_top4 = Frame(self.window4)
            self.label_num4 = Label(self.frame_top4, text='Enter n')
            self.entry_num4 = Entry(self.frame_top4)
            self.label_num4.pack(padx=5, side='left')
            self.entry_num4.pack(padx=5, side='left')
            self.frame_top4.pack()

            self.label_message4 = Label(self.window4, text=' ')
            self.label_message4.pack(side='top')

            self.button_submit4 = Button(self.window4, text='SUBMIT', command=self.clicked3)
            self.button_submit4.pack(side='bottom')

    def clicked1(self):
        numget = int(self.entry_num.get())
        print(f'{t.one(numget)}')
        self.label_message.config(text=f'{t.one(numget)}')

    def clicked2(self):
        numget1 = int(self.entry_num2.get())
        numget2 = int(self.entry_num3.get())
        self.label_message2.config(text=f'{t.two(numget1, numget2)}')

    def clicked3(self):
        numget4 = int(self.entry_num4.get())
        self.label_message4.config(text=f'{t.three(numget4)}')

