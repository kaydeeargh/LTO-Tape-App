import tkinter as tk
import tkinter.ttk as ttk
import configparser as cp
import os
from datetime import datetime, date


class Main_Window(tk.Frame):

    def __init__(self):
        super().__init__()
        self.image_use = [tk.PhotoImage(file='copy.png')]
        self.wc = []
        self.tc = []
        self.auc = []

        self.widgets()
        self.w_widgets()
        self.t_widgets()
        self.au_widgets()
        self.dates()
        self.g_widget()
        self.mf_widget()
        self.create_doc()


        root.protocol("WM_DELETE_WINDOW", self.on_close)
        root.resizable(False, False)




    def widgets(self):

        addMenu = tk.Menu(menu, tearoff=0)
        remMenu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="Add", menu=addMenu)
        menu.add_cascade(label="Remove", menu=remMenu)
        addMenu.add_command(label="W Tapes", command=lambda: self.add_tape('W Tape'))
        addMenu.add_command(label="T Tapes", command=lambda: self.add_tape('T Tape'))
        addMenu.add_command(label="AU Tapes", command=lambda: self.add_tape('AU Tape'))

        remMenu.add_command(label="W Tapes", command=lambda: self.rem_tape('W Tape'))
        remMenu.add_command(label="T Tapes", command=lambda: self.rem_tape('T Tape'))
        remMenu.add_command(label="AU Tapes", command=lambda: self.rem_tape('AU Tape'))

        self.submit = tk.Button(text='SUBMIT', command=self.create_doc).grid(row=100, column=0, columnspan=2, sticky='wens')


    def add_tape(self, code):

        config = cp.ConfigParser()
        config.read('param.ini')
        self.curr_wplace = config.getint('DEFAULT', 'wcasecount')
        self.curr_tplace = config.getint('DEFAULT', 'tcasecount')
        self.curr_auplace = config.getint('DEFAULT', 'aucasecount')

        if code == 'W Tape':
            self.wcase = ttk.Entry(self.wframe)
            self.wcase.insert(0, "Scan Case")
            self.wcase.grid(row=0, column=self.curr_wplace, sticky='w', padx=10)
            self.wcase.bind('<Button-1>', self.clear_entry)

            # # text boxes for windows tape scans
            self.wtext = tk.Text(self.wframe, height=8, width=10)
            self.wtext.grid(row=1, column=self.curr_wplace, columnspan=2, sticky="wens", padx=10, pady=10)

            self.curr_wplace += 1
            self.wbutt = tk.Button(self.wframe, height=25, width=25)
            self.wbutt.grid(row=0, column=self.curr_wplace, sticky="w", padx=10)
            self.photo_butt = self.image_use[0]
            self.wbutt.config(image=self.photo_butt)
            self.curr_wplace -= 1

            self.wctuple = (self.wcase.winfo_id(), self.wtext.winfo_id(), self.wbutt.winfo_id())
            self.wc.append(self.wctuple)

            self.curr_wplace += 2
            config.set('DEFAULT', 'wcasecount', '%s' % self.curr_wplace)
            with open('param.ini', 'w') as configfile:
                config.write(configfile)



        if code == 'T Tape':
            self.tcase = ttk.Entry(self.tframe)
            self.tcase.insert(0, "Scan Case")
            self.tcase.grid(row=0, column=self.curr_tplace, sticky='w', padx=10)
            self.tcase.bind('<Button-1>', self.clear_entry)

            # # text boxes for windows tape scans
            self.ttext = tk.Text(self.tframe, height=8, width=10)
            self.ttext.grid(row=1, column=self.curr_tplace, columnspan=2, sticky="wens", padx=10, pady=10)

            self.curr_tplace += 1
            self.tbutt = tk.Button(self.tframe, height=25, width=25)
            self.tbutt.grid(row=0, column=self.curr_tplace, sticky="w", padx=10)
            self.photo_butt = self.image_use[0]
            self.tbutt.config(image=self.photo_butt)
            self.curr_tplace -= 1

            self.tctuple = (self.tcase.winfo_id(), self.ttext.winfo_id(), self.tbutt.winfo_id())
            self.tc.append(self.tctuple)

            self.curr_tplace += 2
            config.set('DEFAULT', 'tcasecount', '%s' % (self.curr_tplace))
            with open('param.ini', 'w') as configfile:
                config.write(configfile)

        if code == 'AU Tape':
            self.aucase = ttk.Entry(self.auframe)
            self.aucase.insert(0, "Scan Case")
            self.aucase.grid(row=0, column=self.curr_auplace, padx=10)
            self.aucase.bind('<Button-1>', self.clear_entry)

            # # text boxes for windows tape scans
            self.autext = tk.Text(self.auframe, height=8, width=10)
            self.autext.grid(row=1, column=self.curr_auplace, columnspan=2, sticky="wens", padx=10, pady=10)

            self.curr_auplace += 1
            self.aubutt = tk.Button(self.auframe, height=25, width=25)
            self.aubutt.grid(row=0, column=self.curr_auplace, sticky="w", padx=10)
            self.photo_butt = self.image_use[0]
            self.aubutt.config(image=self.photo_butt)
            self.curr_auplace -= 1

            self.auctuple = (self.aucase.winfo_id(), self.autext.winfo_id(), self.aubutt.winfo_id())
            self.auc.append(self.auctuple)

            self.curr_auplace += 2
            config.set('DEFAULT', 'aucasecount', '%s' % (self.curr_auplace))
            with open('param.ini', 'w') as configfile:
                config.write(configfile)

    def rem_tape(self, code):

        if code == 'W Tape':
            self.wclen = len(self.wc)
            self.windex = self.wclen - 1
            self.wc[self.windex][0].destroy()
            self.wc[self.windex][1].destroy()
            self.wc[self.windex][2].destroy()
            del self.wc[self.windex]

        elif code == 'T Tape':
            self.tclen = len(self.tc)
            self.tindex = self.tclen - 1
            self.tc[self.tindex][0].destroy()
            self.tc[self.tindex][1].destroy()
            self.tc[self.tindex][2].destroy()
            del self.tc[self.tindex]

        elif code == 'AU Tape':
            self.auclen = len(self.auc)
            self.auindex = self.auclen - 1
            self.auc[self.auindex][0].destroy()
            self.auc[self.auindex][1].destroy()
            self.auc[self.auindex][2].destroy()
            del self.auc[self.auindex]

    def w_widgets(self):

        # frame for windows tape scans. It's own frame is required for organization and multiples.
        self.wframe = ttk.LabelFrame(labelanchor='n', text="Windows Tapes", height=600, width=200)
        self.wframe.columnconfigure(0, weight=1)
        self.wframe.grid(row=10, column=0, sticky="w")

        # entry box for W tape case ID
        self.wcase = ttk.Entry(self.wframe)
        self.wcase.insert(0, "Scan Case")
        self.wcase.grid(row=0, column=0, sticky="w", padx=10)
        self.wcase.bind('<Button-1>', self.clear_entry)

        # text boxes for windows tape scans
        self.wtext = tk.Text(self.wframe, height=8, width=10)
        self.wtext.grid(row=1, columnspan=2, sticky="wens", padx=10, pady=10)

        """ This button will be to copy everything in the Text box to be pasted externally"""
        self.wbutt = tk.Button(self.wframe, height=25, width=25)
        self.wbutt.grid(row=0, column=1, sticky="w", padx=10)
        self.wcopyicon = tk.PhotoImage(file='copy.png')
        self.wbutt.config(image=self.wcopyicon)
        self.wbutt.bind('<Button-1>', self.copy_buttons)

        self.wctuple = (self.wcase, self.wtext, self.wbutt.winfo_id())
        self.wc.append(self.wctuple)

    def t_widgets(self):

        # frame for T tapes. It's own frame is required for organization and multiples.
        self.tframe = ttk.LabelFrame(labelanchor='n', text="T Tapes", height=600, width=200)
        self.tframe.columnconfigure(0, weight=1)
        self.tframe.grid(row=20, column=0, sticky="w")

        # entry box for T tape case ID
        self.tcase = ttk.Entry(self.tframe)
        self.tcase.insert(0, "Scan Case")
        self.tcase.grid(row=0, column=0, sticky="w", padx=10)
        self.tcase.bind('<Button-1>', self.clear_entry)

        # text box for t tape scans
        self.ttext = tk.Text(self.tframe, height=8, width=10)
        self.ttext.grid(row=1, columnspan=2, sticky="wens", padx=10, pady=10)

        self.tbutt = tk.Button(self.tframe, height=25, width=25)
        self.tbutt.grid(row=0, column=1, sticky="w", padx=10)
        self.tcopyicon = tk.PhotoImage(file='copy.png')
        self.tbutt.config(image=self.tcopyicon)
        self.tbutt.bind('<Button-1>', self.copy_buttons)

        self.tctuple = (self.tcase, self.ttext, self.tbutt.winfo_id())
        self.tc.append(self.tctuple)



    def au_widgets(self):
        # frame for T tapes. It's own frame is required for organization and multiples.
        self.auframe = ttk.LabelFrame(labelanchor='n', text="AU Tapes", height=600, width=200)
        self.auframe.columnconfigure(0, weight=1)
        self.auframe.grid(row=30, column=0, sticky="w")

        # entry box for T tape case ID
        self.aucase = ttk.Entry(self.auframe)
        self.aucase.insert(0, "Scan Case")
        self.aucase.grid(row=0, column=0, sticky="w", padx=10)
        self.aucase.bind('<Button-1>', self.clear_entry)

        # text box for t tape scans
        self.autext = tk.Text(self.auframe, height=8, width=10)
        self.autext.grid(row=1, columnspan=2, sticky="wens", padx=10, pady=10)

        self.aubutt = tk.Button(self.auframe, height=25, width=25)
        self.aubutt.grid(row=0, column=1, sticky="w", padx=10)
        self.aucopyicon = tk.PhotoImage(file='copy.png')
        self.aubutt.config(image=self.aucopyicon)
        self.aubutt.bind('<Button-1>', self.copy_buttons)

        self.auctuple = (self.aucase, self.autext, self.aubutt.winfo_id())
        self.auc.append(self.auctuple)

    def g_widget(self):
        if self.dayofweek != 'Sunday' and self.dayofweek != 'Saturday':
            self.gframe = ttk.LabelFrame(labelanchor='n', text="G Tapes", height=600, width=200)
            self.gframe.columnconfigure(0, weight=1)
            self.gframe.grid(row=10, column=1, sticky="e")

            # entry box for G tape case ID
            self.gcase = ttk.Entry(self.gframe)
            self.gcase.insert(0, "Scan Case")
            self.gcase.grid(row=0, column=0, sticky="w", padx=10)
            self.gcase.bind('<Button-1>', self.clear_entry)

            # text box for G tape scans
            self.gtext = tk.Text(self.gframe, height=8, width=10)
            self.gtext.grid(row=1, columnspan=2, sticky="wens", padx=10, pady=10)

            self.gbutt = tk.Button(self.gframe, height=25, width=25)
            self.gbutt.grid(row=0, column=1, sticky="w", padx=10)
            self.gcopyicon = tk.PhotoImage(file='copy.png')
            self.gbutt.config(image=self.gcopyicon)

    def mf_widget(self):
        if self.dayofweek == 'Monday':
            self.mfframe = ttk.LabelFrame(labelanchor='n', text="MF Tapes", height=600, width=200)
            self.mfframe.columnconfigure(0, weight=1)
            self.mfframe.grid(row=20, column=1, sticky="e")

            # entry box for G tape case ID
            self.mfcase = ttk.Entry(self.mfframe)
            self.mfcase.insert(0, "Scan Case")
            self.mfcase.grid(row=0, column=0, sticky="w", padx=10)
            self.mfcase.bind('<Button-1>', self.clear_entry)

            # text box for G tape scans
            self.mftext = tk.Text(self.mfframe, height=8, width=10)
            self.mftext.grid(row=1, columnspan=2, sticky="wens", padx=10, pady=10)

            self.mfbutt = tk.Button(self.mfframe, height=25, width=25)
            self.mfbutt.grid(row=0, column=1, sticky="w", padx=10)
            self.mfcopyicon = tk.PhotoImage(file='copy.png')
            self.mfbutt.config(image=self.mfcopyicon)

    def dates(self):
        self.datenow = datetime.today()
        self.datemonth = self.datenow.month
        self.dateday = self.datenow.day
        self.dateyear = self.datenow.year
        self.dayofweek = date.today().strftime("%A")

    def create_doc(self):

        """The below code creates a document, pulls the data from the entry and text widgets and formats it as needed"""
        self.outgoing = open(r'C:\Users\Public\Desktop\Outgoing_%s%s%s.txt' %(self.dateyear,self.datemonth,self.dateday), 'w')

        len_w = len(self.wc)
        len_t = len(self.tc)
        len_au = len(self.auc)

        self.username = os.getlogin()

        self.wreturn = self.datenow.day + 10
        self.treturn = self.datenow.day + 9
        self.aureturn = self.datenow.day + 13
        self.mfreturn = self.datenow.day + 14

        self.wdoc = 'PFS, RCP WINDOWS(WLxxxx)'
        self.tdoc = 'PFS, RCP UNIX(Txxxxx)'
        self.rdoc = 'CSI/RPG Unix(Rxxxxx)'
        self.mfdoc = 'PFS/Molded Fiber AS/400(MFPDxx and MFDDxx)'
        self.audoc = 'Automotive UNIX(AUxxxx)'
        self.csdoc = 'CSI AS/400(CSxxxx)'
        self.hdoc = 'Automotive AS/400(HBxxxx)'

        self.w_line = 'SENT DAILY %s TAPES RETURN ON %s/%s/%s Locked by: %s' %(self.wdoc, self.datemonth, self.wreturn, self.dateyear, self.username)
        self.t_line = 'SENT DAILY %s, %s AND %s TAPES RETURN ON %s/%s/%s Locked by: %s' %(self.tdoc, self.rdoc, self.mfdoc, self.datemonth, self.treturn, self.dateyear, self.username)
        self.mf_line = 'SENT WEEKLY %s TAPES RETURN ON %s/%s/%s & Locked by: %s' %(self.mfdoc, self.datemonth, self.mfreturn, self.dateyear, self.username)
        self.au_line = 'SENT DAILY %s, %s AND %s TAPES RETURN ON %s/%s/%s Locked by: %s' %(self.audoc, self.csdoc, self.hdoc, self.datemonth, self.aureturn, self.dateyear, self.username)

        for x in range(0, len_w):
            in_wcase = self.wc[x][0].get()
            in_wtext = self.wc[x][1].get(1.0, 'end')
            self.outgoing.write(in_wcase + '\n' + self.w_line + '\n' + in_wtext + '\n')

        for x in range(0, len_t):
            in_tcase = self.tc[x][0].get()
            in_ttext = self.tc[x][1].get(1.0, 'end')
            self.outgoing.write(in_tcase + '\n' + self.t_line + '\n' + in_ttext + '\n')

        for x in range(0, len_au):
            in_aucase = self.auc[x][0].get()
            in_autext = self.auc[x][1].get(1.0, 'end')
            self.outgoing.write(in_aucase + '\n' + self.au_line + '\n' + in_autext + '\n')

        self.outgoing.close()

    def copy_buttons(self, event=None):
        indx = event.widget.winfo_id()
        widgetset = [item for item in self.wc if indx in item]
        if widgetset:
            root.clipboard_clear()
            copy_w_text = widgetset[0][1].get(1.0, 'end')
            root.clipboard_append(str(datetime.now().strftime("%m-%d-%y")) + ' ' + self.w_line + '\n' + copy_w_text)
        widgetset = [item for item in self.tc if indx in item]
        if widgetset:
            root.clipboard_clear()
            copy_t_text = widgetset[0][1].get(1.0, 'end')
            root.clipboard_append(str(datetime.now().strftime("%m-%d-%y")) + ' ' + self.t_line + '\n' + copy_t_text)
        widgetset = [item for item in self.auc if indx in item]
        if widgetset:
            root.clipboard_clear()
            copy_au_text = widgetset[0][1].get(1.0, 'end')
            root.clipboard_append(str(datetime.now().strftime("%m-%d-%y")) + ' ' + self.au_line + '\n' + copy_au_text)












    # method to delete default text when mouse button is pressed
    def clear_entry(self, event=None):

        entry = event.widget.get()
        if entry == 'Scan Case':
            event.widget.delete(0, 'end')

    def on_close(self):
        config = cp.ConfigParser()
        config.read('param.ini')

        # resets necessary config on window close
        config.set('DEFAULT', 'wcasecount', '2')
        config.set('DEFAULT', 'tcasecount', '2')
        config.set('DEFAULT', 'aucasecount', '2')
        config.set('DEFAULT', 'imagecount', '0')


        with open('param.ini', 'w') as configfile:
            config.write(configfile)
        root.destroy()



root = tk.Tk()


root.style = ttk.Style()
root.style.theme_use("default")
root.update()
root.minsize(root.winfo_width(),root.winfo_height())

menu = tk.Menu(root)
root.config(menu=menu)

app = Main_Window()
app.mainloop()