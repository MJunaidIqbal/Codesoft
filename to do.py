from tkinter import *
from tkinter import ttk


class todo:
    def __init__(self, root):
        self.root=root
        self.root.title("To-Do list")
        self.root.geometry('1000x620+320+100')
        
        self.label=Label(self.root, text="First Task To-do App", font='Rust, 25 bold ', width=10, bd=5, fg="black")
        self.label.pack(side="top", fill=BOTH)
        
        self.label2=Label(self.root, text="Add task", font='arial, 18 bold', width=10, bd=5, fg="black")
        self.label2.place(x="15", y='100')
        
        self.text= Text(self.root, height=2, bd=5, font="ariel, 18 bold", width=40)
        self.text.place(x=30, y=150)
        
        self.main_text= Listbox(self.root, height=9, bd=5, font="ariel, 18 bold", width=60)
        self.main_text.place(x=30, y=280)
        
        self.label2=Label(self.root, text="Task List", font='arial, 18 bold', width=10, bd=5, fg="black")
        self.label2.place(x="15", y='230')
        
        def add():
            content= self.text.get(1.0, END)
            self.main_text.insert(END, content)
            with open('data.txt', 'a') as file:
                file.write(content)
                file.seek(0)
                file.close()
            self.text.delete(1.0, END)
            
        
        def delete():
            delete_ = self.main_text.curselection()
            look = self.main_text.get(delete_)
            with open('data.txt','r+') as fl:
                new_fl = fl.readlines()
                fl.seek(0)
                for line in new_fl:
                    item= str(look)
                    if item not in line:
                        fl.write(line)
            self.main_text.delete(delete_)
            
        with open('data.txt', 'r') as file:
            read = file.readlines()
            for i in read:
                ready =i.split()
                self.main_text.insert(END, ready)
            file.close()
            
        self.button = Button(self.root, text="Add", font='sarif, 15 bold ', bd=5, bg='green', fg='White', command=add)
        self.button.place(x=600, y=150)
        
        self.button2 = Button(self.root, text="Delete", font='sarif, 15 bold ', bd=5, bg='green', fg='White', command=delete)
        self.button2.place(x=700, y=150)
        

def main():
    root= Tk()
    ui=todo(root)
    root.mainloop()

if __name__ == "__main__":
    main()