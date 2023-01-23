import tkinter
import tkinter.messagebox
import sqlite3


class EmployeeDetails:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.__build_main_window()
        tkinter.mainloop()

    def __build_main_window(self):
        self.__create_prompt_label()
        self.__build_listbox_frame()
        self.__create_quitbutton()

    def __create_prompt_label(self):
        self.employee_prompt_label = tkinter.Label(self.main_window, text='Choose an employee: ')
        self.employee_prompt_label.pack(side='top', padx=5, pady=5)

    def __build_listbox_frame(self):
        self.listbox_frame = tkinter.Frame(self.main_window)
        self.__setup_listbox()
        self.__create_scrollbar()
        self.__populate_listbox()
        self.listbox_frame.pack()

    def __setup_listbox(self):
        self.employee_listbox = tkinter.Listbox(
            self.listbox_frame, selectmode=tkinter.SINGLE, height=6)
        self.employee_listbox.bind( '<<ListboxSelect>>', self.__get_details)
        self.employee_listbox.pack(side='left', padx=5, pady=5)

    def __create_scrollbar(self):
        self.scrollbar = tkinter.Scrollbar(self.listbox_frame, orient=tkinter.VERTICAL)
        self.scrollbar.config(command=self.employee_listbox.yview)
        self.employee_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side='right', fill=tkinter.Y)

    def __populate_listbox(self):
        for employee in self.__get_employees():
            self.employee_listbox.insert(tkinter.END, employee)

    def __create_quitbutton(self):
        self.quitbutton = tkinter.Button(self.main_window, text='QUIT',
                                         command=self.main_window.destroy)
        self.quitbutton.pack(side='top', padx=10, pady=5)

    def __get_employees(self):
        employees_list = []
        conn = None
        try:
            conn = sqlite3.connect('Data/employees.db')
            cur = conn.cursor()
            cur.execute('SELECT Name FROM Employees')

            employees_list = [n[0] for n in cur.fetchall()]
        except sqlite3.Error as err:
            tkinter.messagebox.showinfo('Database error', err)
        finally:
            if conn != None:
                conn.close()

        return employees_list

    def __get_details(self, event):
        listbox_index = self.employee_listbox.curselection()[0]
        selected_emp = self.employee_listbox.get(listbox_index)

        conn = None
        try:
            conn = sqlite3.connect('Data/employees.db')
            cur = conn.cursor()

            cur.execute(
                '''SELECT
                        Employees.Name,
                        Employees.Position,
                        Departments.DepartmentName,
                        Location.City
                    FROM
                        Employees, Departments, Locations
                    WHERE
                        Employees.Name == ? AND
                        Employees.DepartmentID == Departments.DepartmentID AND
                        Employees.LocationID == Locations.LocationID''',
                (selected_emp,))
            results = cur.fetchone()
            self.__display_details(name=results[0], position=results[1],
                                   department=results[2], location=results[3])
        except sqlite3.Error as err:
            tkinter.messagebox.showinfo('Database error', err)
        finally:
            if conn != None:
                conn.close()

    def __display_details(self, name, position, department, location):
        tkinter.messagebox.showinfo(f'Employees information\n'
                                    f'Name: {name}\n Position: {position}\n'
                                    f'Department: {department}\n Location {location}')
if __name__ == '__main__':
    prog = EmployeeDetails()
