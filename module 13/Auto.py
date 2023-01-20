import tkinter
import tkinter.messagebox

class Auto:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title('Autoparts')

        # checks
        self.check_frame = tkinter.Frame(self.main_window,
                                         borderwidth=1,
                                         relief='solid')
        self.oil = tkinter.IntVar()
        self.oil_works = tkinter.IntVar()
        self.radiator = tkinter.IntVar()
        self.transmissions = tkinter.IntVar()
        self.check = tkinter.IntVar()
        self.out = tkinter.IntVar()
        self.tyres = tkinter.IntVar()

        self.oil.set(0)
        self.oil_works.set(0)
        self.radiator.set(0)
        self.transmissions.set(0)
        self.check.set(0)
        self.out.set(0)
        self.tyres.set(0)

        self.oil_1 = tkinter.Checkbutton(self.check_frame,
                                       text='Oil - $500',
                                       variable=self.oil)
        self.oil_works_1 = tkinter.Checkbutton(self.check_frame,
                                       text='Oil works - $300',
                                       variable=self.oil_works)
        self.radiator_1 = tkinter.Checkbutton(self.check_frame,
                                       text='Radiator - $700',
                                       variable=self.radiator)
        self.transmissions_1 = tkinter.Checkbutton(self.check_frame,
                                       text='Transmission - $1000',
                                       variable=self.transmissions)
        self.check_1 = tkinter.Checkbutton(self.check_frame,
                                       text='Check - $800',
                                       variable=self.check)
        self.out_1 = tkinter.Checkbutton(self.check_frame,
                                       text='Outer - $1300',
                                       variable=self.out)
        self.tyres_1 = tkinter.Checkbutton(self.check_frame,
                                       text='Tyres - $1300',
                                       variable=self.tyres)
        self.oil_1.pack()
        self.oil_works_1.pack()
        self.radiator_1.pack()
        self.transmissions_1.pack()
        self.check_1.pack()
        self.out_1.pack()
        self.tyres_1.pack()
        # Buttons frame
        self.buttons = tkinter.Frame(self.main_window)
        self.countbutton = tkinter.Button(self.buttons, text='Count',
                                          command=self.check_choice)
        self.quitbutton = tkinter.Button(self.buttons, text='QUIT',
                                         command=self.main_window.destroy)

        self.check_frame.pack()
        self.buttons.pack()
        self.countbutton.pack()
        self.quitbutton.pack()

        tkinter.mainloop()

    def check_choice(self):
        self.total = 0
        if self.oil.get() == 1:
            self.total += 500
        if self.oil_works.get() == 1:
            self.total += 300
        if self.radiator.get() == 1:
            self.total += 700
        if self.transmissions.get() == 1:
            self.total += 1000
        if self.check.get() == 1:
            self.total += 800
        if self.out.get() == 1:
            self.total += 1300
        if self.tyres.get() == 1:
            self.total += 1300
        self.message = f'All works cost $ {self.total}'
        tkinter.messagebox.showinfo('Total', self.message)

if __name__ == '__main__':
    prog = Auto()

