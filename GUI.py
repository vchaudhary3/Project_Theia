#!/usr/bin/env python

from tkinter import*


window = Tk()
global check
check = "jil"
global password
password =  1234
        
window.title("Authorization")

Label(window, text = "User Name: ").grid(row=1)
Label(window, text = "Password: ").grid(row=2)

e1 = Entry(window)
e2 = Entry(window)




e1.grid(row=1, column=4)
e2.grid(row=2, column=4)

def retrieve_input():
        inputValue = lbl.textBox.get("1.0","end-1c")
        print(inputValue)

def checkVarification():
      s= e1.get()
      s2 = e2.get()
      if(s1 == check):
              if s2 == password:
                      window.Label(text = "Horray!").pack()



lbl = Label(window, text = "Enter Password", font = ("Arial Bold", 30))
window.geometry('500x450')
lbl.grid(column = 50, row = 50)
window.mainloop()
        
