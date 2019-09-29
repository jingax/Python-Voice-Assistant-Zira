from tkinter import *
from PIL import ImageTk, Image

class GUI(Tk):
    def __init__(self):
        super().__init__()
        # Status bar variable
        self.back_image = PhotoImage(file="backg.png")
        self.back_image2 = PhotoImage(file="backg2.png")
        self.background_label = Label(self, image=self.back_image)
        self.background_label.pack(side='top', fill='both', expand='yes')
        self.status = StringVar()
        self.msg_var = StringVar()
        self.status.set("ready")
        self.msg_var.set("")
        self.status_bar = Label(self.background_label, textvar=self.status, relief=SUNKEN, anchor="w")
        self.msg_box = Text(self.background_label, height=18, width=110,font=('Arial', 12), bg="grey")

    def set_status(self, status_value, color):
        self.status.set(f"{status_value}")
        self.status_bar.config(bg=f"{color}")
        self.status_bar.update()

    def set_msg(self, message):
        # self.msg_var.set(f"{message}")
        # self.msg_box.update()
        self.msg_box.insert(END, f"{message}\n")
        self.msg_box.update()


    def create_statusbar_msgbox(self):
        self.status_bar.pack(fill=X, side=BOTTOM)
        self.msg_box.pack(side=BOTTOM, padx=10, pady=10)
