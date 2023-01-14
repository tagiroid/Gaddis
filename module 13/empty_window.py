import tkinter

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title('First GUI')
        self.label1 = tkinter.Label(self.main_window,
                                   text= 'Hello world, yopta!',
                                    borderwidth=1,
                                    relief='solid')
        self.label2 = tkinter.Label(self.main_window,
                                    text= 'Say hello to my first GUI!',
                                    borderwidth=4,
                                    relief='groove')
        self.label3 = tkinter.Label(self.main_window,
                                    text= 'MUDAFAKA!', borderwidth= 5,
                                    relief='raised')
        self.label1.pack(ipadx=20, ipady=30)
        self.label2.pack(padx=(40,5), pady=(40,10))
        self.label3.pack(ipadx=10,ipady=10, padx=10, pady=10)

        tkinter.mainloop()
if __name__ == '__main__':
    my_gui = MyGUI()