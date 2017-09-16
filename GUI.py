import tkinter as tk
import tkinter.ttk as ttk

class Main_Window(tk.Frame):

    def __init__(self):
        super().__init__()
        self.w_widgets()
        self.widgets()
        self.t_widgets()
        self.au_widgets()

    def widgets(self):

        def doNothing():
            pass

        subMenu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="Add", menu=subMenu)
        subMenu.add_command(label="W Tapes", command=self.add_wtape)
        subMenu.add_command(label="T Tapes", command=doNothing)
        subMenu.add_command(label="AU Tapes", command=doNothing)

    def add_wtape(self):

        def getx():
            with open(Gui_var.dat) as f:
                pass



        # entry box for W tape case ID
        self.wcase = ttk.Entry(self.wframe)
        self.wcase.insert(0, "Scan Case")
        self.wcase.grid(row=0, column=1, padx=10)
        self.wcase.bind('<Button-1>', self.clear_entry)

        # text boxes for windows tape scans
        self.wtext = tk.Text(self.wframe, width=10)
        self.wtext.grid(row=1, column=1, sticky="wens", padx=10, pady=10)

        x += 1

    def w_widgets(self):

        # frame for windows tape scans. It's own frame is required for organization and multiples.
        self.wframe = ttk.LabelFrame(labelanchor='n', text="Windows Tapes", height=600, width=150)
        self.wframe.columnconfigure(0, weight=1)
        self.wframe.pack(side="left", fill="y")

        # entry box for W tape case ID
        self.wcase = ttk.Entry(self.wframe)
        self.wcase.insert(0, "Scan Case")
        self.wcase.grid(row=0, column=0, padx=10)
        self.wcase.bind('<Button-1>', self.clear_entry)

        # text boxes for windows tape scans
        self.wtext = tk.Text(self.wframe, width=10)
        self.wtext.grid(row=1, column=0, sticky="wens", padx=10, pady=10)

    def t_widgets(self):

        # frame for T tapes. It's own frame is required for organization and multiples.
        self.tframe = ttk.LabelFrame(labelanchor='n', text="T Tapes", height=600, width=200)
        self.tframe.columnconfigure(0, weight=1)
        self.tframe.pack(side="left", fill="y")

        # entry box for T tape case ID
        self.tcase = ttk.Entry(self.tframe)
        self.tcase.insert(0, "Scan Case")
        self.tcase.grid(row=0, column=0, padx=10)
        self.tcase.bind('<Button-1>', self.clear_entry)

        # text box for t tape scans
        self.ttext = tk.Text(self.tframe, width=10)
        self.ttext.grid(row=1, column=0, sticky="wens", padx=10, pady=10)

    def au_widgets(self):
        # frame for T tapes. It's own frame is required for organization and multiples.
        self.auframe = ttk.LabelFrame(labelanchor='n', text="AU Tapes", height=600, width=200)
        self.auframe.columnconfigure(0, weight=1)
        self.auframe.pack(side="left", fill="y")

        # entry box for T tape case ID
        self.aucase = ttk.Entry(self.auframe)
        self.aucase.insert(0, "Scan Case")
        self.aucase.grid(row=0, column=0, padx=10)
        self.aucase.bind('<Button-1>', self.clear_entry)

        # text box for t tape scans
        self.autext = tk.Text(self.auframe, width=10)
        self.autext.grid(row=1, column=0, sticky="wens", padx=10, pady=10)

    # method to delete default text when mouse button is pressed
    def clear_entry(self, event=None):
        event.widget.delete(0, 'end')

    def add_case(self):
        pass


root = tk.Tk()
root.geometry('600x600+200+200')

root.style = ttk.Style()
root.style.theme_use("default")


menu = tk.Menu(root)
root.config(menu=menu)

app = Main_Window()
app.mainloop()