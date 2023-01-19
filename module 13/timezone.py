import tkinter

class TimeZone:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title('TimeZones')

        self.__build_prompt_label()
        self.__build_listbox()
        self.__build_output_frame()
        self.__build_quit_button()

        tkinter.mainloop()

    def __build_prompt_label(self):
        self.prompt_label = tkinter.Label(self.main_window, text='Choose a city',)
        self.prompt_label.pack(padx=5, pady=5)

    def __build_listbox(self):
        self.__cities = ['City of Denver, USA', 'City of Utah, USA', 'City of Seattle, USA',
                         'City of Honolulu, USA', 'City of Minneapolis, USA', 'City of New-York, USA',
                         'City of Boston, USA', 'City of Los-Angeles, USA', 'City of Miami, USA',
                         'City of San-Francisco, USA', 'City of Orlando, USA', 'City of Houston, USA']


        # vertical and horizontal scrollbars
        self.outer_frame = tkinter.Frame(self.main_window)
        self.outer_frame.pack(padx=15, pady=15)
        self.inner_frame = tkinter.Frame(self.outer_frame)
        self.inner_frame.pack()
        self.listbox = tkinter.Listbox(self.inner_frame,
                                       height=5, width=10)
        self.listbox.pack(side='left')
        self.v_scrollbar = tkinter.Scrollbar(self.inner_frame,
                                           orient=tkinter.VERTICAL)
        self.v_scrollbar.pack(side='right', fill=tkinter.Y)
        self.h_scrollbar = tkinter.Scrollbar(self.outer_frame,
                                             orient=tkinter.HORIZONTAL)
        self.v_scrollbar.pack(side='bottom', fill=tkinter.X)
        self.listbox.bind('<<ListboxSelect>>', self.__display_timezone)
        self.v_scrollbar.config(command=self.listbox.yview)
        self.h_scrollbar.config(command=self.listbox.xview)
        self.listbox.config(yscrollcommand=self.v_scrollbar.set,
                            xscrollcommand=self.h_scrollbar.set)


        for city in self.__cities:
            self.listbox.insert(tkinter.END, city)

    def __build_output_frame(self):
        self.output_frame = tkinter.Frame(self.main_window)
        self.output_frame.pack(padx=5)
        self.output_description_label = tkinter.Label(
            self.output_frame, text='Time Zone')
        self.output_description_label.pack(side='left', padx=(5,1),pady=5)
        self.__timezone = tkinter.StringVar()
        self.output_label = tkinter.Label(self.output_frame,
                                          borderwidth=1, relief='solid',
                                          width=15, textvariable=self.__timezone)
        self.output_label.pack(side='right', padx=(1,5), pady=5)

    def __build_quit_button(self):
        self.quit_button = tkinter.Button(self.main_window,
                                          text='Quit',
                                          command=self.main_window.destroy)
        self.quit_button.pack(padx=5, pady=5)

    def __display_timezone(self, event):
        index = self.listbox.curselection()
        city = self.listbox.get(index[0])

        if city == 'City of Denver, USA' or city == 'City of Utah, USA':
            self.__timezone.set('Mountain')
        elif city == 'City of Honolulu, USA':
            self.__timezone.set('Hawaiian')
        elif city == 'City of Minneapolis, USA' or city == 'City of Houston, USA':
            self.__timezone.set('Central')
        elif city == 'City of New-York, USA' or city == 'City of Boston, USA' or \
                city =='City of Miami, USA' or city =='City of Orlando, USA':
            self.__timezone.set('Eastern')
        elif city == 'City of San-Francisco, USA' or city == 'City of Seattle, USA'\
                or city == 'City of Los-Angeles, USA':
            self.__timezone.set('Pacific')


if __name__ == '__main__':
    my_gui = TimeZone()