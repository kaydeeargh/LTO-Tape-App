import tkinter as tk
import tkinter.ttk as ttk
import configparser as cp

class Main_Window(tk.Frame):

    def __init__(self):
        super().__init__()
        self.w_widgets()
        self.widgets()
        self.t_widgets()
        self.au_widgets()
        self.wc = []
        self.tc = []
        self.auc = []
        root.protocol("WM_DELETE_WINDOW", self.on_close)

    def widgets(self):

        def doNothing():
            pass

        addMenu = tk.Menu(menu, tearoff=0)
        remMenu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="Add", menu=addMenu)
        menu.add_cascade(label="Remove", menu=remMenu)
        addMenu.add_command(label="W Tapes", command=lambda: self.add_tape('W Tape'))
        addMenu.add_command(label="T Tapes", command=lambda: self.add_tape('T Tape'))
        addMenu.add_command(label="AU Tapes", command=lambda: self.add_tape('AU Tape'))

        remMenu.add_command(label="W Tapes", command=self.rem_wtape)
        remMenu.add_command(label="T Tapes", command=self.rem_ttape)
        remMenu.add_command(label="AU Tapes", command=self.rem_autape)

    def add_tape(self, code):

        config = cp.ConfigParser()
        config.read('param.ini')
        self.curr_wplace = config.getint('DEFAULT', 'wcasecount')
        self.curr_tplace = config.getint('DEFAULT', 'tcasecount')
        self.curr_auplace = config.getint('DEFAULT', 'aucasecount')

        if code == 'W Tape':
            self.wcase = ttk.Entry(self.wframe)
            self.wcase.insert(0, "Scan Case")
            self.wcase.grid(row=0, column=self.curr_wplace, padx=10)
            self.wcase.bind('<Button-1>', self.clear_entry)

            # # text boxes for windows tape scans
            self.wtext = tk.Text(self.wframe, width=10)
            self.wtext.grid(row=1, column=self.curr_wplace, sticky="wens", padx=10, pady=10)

            self.wctuple = (self.wcase, self.wtext)
            self.wc.append(self.wctuple)

            self.curr_wplace += 1
            config.set('DEFAULT', 'wcasecount', '%s' % (self.curr_wplace))
            with open('param.ini', 'w') as configfile:
                config.write(configfile)

        if code == 'T Tape':
            self.tcase = ttk.Entry(self.tframe)
            self.tcase.insert(0, "Scan Case")
            self.tcase.grid(row=0, column=self.curr_tplace, padx=10)
            self.tcase.bind('<Button-1>', self.clear_entry)

            # # text boxes for windows tape scans
            self.ttext = tk.Text(self.tframe, width=10)
            self.ttext.grid(row=1, column=self.curr_tplace, sticky="wens", padx=10, pady=10)

            self.tctuple = (self.tcase, self.ttext)
            self.tc.append(self.tctuple)

            self.curr_tplace += 1
            config.set('DEFAULT', 'tcasecount', '%s' % (self.curr_tplace))
            with open('param.ini', 'w') as configfile:
                config.write(configfile)

        if code == 'AU Tape':
            self.aucase = ttk.Entry(self.auframe)
            self.aucase.insert(0, "Scan Case")
            self.aucase.grid(row=0, column=self.curr_auplace, padx=10)
            self.aucase.bind('<Button-1>', self.clear_entry)

            # # text boxes for windows tape scans
            self.autext = tk.Text(self.auframe, width=10)
            self.autext.grid(row=1, column=self.curr_auplace, sticky="wens", padx=10, pady=10)

            self.auctuple = (self.aucase, self.autext)
            self.auc.append(self.auctuple)

            self.curr_auplace += 1
            config.set('DEFAULT', 'aucasecount', '%s' % (self.curr_auplace))
            with open('param.ini', 'w') as configfile:
                config.write(configfile)

    def add_wtape(self):

        config = cp.ConfigParser()
        config.read('param.ini')
        self.currentwplace = config.getint('Windows Case', 'wcasecount')



        if self.currentwplace > 0:

            # entry box for W tape case ID
            self.wcase = ttk.Entry(self.wframe)
            self.wcase.insert(0, "Scan Case")
            self.wcase.grid(row=0, column=self.currentwplace, padx=10)
            self.wcase.bind('<Button-1>', self.clear_entry)

            # # text boxes for windows tape scans
            self.wtext = tk.Text(self.wframe, width=10)
            self.wtext.grid(row=1, column=self.currentwplace, sticky="wens", padx=10, pady=10)

        self.wctuple = (self.wcase, self.wtext)
        self.wc.append(self.wctuple)

        self.currentwplace += 1
        config.set('Windows Case', 'wcasecount', '%s' % (self.currentwplace))
        with open('param.ini', 'w') as configfile:
            config.write(configfile)

    def rem_wtape(self):

        self.wclen = len(self.wc)
        self.windex = self.wclen - 1
        self.wc[self.windex][0].destroy()
        self.wc[self.windex][1].destroy()
        del self.wc[self.windex]

    def rem_ttape(self):

        self.tclen = len(self.tc)
        self.tindex = self.tclen - 1
        self.tc[self.tindex][0].destroy()
        self.tc[self.tindex][1].destroy()
        del self.tc[self.tindex]

    def rem_autape(self):

        self.auclen = len(self.auc)
        self.auindex = self.auclen - 1
        self.auc[self.auindex][0].destroy()
        self.auc[self.auindex][1].destroy()
        del self.auc[self.auindex]


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

    def on_close(self):
        config = cp.ConfigParser()
        config.read('param.ini')

        # resets necessary config on window close
        config.set('DEFAULT', 'wcasecount', '1')
        config.set('DEFAULT', 'tcasecount', '1')
        config.set('DEFAULT', 'aucasecount', '1')


        with open('param.ini', 'w') as configfile:
            config.write(configfile)
        root.destroy()



root = tk.Tk()
root.geometry('600x600+200+200')

root.style = ttk.Style()
root.style.theme_use("default")

menu = tk.Menu(root)
root.config(menu=menu)

app = Main_Window()
app.mainloop()