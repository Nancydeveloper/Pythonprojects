from tkinter import *
a = Tk()
def click(num):
    value = e.get()
    e.delete(0,END)
    e.insert(0,str(value) + str(num))
def clear():
     e.delete(0,END)  
def add():
    num = e.get()
    e.delete(0,END)
    global math
    math = "add"
    global a
    a = int(num)
def minus():
    num1 = e.get()
    e.delete(0,END)
    global math
    math = "minus"
    global b
    b = int(num1)
    
def multiply():
    num2 = e.get()
    e.delete(0,END)
    global math
    math = "mul"
    global c
    c = int(num2)
def divide():
    num3 = e.get()
    e.delete(0,END)
    global math
    math = "divide"
    global d
    d = int(num3)    
        
def equal():
    second = e.get()
    e.delete(0,END)
    if math == "add":
        e.insert(0,a + int(second))
    elif math == "minus":
        e.insert(0,b - int(second))
    elif math == "mul":
        e.insert(0,c * int(second))  
    elif math == "divide":
        e.insert(0,d / int(second))             
            
    
e = Entry(a,width=35)
btn1 = Button(a,text=1,padx=25,pady=15,command=lambda:click(1))
btn2 = Button(a,text=2,padx=25,pady=15,command=lambda:click(2))
btn3 = Button(a,text=3,padx=25,pady=15,command=lambda:click(3))

btn4 = Button(a,text=4,padx=25,pady=15,command=lambda:click(4))
btn5 = Button(a,text=5,padx=25,pady=15,command=lambda:click(5))
btn6 = Button(a,text=6,padx=25,pady=15,command=lambda:click(6))

btn7 = Button(a,text=7,padx=25,pady=15,command=lambda:click(7))
btn8 = Button(a,text=8,padx=25,pady=15,command=lambda:click(8))
btn9 = Button(a,text=9,padx=25,pady=15,command=lambda:click(9))

btn0 = Button(a,text=0,padx=25,pady=15,command=lambda:click(0))
btnc = Button(a,text="=",padx=54,pady=15,command=equal)

btna = Button(a,text="+",padx=25,pady=15,command=add)
btns = Button(a,text="-",padx=25,pady=15,command=minus)
btnm = Button(a,text="*",padx=25,pady=15,command=multiply)

btne =Button(a,text="clear",padx=54,pady=15,command=clear)
btnd =Button(a,text="/",padx=25,pady=15,command=divide)

e.grid(row=1,column=1,columnspan=3)
btn1.grid(row=2,column=1)
btn2.grid(row=2,column=2)
btn3.grid(row=2,column=3)

btn4.grid(row=3,column=1)
btn5.grid(row=3,column=2)
btn6.grid(row=3,column=3)

btn7.grid(row=4,column=1)
btn8.grid(row=4,column=2)
btn9.grid(row=4,column=3)

btn0.grid(row=5,column=1)
btnc.grid(row=5,column=2,columnspan=2)

btna.grid(row=6,column=1)
btns.grid(row=6,column=2)
btnm.grid(row=6,column=3)

btne.grid(row=7,column=1,columnspan=2)
btnd.grid(row=7,column=3)


mainloop()



