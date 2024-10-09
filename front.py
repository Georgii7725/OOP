from tkinter import *
from tkinter import ttk
from Franc import Frac

def calculate():
    A = int(numer1.get()) if typeN1.get() == "int" else Frac(int(numer1.get()), int(denom1.get()))
    B = int(numer2.get()) if typeN2.get() == "int" else Frac(int(numer2.get()), int(denom2.get()))
    match operation.get():
        case "+":
            answer_string.set(str(A+B))
        case "-":
            answer_string.set(str(A-B))
        case "*":
            answer_string.set(str(A*B))
        case "/":
            answer_string.set(str(A/B))
        case "**":
            answer_string.set(str(A**B))        

def change1():
    numer1.grid_remove()
    line1.grid_remove()
    denom1.grid_remove()
    match typeN1.get():
        case "int":
            numer1.grid(row=3, column=0)
        case "frac":
            numer1.grid(row=2, column=0)
            line1.grid(row=3, column=0)
            denom1.grid(row=4, column=0)

def change2():
    numer2.grid_remove()
    line2.grid_remove()
    denom2.grid_remove()
    match typeN2.get():
        case "int":
            numer2.grid(row=3, column=2)
        case "frac":
            if operation.get() != "**":
                numer2.grid(row=2, column=2)
                line2.grid(row=3, column=2)
                denom2.grid(row=4, column=2)
            else: 
                typeN2.set("int")
                numer2.grid(row=3, column=2)



screen = Tk()
screen.geometry("800x150+200+200")

options = ["int", "frac"]
typeN1 = ttk.Combobox(textvariable=StringVar(value=options[0]), values=options, state="readonly")
typeN1.bind("<<ComboboxSelected>>", lambda e: change1())
typeN1.set(options[1])
typeN1.grid(row=0, column=0, padx=20)
typeN2 = ttk.Combobox(textvariable=StringVar(value=options[0]), values=options, state="readonly")
typeN2.set(options[1])
typeN2.grid(row=0, column=2, padx=20)
typeN2.bind("<<ComboboxSelected>>", lambda e: change2())

Label(text = "                                   ").grid(row=1, column=0)

options = ["+", "-", "x", "/", "**"]
operation = ttk.Combobox(textvariable=StringVar(value=options[0]), values=options, state="readonly", width=2)
operation.bind("<<ComboboxSelected>>", lambda e: change2())
operation.set(options[0])
operation.grid(row=3, column=1)

numer1 = Entry(width=10)
line1 = Label(text = "____________")
denom1 = Entry(width=10)
numer2 = Entry(width=10)
line2 = Label(text = "____________")
denom2 = Entry(width=10)
equal = Button(text="=", width=10, command=calculate)
equal.grid(row=3, column=3)
answer_string = StringVar()
answer = Label(textvariable=answer_string, width=50)
answer.grid(row=3, column=4)
change1()
change2()        

screen.mainloop()