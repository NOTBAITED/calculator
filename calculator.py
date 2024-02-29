import tkinter as tk

# create window
wind = tk.Tk()

# set window config
wind.title("calculator")
wind.config(bg="black")
wind.geometry("400x500")
wind.resizable(False, False)

#title
title = tk.Label(wind, text="calculator", font=("arial", 20), bg="#B30E0E", fg="white")
title.place(x=0, y=0, width=400, height=50)

#box
box = tk.Entry(wind, bd=1, font=("arial", 20))
box.place(x=50, y=60, width=300, height=30)

#function numbers insert
def button_click(button_number):
    current_number = box.get()
    box.delete(0, tk.END)
    box.insert(0, str(current_number) + str(button_number))

#clear function
def button_clear():
    box.delete(0, tk.END)

#function for addition
def button_add():
    first_number_str = box.get()
    global first_number
    global operation
    first_number = float(first_number_str)
    operation = "+"
    box.delete(0, tk.END)
    
    #function for substraction
def button_substract():
    first_number_str = box.get()
    global first_number
    global operation
    first_number = float(first_number_str)
    operation = "-"
    box.delete(0, tk.END)

#function for multiplication
def button_mulitply():
    first_number_str = box.get()
    global first_number
    global operation
    first_number = float(first_number_str)
    operation = "x"
    box.delete(0, tk.END)

#function for devide
def button_devide():
    first_number_str = box.get()
    global first_number
    global operation
    first_number = float(first_number_str)
    operation = "/"
    box.delete(0, tk.END)


#equal function
def button_equal():
    second_number = float(box.get())
    box.delete(0, tk.END)

    if operation == "+":
        box.insert(0, first_number + (second_number))

    elif operation == "-":
        box.insert(0, first_number - (second_number))

    elif operation == "x":
        box.insert(0, first_number * (second_number))

    elif operation == "/":
        box.insert(0, first_number / (second_number))


#define buttons
button_1 = tk.Button(wind, text="1",font=("arial", 20),bd=1,bg="#B30E0E",fg="white", command=lambda: button_click(1))
button_2 = tk.Button(wind, text="2",font=("arial", 20),bd=1,bg="#B30E0E",fg="white", command=lambda: button_click(2))
button_3 = tk.Button(wind, text="3",font=("arial", 20),bd=1,bg="#B30E0E",fg="white", command=lambda: button_click(3))
button_4 = tk.Button(wind, text="4",font=("arial", 20),bd=1,bg="#B30E0E",fg="white", command=lambda: button_click(4))
button_5 = tk.Button(wind, text="5",font=("arial", 20),bd=1,bg="#B30E0E",fg="white", command=lambda: button_click(5))
button_6 = tk.Button(wind, text="6",font=("arial", 20),bd=1,bg="#B30E0E",fg="white", command=lambda: button_click(6))
button_7 = tk.Button(wind, text="7",font=("arial", 20),bd=1,bg="#B30E0E",fg="white", command=lambda: button_click(7))
button_8 = tk.Button(wind, text="8",font=("arial", 20),bd=1,bg="#B30E0E",fg="white", command=lambda: button_click(8))
button_9 = tk.Button(wind, text="9",font=("arial", 20),bd=1,bg="#B30E0E",fg="white", command=lambda: button_click(9))
button_0 = tk.Button(wind, text="0",font=("arial", 20),bd=1,bg="#B30E0E",fg="white", command=lambda: button_click(0))

button_add = tk.Button(wind, text="+",bd=1, bg="white", font=("arial",20), fg="black", command=button_add)
button_substract = tk.Button(wind, text="-",bd=1, bg="white", font=("arial",20), fg="black", command=button_substract)
button_multiply = tk.Button(wind, text="x",bd=1, bg="white", font=("arial",20), fg="black", command=button_mulitply)
button_divide = tk.Button(wind, text="/",bd=1,bg="white", font=("arial",20), fg="black", command=button_devide)

button_equal = tk.Button(wind, text="=", bg="black", font=("arial", 20), fg="white", command=button_equal)
button_clear = tk.Button(wind, text="C", bg="black", font=("arial", 20), fg="white", command=button_clear)

#show buttons
button_1.place(x=0,y=100, width=100, height=100)
button_2.place(x=100,y=100, width=100, height=100)
button_3.place(x=200,y=100, width=100, height=100)

button_4.place(x=0,y=200, width=100, height=100)
button_5.place(x=100,y=200, width=100, height=100)
button_6.place(x=200,y=200, width=100, height=100)

button_7.place(x=0,y=300, width=100, height=100)
button_8.place(x=100,y=300, width=100, height=100)
button_9.place(x=200,y=300, width=100, height=100)

button_0.place(x=100,y=400, width=100, height=100)

button_clear.place(x=0,y=400, width=100, height=100)
button_equal.place(x=200,y=400, width=100, height=100)

button_add.place(x=300,y=100, width=100, height=100)
button_substract.place(x=300,y=200, width=100, height=100)
button_multiply.place(x=300,y=300, width=100, height=100)
button_divide.place(x=300,y=400, width=100, height=100)


wind.mainloop()