import tkinter as tk
import tkinter.ttk as ttk

class Main_Window(tk.Frame):

    def __init__(self):
        super().__init__(self)
        self.w_widgets()
        self.widgets()
        self.t_widgets()
        self.au_widgets()

    def widgets(self):
        self.mb = tk.Menubutton(text='file')
        self.m = tk.Menu(self.mb)
        self.m.grid(columnspan=1)


    def w_widgets(self):

        # frame for windows tape scans. It's own frame is required for organization and multiples.
        self.wframe = tk.LabelFrame(labelanchor='n', text="Windows Tapes", height=600, width=150)
        self.wframe.columnconfigure(0, weight=1)
        self.wframe.grid(row=10, column=0, padx=5, pady=2)

        # entry box for W tape case ID
        self.wcase = tk.Entry(self.wframe)
        self.wcase.insert(0, "Scan Case")
        self.wcase.grid(row=0, column=0)
        self.wcase.bind('<Button-1>', self.clear_entry)

        # text boxes for windows tape scans
        self.wtext = tk.Text(self.wframe, width=10)
        self.wtext.grid(row=1, column=0)

    # method to delete default text when mouse button is pressed
    def clear_entry(self, event=None):
        self.wcase.delete(0, 20)

    def t_widgets(self):

        # frame for T tapes. It's own frame is required for organization and multiples.
        self.tframe = tk.LabelFrame(labelanchor='n', text="T Tapes", height=600, width=200)
        self.tframe.columnconfigure(0, weight=1)
        self.tframe.grid(row=10, column=1, padx=5, pady=2)

        # entry box for T tape case ID
        self.tcase = tk.Entry(self.tframe)
        self.tcase.insert(0, "Scan Case")
        self.tcase.grid(row=0, column=0)

        # text box for t tape scans
        self.ttext = tk.Text(self.tframe, width=10)
        self.ttext.grid(row=1, column=0)

    def au_widgets(self):
        # frame for T tapes. It's own frame is required for organization and multiples.
        self.auframe = tk.LabelFrame(labelanchor='n', text="AU Tapes", height=600, width=200)
        self.auframe.columnconfigure(0, weight=1)
        self.auframe.grid(row=10, column=3, padx=5, pady=2)

        # entry box for T tape case ID
        self.aucase = tk.Entry(self.auframe)
        self.aucase.insert(0, "Scan Case")
        self.aucase.grid(row=0, column=0)

        # text box for t tape scans
        self.autext = tk.Text(self.auframe, width=10)
        self.autext.grid(row=1, column=0)


root = tk.Tk()
root.geometry('600x600+200+200')
app = Main_Window()
app.mainloop()