import tkinter


class TestAverage:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title('Average marks calculator')
        # Creating frames

        self.test_frame1 = tkinter.Frame(self.main_window)
        self.test_frame2 = tkinter.Frame(self.main_window)
        self.test_frame3 = tkinter.Frame(self.main_window)

        self.avg_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)

        # top frame 1
        self.test_label1 = tkinter.Label(self.test_frame1,
                                         text='Enter mark #1: ')
        self.test_entry1 = tkinter.Entry(self.test_frame1,
                                         width=10)
        self.test_label1.pack(side='left')
        self.test_entry1.pack(side='left')
        # top frame 2
        self.test_label2 = tkinter.Label(self.test_frame2,
                                         text='Enter mark #2: ')
        self.test_entry2 = tkinter.Entry(self.test_frame2,
                                         width=10)
        self.test_label2.pack(side='left')
        self.test_entry2.pack(side='left')
        # top frame 3
        self.test_label3 = tkinter.Label(self.test_frame3,
                                         text='Enter mark #3: ')
        self.test_entry3 = tkinter.Entry(self.test_frame3,
                                         width=10)
        self.test_label3.pack(side='left')
        self.test_entry3.pack(side='left')

        # Average marks frame
        self.result_label = tkinter.Label(self.avg_frame,
                                          text='Average mark is: ')
        self.avg = tkinter.StringVar()
        self.result_label = tkinter.Label(self.avg_frame,
                                          textvariable=self.avg)  # calculation result here
        self.result_label.pack(side='left')
        self.result_label.pack(side='left')

        # Buttons frame
        self.go_button = tkinter.Button(self.button_frame,
                                        text='Calculate: ',
                                        command=self.calc_avg)  # calculation function
        self.quit_button = tkinter.Button(self.button_frame,
                                          text='Quit',
                                          command=self.main_window.destroy)
        self.go_button.pack(side='left')
        self.quit_button.pack(side='left')

        self.test_frame1.pack()
        self.test_frame2.pack()
        self.test_frame3.pack()
        self.avg_frame.pack()
        self.button_frame.pack()

        tkinter.mainloop()

    def calc_avg(self):
        self.test1 = float(self.test_entry1.get())
        self.test2 = float(self.test_entry2.get())
        self.test3 = float(self.test_entry3.get())

        self.average = (self.test1 + self.test2 + self.test3) / 3.0

        self.avg.set(str(self.average))


if __name__ == '__main__':
    my_test = TestAverage()
