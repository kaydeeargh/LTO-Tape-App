import tkinter as tk
import tkinter.ttk as ttk
import configparser as cp
import os
import datetime

windows_placeholder = None

class MainWindow(tk.Frame):

    def __init__(self):
        super().__init__()

        self.column_placeholder = 0

        self.config = cp.ConfigParser()
        self.config.read('param.ini')

        self.image_use = [tk.PhotoImage(file='copy.png')]

        self.tape_info = []

        self.dates()

        # START OF FRAME CREATION
        # frame for W tape scans. It's own frame is required for organization and multiples.
        self.wframe = ttk.LabelFrame(labelanchor='n', text="Windows Tapes", height=600, width=200)
        self.wframe.columnconfigure(0, weight=1)
        self.wframe.grid(row=10, column=0, sticky="w")

        # frame for T tapes. It's own frame is required for organization and multiples.
        self.tframe = ttk.LabelFrame(labelanchor='n', text="T Tapes", height=600, width=200)
        self.tframe.columnconfigure(0, weight=1)
        self.tframe.grid(row=20, column=0, sticky="w")

        # frame for AU tapes. It's own frame is required for organization and multiples.
        self.auframe = ttk.LabelFrame(labelanchor='n', text="AU Tapes", height=600, width=200)
        self.auframe.columnconfigure(0, weight=1)
        self.auframe.grid(row=30, column=0, sticky="w")

        # frame for G tapes. Gridded based on day of week.
        self.gframe = ttk.LabelFrame(labelanchor='n', text="G Tapes", height=600, width=200)

        # frame for MF tapes. Gridded based on day of week.
        self.mfframe = ttk.LabelFrame(labelanchor='n', text="MF Tapes", height=600, width=200)
        # END OF FRAME CREATION

        # list of frame IDs for later reference
        self.frame_id = (self.wframe.winfo_id(), self.tframe.winfo_id(), self.auframe.winfo_id(), self.gframe.winfo_id(), self.mfframe.winfo_id())

        # Frame gridding based on day of the week
        if self.dayofweek != 'Sunday' and self.dayofweek != 'Saturday':
            self.gframe.columnconfigure(0, weight=1)
            self.gframe.grid(row=10, column=1, sticky="e")
            self.tapes_widget(0, self.gframe)

        if self.dayofweek == 'Monday':
            self.mfframe.columnconfigure(0, weight=1)
            self.mfframe.grid(row=20, column=1, sticky="e")
            self.tapes_widget(0, self.mfframe)

        self.menubar()
        self.tapes_widget(self.column_placeholder, self.wframe)
        self.tapes_widget(self.column_placeholder, self.tframe)
        self.tapes_widget(self.column_placeholder, self.auframe)

        self.username = os.getlogin()

        # return dates for IronMountain
        self.w_return = datetime.date.today() + datetime.timedelta(10)
        self.t_return = datetime.date.today() + datetime.timedelta(9)
        self.au_return = datetime.date.today() + datetime.timedelta(13)
        self.mf_return = datetime.date.today() + datetime.timedelta(14)

        # formats return date for preference
        self.w_return_format = "%d/%d/%d" % (self.w_return.month, self.w_return.day, self.w_return.year)
        self.t_return_format = "%d/%d/%d" % (self.t_return.month, self.t_return.day, self.t_return.year)
        self.au_return_format = "%d/%d/%d" % (self.au_return.month, self.au_return.day, self.au_return.year)
        self.mf_return_format = "%d/%d/%d" % (self.mf_return.month, self.mf_return.day, self.mf_return.year)

        # places dates in ini file for formatting
        self.config.set('DEFAULT', 'datemonth', '%s' % self.datemonth)
        self.config.set('DEFAULT', 'dateyear', '%s' % self.dateyear)
        self.config.set('DEFAULT', 'wreturn', '%s' % self.w_return_format)
        self.config.set('DEFAULT', 'treturn', '%s' % self.t_return_format)
        self.config.set('DEFAULT', 'aureturn', '%s' % self.au_return_format)
        self.config.set('DEFAULT', 'mfreturn', '%s' % self.mf_return_format)
        self.config.set('DEFAULT', 'username', '%s' % self.username)
        with open('param.ini', 'w') as configfile:
            self.config.write(configfile)

        # Runs a cleanup function on window close
        root.protocol("WM_DELETE_WINDOW", self.on_close)

        # Keeps the window from being resized by the user
        root.resizable(False, False)

    def menubar(self):

        addmenu = tk.Menu(menu, tearoff=0)
        remmenu = tk.Menu(menu, tearoff=0)
        editmenu = tk.Menu(menu, tearoff=0)

        menu.add_cascade(label="Edit", menu=editmenu)
        menu.add_cascade(label="Add", menu=addmenu)
        menu.add_cascade(label="Remove", menu=remmenu)

        addmenu.add_command(label="W Tapes", command=lambda: self.add_tape('W Tape'))
        addmenu.add_command(label="T Tapes", command=lambda: self.add_tape('T Tape'))
        addmenu.add_command(label="AU Tapes", command=lambda: self.add_tape('AU Tape'))

        remmenu.add_command(label="W Tapes", command=lambda: self.rem_tape('W Tape'))
        remmenu.add_command(label="T Tapes", command=lambda: self.rem_tape('T Tape'))
        remmenu.add_command(label="AU Tapes", command=lambda: self.rem_tape('AU Tape'))

        editmenu.add_command(label="Settings", command=self.preferences)

        submit = tk.Button(text='SUBMIT', command=self.create_doc).grid(row=100, column=0, columnspan=2, sticky='wens')

    def preferences(self):
        pref_window = tk.Toplevel()

    def add_tape(self, code):

        if code == 'W Tape':
            self.tapes_widget(self.column_placeholder, self.wframe)

        if code == 'T Tape':
            self.tapes_widget(self.column_placeholder, self.tframe)

        if code == 'AU Tape':
            self.tapes_widget(self.column_placeholder, self.auframe)

    def rem_tape(self, code):

        if code == 'W Tape':
            for i, item in reversed(list(enumerate(self.tape_info))):
                if self.frame_id[0] in item:
                    for x in range(3):
                        item[x].destroy()
                    del self.tape_info[i]
                    break

        elif code == 'T Tape':
            for i, item in reversed(list(enumerate(self.tape_info))):
                if self.frame_id[1] in item:
                    for x in range(3):
                        item[x].destroy()
                    del self.tape_info[i]
                    break

        elif code == 'AU Tape':
            for i, item in reversed(list(enumerate(self.tape_info))):
                if self.frame_id[2] in item:
                    for x in range(3):
                        item[x].destroy()
                    del self.tape_info[i]
                    break

    def tapes_widget(self, x, frame):

        # entry box for W tape case ID
        self.tape_case = ttk.Entry(frame)
        self.tape_case.insert(0, "Scan Case")
        self.tape_case.grid(row=0, column=x, sticky="w", padx=10)
        self.tape_case.bind('<Button-1>', self.clear_entry)

        # text boxes for windows tape scans
        self.tape_text = tk.Text(frame, height=8, width=10)
        self.tape_text.grid(row=1, column=x, columnspan=2, sticky="wens", padx=10, pady=10)

        # This button will be to copy everything in the Text box to be pasted externally
        x += 1
        self.copy_button = tk.Button(frame, height=25, width=25)
        self.copy_button.grid(row=0, column=x, sticky="w", padx=10)
        self.photo_button = self.image_use[0]
        self.copy_button.config(image=self.photo_button)
        self.copy_button.bind('<Button-1>', self.copy_buttons)


        self.tape_info.append((self.tape_case, self.tape_text, self.copy_button, self.copy_button.winfo_id(), frame.winfo_id()))
        self.column_placeholder += 2

    def dates(self):
        self.datenow = datetime.datetime.now()
        self.datemonth = self.datenow.month
        self.dateday = self.datenow.day
        self.dateyear = self.datenow.year
        self.dayofweek = self.datenow.strftime("%A")

    def checker(self):
        pass
        print(int(self.tape_text.index('end-1c').split('.')[0]))


    def create_doc(self):

        """The below code creates a document, pulls the data from the entry and text widgets and formats it as needed"""
        os.chdir("C:\\Users\\%s\\Desktop\\" % (self.username))
        outgoing = open('Outgoing_%s%s%s.txt' % (self.dateyear, self.datemonth, self.dateday), 'w+')  ## see line243 ******Fix formatting on single digit month*******

        # Lists to organize the output
        w_group = [item for item in self.tape_info if self.frame_id[0] in item]
        t_group = [item for item in self.tape_info if self.frame_id[1] in item]
        au_group = [item for item in self.tape_info if self.frame_id[2] in item]
        g_group = [item for item in self.tape_info if self.frame_id[3] in item]
        mf_group = [item for item in self.tape_info if self.frame_id[4] in item]

        reorg_list = w_group + t_group + au_group
        while len(reorg_list) < len(self.tape_info):
            if g_group:
                reorg_list = reorg_list + g_group
            if mf_group:
                reorg_list = reorg_list + mf_group

        # for x in range(0, len(reorg_list)):
        for item in reorg_list:
            if self.frame_id[0] == item[4]:
                in_case = item[0].get()
                in_text = item[1].get(1.0, 'end')
                outgoing.write(in_case + '\n' + self.config.get('SETTINGS', 'w_line') + '\n' + in_text + '\n')
            if self.frame_id[1] == item[4]:
                in_case = item[0].get()
                in_text = item[1].get(1.0, 'end')
                if self.dayofweek == 'Monday':
                    outgoing.write(
                        in_case + '\n' + self.config.get('SETTINGS', 't_line_monday') + '\n' + in_text + '\n')
                else:
                    outgoing.write(
                        in_case + '\n' + self.config.get('SETTINGS', 't_line_main') + '\n' + in_text + '\n')
            if self.frame_id[2] == item[4]:
                in_case = item[0].get()
                in_text = item[1].get(1.0, 'end')
                outgoing.write(in_case + '\n' + self.config.get('SETTINGS', 'au_line') + '\n' + in_text + '\n')
            if self.frame_id[3] == item[4]:
                in_case = item[0].get()
                in_text = item[1].get(1.0, 'end')
                outgoing.write(in_case + '\n' + self.config.get('SETTINGS', 'g_line') + '\n' + in_text + '\n')
            if self.frame_id[4] == item[4]:
                in_case = item[0].get()
                in_text = item[1].get(1.0, 'end')
                outgoing.write(in_case + '\n' + self.config.get('SETTINGS', 'mf_line') + '\n' + in_text + '\n')

        outgoing.close()
        os.startfile(r'C:\Users\%s\Desktop\Outgoing_%s%s%s.txt' % (self.username, self.dateyear, self.datemonth, self.dateday)) ## see line 198******Fix formatting on single digit month*******

    def copy_buttons(self, event=None):
        indx = event.widget.winfo_id()
        root.clipboard_clear()

        for item in self.tape_info:
            if indx in item:
                copy_text = item[1].get(1.0, 'end')
                if self.frame_id[0] == item[4]:
                    root.clipboard_append(str(datetime.date.today().strftime("%m-%d-%y")) + ' ' + self.config.get('SETTINGS', 'w_line') + '\n' + copy_text)
                elif self.frame_id[1] == item[4]:
                    if self.dayofweek == 'Monday':
                        root.clipboard_append(str(datetime.date.today().strftime("%m-%d-%y")) + ' ' + self.config.get('SETTINGS', 't_line_monday') + '\n' + copy_text)
                    else:
                        root.clipboard_append(str(datetime.date.today().strftime("%m-%d-%y")) + ' ' + self.config.get('SETTINGS', 't_line_main') + '\n' + copy_text)
                elif self.frame_id[2] == item[4]:
                    root.clipboard_append(str(datetime.date.today().strftime("%m-%d-%y")) + ' ' + self.config.get('SETTINGS', 'au_line') + '\n' + copy_text)
                elif self.frame_id[3] == item[4]:
                    root.clipboard_append(str(datetime.date.today().strftime("%m-%d-%y")) + ' ' + self.config.get('SETTINGS', 'g_line') + '\n' + copy_text)
                elif self.frame_id[4] == item[4]:
                    root.clipboard_append(str(datetime.date.today().strftime("%m-%d-%y")) + ' ' + self.config.get('SETTINGS', 'mf_line') + '\n' + copy_text)

    # method to delete default text when mouse button is pressed
    def clear_entry(self, event=None):

        entry = event.widget.get()
        if entry == 'Scan Case':
            event.widget.delete(0, 'end')

    def on_close(self):

        root.destroy()


root = tk.Tk()

root.style = ttk.Style()
root.style.theme_use("default")
root.update()
root.minsize(root.winfo_width(),root.winfo_height())

menu = tk.Menu(root)
root.config(menu=menu)

app = MainWindow()
app.mainloop()
