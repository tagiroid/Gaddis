import tkinter

class Temper:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title('Temperature')

        #Converter
        self.text_frame = tkinter.Frame(self.main_window,
                                        borderwidth=1,
                                        relief='solid')
        self.text_label = tkinter.Label(self.text_frame,
                                        text='Convert Celcius to Fahrengheit: ')
        self.result = tkinter.Entry(self.text_frame, width=10)
        self.text_frame.pack()
        self.text_label.pack(side='left')
        self.result.pack(side='left')
        # Answer frame
        self.answer_frame = tkinter.Frame(self.main_window,
                                          borderwidth=1, relief='solid')
        self.answer = tkinter.Label(self.answer_frame,
                                    text='Your answer is: ')
        self.value = tkinter.StringVar()
        self.answer_far = tkinter.Label(self.answer_frame,
                                        textvariable=self.value)
        self.answer_frame.pack()
        self.answer.pack()
        self.answer_far.pack()
        # Buttons
        self.buttons = tkinter.Frame(self.main_window)
        self.count_button = tkinter.Button(self.buttons, text='Convert',
                                          command=self.converter)
        self.quit_button = tkinter.Button(self.buttons, text='QUIT',
                                         command=self.main_window.destroy)
        self.buttons.pack()
        self.count_button.pack(side='left')
        self.quit_button.pack(side='left')

        tkinter.mainloop()

    def converter(self):
        pass
        cel = float(self.result.get())
        far = float(((9/5)*cel) + 32)
        self.value.set(far)

if __name__ == '__main__':
    prog = Temper()