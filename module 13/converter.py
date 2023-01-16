import tkinter

class ConverterGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame()# self.main_window)
        self.mid_frame = tkinter.Frame()#(self.main_window)
        self.bottom_frame = tkinter.Frame()#(self.main_window)

        #top frame
        self.promt_label = tkinter.Label(self.top_frame,
                                         text='Enter kilometers:')
        self.kilo_entry = tkinter.Entry(self.top_frame,
                                        width=10)

        self.promt_label.pack(side='left')
        self.kilo_entry.pack(side='left')

        #mid frame
        self.descr_label = tkinter.Label(self.mid_frame,
                                         text='Converted to miles:')
        self.value = tkinter.StringVar()
        self.miles_label = tkinter.Label(self.mid_frame,
                                         textvariable=self.value)
        self.descr_label.pack(side='left')
        self.miles_label.pack(side='left')

        #Bottom frame
        self.calc_button = tkinter.Button(self.bottom_frame,
                                          text='Calculate',
                                          command=self.convert)
        self.quit_button = tkinter.Button(self.bottom_frame,
                                          text='Quit',
                                          command=self.main_window.destroy)

        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')

        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    def convert(self):
        kilo = float(self.kilo_entry.get())

        miles = kilo * 0.6214

        self.value.set(f'{float(miles):,.2f}')
if __name__ == '__main__':
    kilo_conv = ConverterGUI()