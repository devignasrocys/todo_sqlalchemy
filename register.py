from sqlalchemy.orm import sessionmaker
from models import User, engine
from tkinter import messagebox, Label, Entry, Button

session = sessionmaker(bind=engine)()

class Register:
    def __init__(self, main, to_login):
        self.to_login_page = to_login
        self.main = main
        self.main.geometry("500x300")
        self.username_label = Label(self.main, text="Username", width=20).place(x=170, y=40)
        self.username_entry = Entry(self.main, width=20)
        self.username_entry.place(x=170, y=60)
        self.pasword_label = Label(self.main, text="Password", width=20).place(x=170, y=80)
        self.password_entry = Entry(self.main, width=20, show="*")
        self.password_entry.place(x=170, y=100)
        self.repeat_pasword_label = Label(self.main, text="Repeat Password", width=20).place(x=170, y=120)
        self.repeat_password_entry = Entry(self.main, width=20, show="*")
        self.repeat_password_entry.place(x=170, y=140)
        self.register_btn = Button(self.main, text="Register", width=20, height=1, command=self.register_user).place(x=160, y=180)
    
    def register_user(self):
        if self.password_entry.get() != self.repeat_password_entry.get():
            messagebox.showwarning("ok", "Passwords does'nt match ")
        elif self.username_entry.get() == "" or self.password_entry.get() == "" or self.repeat_password_entry.get == "":
            messagebox.showwarning("ok", "Can't be empty entries")
        elif self.password_entry.get() == self.repeat_password_entry.get():
            user = User(username=self.username_entry.get(),password=self.password_entry.get())
            session.add(user)
            session.commit()
            self.to_login_page()



