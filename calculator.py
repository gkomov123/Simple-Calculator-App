import tkinter


button_values = [
    ["AC", "+/-", "%", "÷"],
    ["7", "8", "9", "×"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "√", "="]
]

right_symbols = ["÷", "×", "-", "+", "="]
top_symbols = ["AC", "+/-", "%"]

row_count = len(button_values) #5
col_count = len(button_values[0]) #4

color_light_gray = "#D4D4D2"
color_black = "#1C1C1C"
color_dark_gray = "#505050"
color_orange = "#FF9500"
color_white = "white"

# Window Setup
window = tkinter.Tk() # Create window
window.title("Calculator")
window.resizable(False, False)

frame = tkinter.Frame(window)
label = tkinter.Label(frame, text="0", font=("Arial", 45), background=color_black, foreground=color_white,
                      anchor='e', width=col_count)

label.grid(row=0, column=0, columnspan=col_count, sticky="we")

# Button generator
for row in range(row_count):
    for col in range(col_count):
        value = button_values[row][col]
        button = tkinter.Button(frame, text=value, font=("Arial", 30), width=col_count-1, height=1,
                                command=lambda value=value: button_clicked(value))
        if value in top_symbols:
            button.config(foreground=color_black, background=color_light_gray)
        elif value in right_symbols:
            button.config(foreground=color_white, background=color_orange)
        else:
            button.config(foreground=color_white, background=color_dark_gray)
        button.grid(row=row+1, column=col)

frame.pack()

#A+B, A-B, A*B, A/B
A = "0"
operator = None
B = None


def clear_all():
    global A, B, operator

    A = "0"
    operator = None
    B = None


def remove_zero_decimal(num):
    if num % 1 == 0:
        num = int(num)
    return str(num)


def button_clicked(some_value):
    global right_symbols, top_symbols, label, A, B, operator

    if some_value in right_symbols:
        if some_value == "=":
            if A is not None and operator is not None:
                B = label["text"]
                numA = float(A)
                numB = float(B)

                if operator == "+":
                    label["text"] = remove_zero_decimal(numA + numB)
                elif operator == "-":
                    label["text"] = remove_zero_decimal(numA - numB)
                elif operator == "×":
                    label["text"] = remove_zero_decimal(numA * numB)
                elif operator == "÷":
                    label["text"] = remove_zero_decimal(numA / numB)

                clear_all()

        elif some_value in "+-×÷":
            if operator is None:
                A = label["text"]
                label["text"] = "0"
                B = "0"

            operator = some_value

    elif some_value in top_symbols:
        if some_value == 'AC':
            clear_all()
            label["text"] = "0"
        elif some_value == "+/-":
            result = float(label["text"]) * -1
            label["text"] = remove_zero_decimal(result)
        elif some_value == "%":
            result = float(label["text"]) / 100
            label["text"] = remove_zero_decimal(result)
    else:#digits or .

        # TODO square root button

        if some_value == ".":
            if some_value not in label["text"]:
                label["text"] += some_value
        elif some_value in "0123456789":
            if label["text"] == "0": # replace 0 with number instead of getting 05 when typing
                label["text"] = some_value
            else:
                label["text"] += some_value


# Center window on open
window.update() #update window with the new size dimensions
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()


window_x = int((screen_width/2) - (window_width/2))
window_y = int((screen_height/2) - (window_height/2))

#format "(w)x(h)+(x)+(y)"
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

window.mainloop()



