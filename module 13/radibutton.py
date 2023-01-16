import tkinter
import tkinter.messagebox


class GUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title('Buttons')

        self.radio_frame = tkinter.Frame(self.main_window,
                                         borderwidth=1,
                                         relief='solid')
        self.check_frame = tkinter. Frame(self.main_window,
                                          borderwidth=1,
                                          relief='solid')
        self.buttons_frame = tkinter.Frame(self.main_window)

        #  Radiosection
        self.radio_var = tkinter.IntVar()
        self.radio_var.set(1)

        self.rb1 = tkinter.Radiobutton(self.radio_frame,
                                       text='Option 1',
                                       variable=self.radio_var,
                                       value=1)
        self.rb2 = tkinter.Radiobutton(self.radio_frame,
                                       text='Option 2',
                                       variable=self.radio_var,
                                       value=2)
        self.rb3 = tkinter.Radiobutton(self.radio_frame,
                                       text='Option 3',
                                       variable=self.radio_var,
                                       value=3)
        self.radio_ok = tkinter.Button(self.radio_frame,
                                       text='OK',
                                       command=self.radio_choice)
        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()
        self.radio_ok.pack()

        #  checkboxessection
        self.cb_var1 = tkinter.IntVar()
        self.cb_var2 = tkinter.IntVar()
        self.cb_var3 = tkinter.IntVar()

        self.cb_var1.set(0)
        self.cb_var2.set(0)
        self.cb_var3.set(0)

        self.cb1 = tkinter.Checkbutton(self.check_frame,
                                       text='Option 1',
                                       variable=self.cb_var1)
        self.cb2 = tkinter.Checkbutton(self.check_frame,
                                       text='Option 2',
                                       variable=self.cb_var2)
        self.cb3 = tkinter.Checkbutton(self.check_frame,
                                       text='Option 3',
                                       variable=self.cb_var3)
        self.check_ok = tkinter.Button(self.check_frame,
                                       text='OK',
                                       command=self.check_choice)

        self.cb1.pack()
        self.cb2.pack()
        self.cb3.pack()
        self.check_ok.pack()

        # quit buttonframe

        self.quit_button = tkinter.Button(self.buttons_frame,
                                          text='QUIT',
                                          command=self.main_window.destroy)

        self.quit_button.pack()

        self.radio_frame.pack(ipadx=10, ipady=10)
        self.check_frame.pack(ipadx= 10, ipady=10)
        self.buttons_frame.pack()

        tkinter.mainloop()

    def radio_choice(self):
        tkinter.messagebox.showinfo('Choice',
                                    'you choose ' +
                                    str(self.radio_var.get()))

    def check_choice(self):
        self.message = 'You choose:\n'
        if self.cb_var1.get() == 1:
            self.message = self.message + '1\n'
        if self.cb_var2.get() == 1:
            self.message = self.message + '2\n'
        if self.cb_var3.get() == 1:
            self.message = self.message + '3\n'

        tkinter.messagebox.showinfo('Checkbox choice', self.message)
if __name__ == '__main__':
    my_gui = GUI()