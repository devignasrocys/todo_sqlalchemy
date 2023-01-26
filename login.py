from sqlalchemy.orm import sessionmaker
from models import User, engine
from tkinter import messagebox, Label, Entry, Button

session = sessionmaker(bind=engine)()

class Login:
    def __init__(self, main, to_register_page, to_dashboard, logged_user):
        self.logged_user = logged_user
        self.to_dashboard_page = to_dashboard
        self.main = main
        self.main.geometry("500x300")
        self.username_label = Label(self.main, text="Username", width=20).place(x=170, y=40)
        self.username_entry = Entry(self.main, width=20)
        self.username_entry.place(x=170, y=60)
        self.pasword_label = Label(self.main, text="Password", width=20).place(x=170, y=80)
        self.password_entry = Entry(self.main, width=20, show="*")
        self.password_entry.place(x=170, y=100)
        self.login_btn = Button(self.main, text="Login", width=20, height=1, command=self.login_user).place(x=160, y=140)
        self.register_btn = Button(self.main, text="Register", width=20, height=1, command=to_register_page).place(x=160, y=180)
    
    def login_user(self):
        # find user by username
        user = session.query(User).filter(User.username==self.username_entry.get()).first()
        if user:
            # check passwords
            if user.password == self.password_entry.get():
                self.logged_user(user)
                self.to_dashboard_page()
            else:
                messagebox.showwarning("ok", "Wrong password")
        else:
            messagebox.showwarning("ok", "User doesn't exit")


