import tkinter


class Scroll:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.outer_frame = tkinter.Frame(self.main_window)
        self.outer_frame.pack(padx=20, pady=20)

        self.inner_frame = tkinter.Frame(self.outer_frame)
        self.inner_frame.pack()

        self.listbox = tkinter.Listbox(self.inner_frame,
                                       height=5, width=30)
        self.listbox.pack(side='left')

        self.v = tkinter.Scrollbar(self.inner_frame, orient=tkinter.VERTICAL)
        self.v.pack(side='right', fill=tkinter.Y)

        self.h = tkinter.Scrollbar(self.outer_frame, orient=tkinter.HORIZONTAL)
        self.h.pack(side='bottom', fill=tkinter.X)

        self.v.config(command=self.listbox.yview)
        self.h.config(command=self.listbox.xview)
        self.listbox.config(yscrollcommand=self.v.set, xscrollcommand=self.h.set)

        data = ['Random text:',
                'Как рассказал союзу брат режиссера,',
                'Досталь умер вечером 18 января. Причины смерти не уточняются.',
                'Николай Досталь — советский и российский режиссер, сценарист и актер.',
                'Среди самых известных его работ — ',
                'фильмы «Облако-рай», «Раскол», «До свидания, мальчики» (актерская работа),',
                'а также телесериал «Штрафбат».']

        for sentence in data:
            self.listbox.insert(tkinter.END, sentence)

        tkinter.mainloop()


if __name__ == '__main__':
    my_prog = Scroll()
