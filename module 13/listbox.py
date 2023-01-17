import tkinter

class Listboks():
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.listbox = tkinter.Listbox(self.main_window,
                                       height=0, width=12,)
        self.listbox.pack()

        days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

        for day in days:
            self.listbox.insert(tkinter.END, day)
        tkinter.mainloop()


if __name__ == '__main__':
    my_gui = Listboks()