from sqlalchemy.orm import sessionmaker
from models import engine
from login import Login
from register import Register
from dashboard import Dashboard
from tkinter import *

session = sessionmaker(bind=engine)()

class App:
    def __init__(self,main):
        self.user = None
        self.main = main
        self.login()
        self.main.mainloop()
    
    def logged_user(self, user):
        self.user = user
        print(self.user.todos)
    
    def login(self):
        for i in self.main.winfo_children():
            i.destroy()
        self.view = Login(self.main, self.register, self.dashboard, self.logged_user)

    def register(self):
        for i in self.main.winfo_children():
            i.destroy()
        self.view = Register(self.main, self.login)
    
    def dashboard(self):
        for i in self.main.winfo_children():
            i.destroy()
        print(self.user)
        self.view = Dashboard(self.main, self.user)
    
root = Tk()
app = App(root)

