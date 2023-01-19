import tkinter
import tkinter.font

HOR = 600
VER = 400


class CanvasGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title('Canvas practice')
        # this part is for lines
        self.canvas = tkinter.Canvas(self.main_window,
                                     width=HOR, height=VER)

        self.canvas.create_line(0, 0, 199, 199, fill='green')
        self.canvas.create_line(199, 0, 0, 199, fill='blue')
        self.canvas.create_line(0, 200, HOR, 200)  # horizontal
        self.canvas.create_line(200, 0, 200, 400)  # vertical
        self.canvas.create_line(400, 0, 400, 400)  # vertical 2
        points = [25, 25, 25, 175, 175, 175, 175, 25, 25, 25]
        self.canvas.create_line(points, dash=(5, 5))

        # this part is for rectangles
        self.canvas.create_rectangle(50, 50, 150, 150, fill='red', width=5)
        self.canvas.create_rectangle(2, 2, 200, 200)

        #  this part draws ovals
        self.canvas.create_oval(280, 75, 330,  125, width=5, outline='green')   # look like circle
        self.canvas.create_oval(210, 50, 390,  150, dash=(2, 2))
        self.canvas.pack()

        #  in this part im practicing arcs
        self.canvas.create_arc(10, 210, 190, 390, start=45, extent=30, fill='brown')  # default.PIESLICE
        self.canvas.create_arc(10, 210, 190, 390, start=180, extent=50, style=tkinter.ARC)
        self.canvas.create_arc(10, 210, 190, 390, start=240, extent=100,
                               fill='green', style=tkinter.CHORD)
        # PIECHART
        self.draw_piechart()
        # practicing polygons and texts
        self.canvas.create_polygon(480, 40, 520, 40, 560, 80, 560, 120,
                                   520, 160, 480, 160, 440, 120, 440, 80,
                                   fill='white', outline='red', width=10)
        stop_font = tkinter.font.Font(family='Arial', size=18, weight='bold')
        self.canvas.create_text(500, 100, text="STOP", font=stop_font)
        my_font = tkinter.font.Font(family='Arial', size=30, weight='bold')
        self.canvas.create_text(500, 300, text="Oh, c'mon", font=my_font)
        tkinter.mainloop()

    def draw_piechart(self):
        self.__X1 = 220
        self.__Y1 = 220
        self.__X2 = 380
        self.__Y2 = 380

        self.__PIE1_START = 0
        self.__PIE1_WIDTH = 45
        self.__PIE2_START = 45
        self.__PIE2_WIDTH = 90
        self.__PIE3_START = 135
        self.__PIE3_WIDTH = 120
        self.__PIE4_START = 255
        self.__PIE4_WIDTH = 105

        self.canvas.create_arc(self.__X1, self.__Y1, self.__X2,
                               self.__Y2, start=self.__PIE1_START,
                               extent=self.__PIE1_WIDTH, fill='red')
        self.canvas.create_arc(self.__X1, self.__Y1, self.__X2,
                               self.__Y2, start=self.__PIE2_START,
                               extent=self.__PIE2_WIDTH, fill='green')
        self.canvas.create_arc(self.__X1, self.__Y1, self.__X2,
                               self.__Y2, start=self.__PIE3_START,
                               extent=self.__PIE3_WIDTH, fill='blue')
        self.canvas.create_arc(self.__X1, self.__Y1, self.__X2,
                               self.__Y2, start=self.__PIE4_START,
                               extent=self.__PIE4_WIDTH, fill='yellow')
        self.canvas.pack()


if __name__ == '__main__':
    run = CanvasGUI()
