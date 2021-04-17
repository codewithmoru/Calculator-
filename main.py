
my_secret = os.environ['Moreshwar']
from tkinter import*
from tkinter import messagebox

root = Tk()

def info():
	messagebox.showinfo("Criator"," Criator: Moreshwar Mahale")
	
root.geometry('1000x1500')	
root.title("calculetor")
root["bg"]="orange"
operator = ""
text_input = StringVar()

f1= Frame(root, width="1000", height="1500", bg="#ffff00").place(x="50", y="50")

b0 = Button(f1, text='Criator', bg='red', fg='blue', width="5",command=info).place(x="800", y="50")


textDisplay = Entry(f1, textvariable = text_input,  bg = 'powder blue', justify = 'right' ,bd='4px', width="32").place(x="100", y="150")

def bttnClear():
    global operator
    operator = ""
    text_input.set("")

b1 = Button(f1, text='C', bg='red', fg='blue', bd='2px', activebackground = "#00ffff", font="Times 10 bold", command=bttnClear).place(x="100", y="350")

def bttnClear():
    global operator
    operator = ""
    text_input.set("")

b2 = Button(f1, text='(', bg='red', fg='blue', bd='2px', font="Times 10 bold", command=lambda:bttnClick('(') ).place(x="350",y="350")

b3 = Button(f1, text=')', bg='red', fg='blue', bd='2px', font="Times 10 bold", command=lambda:bttnClick(')')).place(x="580", y="350")

b4 = Button(f1, text='/', bg='red', fg='blue', bd='2px', font="Times 10 bold", command=lambda:bttnClick('/')).place(x="850", y="350")

l1 = Label(f1, text="---------------------------------------------------------------------", bg="yellow").place(x="100", y="500")

def bttnClick(numbers):
	global operator
	operator = operator+str(numbers)
	text_input.set(operator)	                                    
button_1 = Button(f1, text = '1',bg='red', fg='blue', bd='2px', font="Times 10 bold", command=lambda:bttnClick(1)).place(x="100", y="600")

b6 = Button(f1, text='2', bg='red', fg='blue', bd='2px', font="Times 10 bold", command=lambda:bttnClick(2)).place(x="350", y="600")

b7 = Button(f1, text='3', bg='red', fg='blue', bd='2px', font="Times 10 bold", command=lambda:bttnClick(3)).place(x="580", y="600")

b8 = Button(f1, text='*', bg='red', fg='blue', bd='2px', font="Times 10 bold", command=lambda:bttnClick('*')).place(x="850", y="600")

l2 = Label(f1, text="---------------------------------------------------------------------", bg="yellow").place(x="100", y="750")

b9 = Button(f1, text='4', bg='red', fg='blue', bd='2px', font="Times 10 bold", command=lambda:bttnClick(4)).place(x="100", y="850")

b10 = Button(f1, text='5', bg='red', fg='blue', bd='2px', font="Times 10 bold", command=lambda:bttnClick(5)).place(x="350", y="850")

b11 = Button(f1, text='6', bg='red', fg='blue', bd='2px', font="Times 10 bold", command=lambda:bttnClick(6)).place(x="580", y="850")

b12 = Button(f1, text='+', bg='red', fg='blue', bd='2px', font="Times 10 bold", command=lambda:bttnClick('+')).place(x="850", y="850")

l3 = Label(f1, text="---------------------------------------------------------------------", bg="yellow").place(x="100", y="1000")

b13 = Button(f1, text='7', bg='red', fg='blue', bd='2px', font="Times 10 bold", command=lambda:bttnClick(7)).place(x="100", y="1100")

b14 = Button(f1, text='8', bg='red', fg='blue', bd='2px', font="Times 10 bold", command=lambda:bttnClick(9)).place(x="350", y="1100")

b15 = Button(f1, text='9', bg='red', fg='blue', bd='2px', font="Times 10 bold", command=lambda:bttnClick(9)).place(x="580", y="1100")

b16 = Button(f1, text='-', bg='red', fg='blue', bd='2px', font="Times 10 bold", command=lambda:bttnClick('-')).place(x="850", y="1100")

l4 = Label(f1, text="---------------------------------------------------------------------", bg="yellow").place(x="100", y="1250")

b17 = Button(f1, text='0', bg='red', fg='blue', bd='2px', font="Times 10 bold", command=lambda:bttnClick(0)).place(x="100", y="1350")

b18 = Button(f1, text='.', bg='red', fg='blue', bd='2px', font="Times 10 bold", command=lambda:bttnClick('.')).place(x="350", y="1350")

def bttnEquals():
    global operator
    sumup = str(eval(operator))
    text_input.set(sumup)
    operator = ""

b19 = Button(f1, text='=', bg='red', fg='blue', bd='2px', width="10", font="Times 10 bold", command=bttnEquals).place(x="580", y="1350")

l5 = Label(root, text="its made by :Eng.Morshwar Mahale").pack()

root.mainloop()