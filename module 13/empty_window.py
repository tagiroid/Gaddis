import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        #title
        self.main_window = tkinter.Tk()
        self.main_window.title('First GUI')

        #frames
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        #frames labels
        self.frame_label_1 = tkinter.Label(self.top_frame,
                                           text= 'ONE')
        self.frame_label_2 = tkinter.Label(self.top_frame,
                                           text='TWO')
        self.frame_label_3 = tkinter.Label(self.top_frame,
                                           text='THREE')

        self.frame_label_1.pack(side='top')
        self.frame_label_2.pack(side='top')
        self.frame_label_3.pack(side='top')

        #frame labels 2
        self.frame_label_4 = tkinter.Label(self.top_frame,
                                           text='ONE')
        self.frame_label_5 = tkinter.Label(self.top_frame,
                                           text='TWO')
        self.frame_label_6 = tkinter.Label(self.top_frame,
                                           text='THREE')

        self.frame_label_4.pack(side='left')
        self.frame_label_5.pack(side='left')
        self.frame_label_6.pack(side='left')


        # labels with borders
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

        self.top_frame.pack()
        self.bottom_frame.pack()

        # buttons
        self.my_button = tkinter.Button(self.main_window,
                                        text='Push me!',
                                        command=self.do_something)
        self.quit_button = tkinter.Button(self.main_window,
                                          text='Im done with this s*it!',
                                          command=self.main_window.destroy)
        self.my_button.pack()
        self.quit_button.pack()

        # doesnt close
        tkinter.mainloop()

    def do_something(self):
        tkinter.messagebox.showinfo('Reaction', 'thank you!')



if __name__ == '__main__':
    my_gui = MyGUI()