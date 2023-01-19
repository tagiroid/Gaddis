import tkinter
import tkinter.messagebox

class Listboks():
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.listbox = tkinter.Listbox(self.main_window,
                                       height=0, width=0)
        self.get_button = tkinter.Button(self.main_window,
                                         text= 'Get day',
                                         command=self.__retrieve_day)
        self.quit_button = tkinter.Button(self.main_window,
                                          text='Quit',
                                          command=self.main_window.destroy)

        self.listbox.pack(padx=10, pady=5)
        self.get_button.pack(padx=10, pady=5)
        self.quit_button.pack()

        days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

        for day in days:
            self.listbox.insert(tkinter.END, day)

        tkinter.mainloop()

    def __retrieve_day(self):
        indexes = self.listbox.curselection()
        if (len(indexes) > 0):
            tkinter.messagebox.showinfo(
            message= self.listbox.get(indexes[0]))
        else:
            tkinter.messagebox.showinfo(
                message='No day was chosen')
if __name__ == '__main__':
    my_gui = Listboks()