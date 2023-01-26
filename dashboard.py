from sqlalchemy.orm import sessionmaker
from models import Todo, engine
from tkinter import Label, Entry, Button, Listbox, END, IntVar, messagebox

session = sessionmaker(bind=engine)()

class Dashboard:
    def __init__(self, main,user):
        self.selection = IntVar()
        self.todos = []
        self.user = user
        self.main = main
        self.main.geometry("800x400")
        self.label = Label(self.main, text="Enter the Task").place(x=100, y=20)
        self.todo_entry = Entry(self.main, width=50)
        self.todo_entry.place(x=220, y=20)
        self.add_button = Button(self.main, text="Add todo",width=15, height=2, command=self.add_todo).place(x=50,y=60)
        self.edit_button = Button(self.main, text="Edit todo",width=15, height=2, command=self.edit_todo).place(x=235,y=60)
        self.delete_button = Button(self.main, text="Delete todo", width=15, height=2, command=self.delete_todo).place(x=420,y=60)
        self.delete_all_button = Button(self.main, text="Delete All", width=15, height=2, command=self.delete_all_todos).place(x=600,y=60)
        self.list_box = Listbox(self.main, selectmode="single",width=97)
        self.list_box.place(x=10, y=120)
        self.list_box.bind("<<ListboxSelect>>", self.mark_todo)
        self.change_status_button = Button(self.main, text="Change todo status", width=90,command=self.change_todo_status).place(x=20, y=310)
        self.exit_button = Button(self.main, text="Exit", width=90, command=self.main.destroy).place(x=20,y=350)
        self._show_todos()
    
    def _show_todos(self):
        self.list_box.delete(0, END)
        self.todos = []
        for todo in session.query(Todo).all():
            if todo.user_id == self.user.id:
                self.todos.append(todo)
        for index,todo in enumerate(self.todos):
                todo_string = f"{index} {todo.todo} {todo.status}"
                self.list_box.insert(END,todo_string)
                
    def mark_todo(self, event):
       todos = event.widget
       try:
           index = todos.curselection()[0]
       except IndexError:
           pass
       else:
           self.selection.set(index)
           self.todo_entry.delete(0, END)
           self.todo_entry.insert(0, self.todos[self.selection.get()].todo)
 
    def add_todo(self):
        todo = Todo(todo=self.todo_entry.get(), status="Active", user_id=self.user.id)
        session.add(todo)
        session.commit()
        self._show_todos()

    def edit_todo(self):
        todo = session.query(Todo).filter(Todo.id==self.todos[self.selection.get()].id).one()
        todo.todo = self.todo_entry.get()
        session.commit()
        self._show_todos()
    
    def change_todo_status(self):
        todo = session.query(Todo).filter(Todo.id==self.todos[self.selection.get()].id).one()
        if todo.status == "Active":
            todo.status = "Not active"
        else:
            todo.status = "Active"
        session.commit()
        self._show_todos()

    def delete_todo(self):
        if messagebox.askquestion("Delete todo", "Do you wanna delete todo? ") == "yes":
            self.list_box.delete(self.selection.get())
            print(self.todos[self.selection.get()].id)
            todo = session.query(Todo).filter(Todo.id==self.todos[self.selection.get()].id).one()
            session.delete(todo)
            session.commit()

    def delete_all_todos(self):
        if messagebox.askquestion("Delete todos", "Do you wanna delete all todos? ") == "yes":
            for todo in self.todos:
                session.delete(todo)
                session.commit()
            self.list_box.delete(0, END)
    
