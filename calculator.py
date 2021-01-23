from Tkinter import *
import config

# Functions


def turnOn():
    if not config.isOn:
        config.isOn = True
    output.delete(0, END)
    output.insert(0, "0")


def turnOff():
    if config.isOn:
        config.isOn = False
    output.delete(0, END)

def onClick(digit):
    if config.isOn:
        current = output.get()
        output.delete(0, END)
        if current == "0":
            if digit == "00":
                output.insert(0, "0")
            else:
                output.insert(0, digit)
        elif current != "00":
            #output.insert(0, str(current) + str(digit))
            if digit == ".":
                if "." not in str(current):
                    output.insert(0, str(current) + str(digit))
                else:
                    output.insert(0, current)
            else:
                output.insert(0, str(current) + str(digit))
        else:
            output.insert(0, "0")
    else:
        print("Not on")

def operator(operation):
    if config.isOn:
        config.fNum = float(output.get())
        config.operation = operation
        output.delete(0, END)
        output.insert(0, "0")

def equals():
    if config.isOn and output.get() != "" and output.get() != "0":
        sNum = float(output.get())
        output.delete(0, END)
        if config.operation == "+":
            if float.is_integer(config.fNum + sNum):
                output.insert(0, int(config.fNum + sNum))
            else:
                output.insert(0, config.fNum + sNum)
        elif config.operation == "-":
            if float.is_integer(config.fNum - sNum):
                output.insert(0, int(config.fNum - sNum))
            else:
                output.insert(0, config.fNum - sNum)
        elif config.operation == "*":
            if float.is_integer(config.fNum * sNum):
                output.insert(0, int(config.fNum * sNum))
            else:
                output.insert(0, config.fNum * sNum)
        elif config.operation == "/":
            if float.is_integer(config.fNum / sNum):
                output.insert(0, int(config.fNum / sNum))
            else:
                output.insert(0, config.fNum / sNum)
        elif config.operation == "%":
            if float.is_integer(config.fNum % sNum):
                output.insert(0, int(config.fNum % sNum))
            else:
                output.insert(0, config.fNum % sNum)
    else:
        output.delete(0, END)
        output.insert(0, "0")

# Window

root = Tk()

# calculator output:

output = Entry(root, borderwidth = 10)
output.grid(row = 0, column = 0, columnspan = 5)


#My calculator buttons:

button1 = Button(root, text = "1", padx = 20, pady = 20, command = lambda: onClick(1))
button2 = Button(root, text = "2", padx = 20, pady = 20, command = lambda: onClick(2))
button3 = Button(root, text = "3", padx = 20, pady = 20, command = lambda: onClick(3))
button4 = Button(root, text = "4", padx = 20, pady = 20, command = lambda: onClick(4))
button5 = Button(root, text = "5", padx = 20, pady = 20, command = lambda: onClick(5))
button6 = Button(root, text = "6", padx = 20, pady = 20, command = lambda: onClick(6))
button7 = Button(root, text = "7", padx = 20, pady = 20, command = lambda: onClick(7))
button8 = Button(root, text = "8", padx = 20, pady = 20, command = lambda: onClick(8))
button9 = Button(root, text = "9", padx = 20, pady = 20, command = lambda: onClick(9))
button0 = Button(root, text = "0", padx = 20, pady = 20, command = lambda: onClick(0))
button00 = Button(root, text = "00", padx = 17, pady = 20, command = lambda: onClick("00"))
buttonDecimal = Button(root, text = ".", padx = 20, pady = 20, command = lambda: onClick("."))

buttonAddition = Button(root, text = "+", padx = 20, pady = 20, command = lambda: operator("+"))
buttonMultiplication = Button(root, text = "x", padx = 20, pady = 20, command = lambda: operator("*"))
buttonSubtraction = Button(root, text = "-", padx = 20, pady = 20, command = lambda: operator("-"))
buttonDivision = Button(root, text = "/", padx = 20, pady = 20, command = lambda: operator("/"))

buttonModulus = Button(root, text = "%", padx = 34, pady = 20, command = lambda: operator("%"))
buttonOn = Button(root, text = "On/Reset", padx = 17, pady = 20, command = lambda: turnOn())
buttonOff = Button(root, text = "Off", padx = 33, pady = 20, command = lambda: turnOff())
buttonEquals = Button(root, text = "=", padx = 35, pady = 20, command = lambda: equals())

# Calculator button layout:

button1.grid(row = 1, column = 0)
button2.grid(row = 1, column = 1)
button3.grid(row = 1, column = 2)

button4.grid(row = 2, column = 0)
button5.grid(row = 2, column = 1)
button6.grid(row = 2, column = 2)

button7.grid(row = 3, column = 0)
button8.grid(row = 3, column = 1)
button9.grid(row = 3, column = 2)


button0.grid(row = 4, column = 0)
button00.grid(row = 4, column = 1)
buttonDecimal.grid(row = 4, column = 2)

buttonAddition.grid(row = 4, column = 3)
buttonMultiplication.grid(row = 3, column = 3)
buttonSubtraction.grid(row = 2, column = 3)
buttonDivision.grid(row = 1, column = 3)

buttonModulus.grid(row = 3, column = 4)
buttonOn.grid(row = 1, column = 4)
buttonOff.grid(row = 2, column = 4)
buttonEquals.grid(row = 4, column = 4)


output.insert(0, "0")
root.title("Simpl Calculator")
root.mainloop()