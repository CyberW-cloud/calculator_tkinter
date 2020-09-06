import tkinter as tk


class CalculatorApp(tk.Frame):
    """
    Calculator on Tkinter with basic operators.
    """
    def __init__(self, master):
        super().__init__(master)
        self.log_list = list()
        self.master = master
        self.pack()
        self._create_main_canvas()
        self._create_input_frame()
        self._create_button_cont()

    def _calculate(self):
        user_input = self.entry.get()
        if user_input:
            try:
                result = round(eval(user_input.replace('^', '**')), 3)
                output = f'{user_input} = {result}'
                self._clear_input()
            except SyntaxError:
                output = "Bad operators"
            except NameError:
                output = "Only numbers allowed"
            finally:
                self._update_log(output)

    def _clear_all(self):
        for entry in self.log_list:
            entry.destroy()
        self.log_list.clear()
        self._clear_input()

    def _clear_input(self):
        self.entry.delete(0, 100)

    def _button_callback(self, symbol):
        if symbol == 'C':
            self._clear_input()
        elif symbol == 'CE':
            self._clear_all()
        elif symbol == '=':
            self._calculate()
        else:
            self.entry.insert(tk.INSERT, symbol)

    def _update_log(self, text=None):
        # Clearing oldest log entry if full
        if len(self.log_list) == 5:
            self.log_list[0].destroy()
            self.log_list.pop(0)

        label = tk.Label(self.log_frame,
                         bg='#3E3E3E',
                         font=('Times', 24),
                         fg='#FFF',
                         height=1,
                         text=text,
                         wraplength=370,
                         justify='left')
        label.pack(anchor='w')
        self.log_list.append(label)



    def _create_main_canvas(self):
        self.main_canvas = tk.Canvas(self,
                                     width=400,
                                     height=500,
                                     bg='#000')
        self.main_canvas.pack()
        self.log_frame = tk.Frame(self.main_canvas, bd=15,
                                  bg='#3E3E3E')
        self.log_frame.place(relwidth=1, relheight=0.45)
        self._update_log()

    def _create_input_frame(self):
        self.input_frame = tk.Frame(self.main_canvas,
                                    highlightbackground="#000",
                                    highlightthickness=1,
                                    bg='#3D3D3D')
        self.input_frame.place(relx=0, rely=0.45,
                               relwidth=1, relheight=0.1)
        self.entry = tk.Entry(self.input_frame,
                              bg='#4D4D4D',
                              font=('Times', 32),
                              fg='#FFF',
                              highlightcolor='#3D3D3D',
                              justify='left',
                              relief='solid',
                              width=20)
        self.entry.pack(padx=2, pady=2)

    def _create_button_cont(self):
        self.button_cont = tk.Frame(self.main_canvas,
                                    bd=15,
                                    bg='#3C3C3C')
        self.button_cont.place(relx=0, rely=0.55,
                               relwidth=1, relheight=0.45)

        button_matrix = [['7', '8', '9', 'C', 'CE'],
                         ['4', '5', '6', '+', '-'],
                         ['1', '2', '3', '*', '/'],
                         ['.', '0', '^', '()', '=']]

        button_list = list()
        for row in button_matrix:
            row_num = button_matrix.index(row)
            for symbol in row:
                col_num = row.index(symbol)
                button = self._create_button(self.button_cont, symbol)\
                    .grid(padx=3, pady=3, row=row_num, column=col_num)
                button_list.append(button)

    def _create_button(self, master, symbol):
        button = tk.Button(master,
                           width=3,
                           highlightbackground="#000",
                           highlightthickness=1,
                           activebackground='#4D4D4D',
                           activeforeground='#FFF',
                           fg='#FFF',
                           bg='#3D3D3D',
                           relief='flat',
                           font=('Times', 20),
                           text=symbol,
                           command=lambda x=symbol: self._button_callback(x))
        return button


if __name__ == '__main__':
    root = tk.Tk()
    root.title('My Calculator')
    root.resizable(width=False, height=False)
    app = CalculatorApp(master=root)
    app.mainloop()