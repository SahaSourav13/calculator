import tkinter as tk

# Function to update the expression in the entry box
def press(key):
    current = entry_var.get()
    current += str(key)
    entry_var.set(current)

# Function to evaluate the expression
def evaluate():
    try:
        result = eval(entry_var.get())  # Evaluate the expression entered by the user
        entry_var.set(result)
    except Exception as e:
        entry_var.set("Error")

# Function to clear the expression in the entry box
def clear():
    entry_var.set("")

# Initialize the main window
window = tk.Tk()
window.title("Calculator")

# Create a StringVar to hold the current input for the entry widget
entry_var = tk.StringVar()

# Entry widget to display the expression
entry = tk.Entry(window, textvariable=entry_var, font=("Arial", 16), bd=10, relief="sunken", width=25, justify="right")
entry.grid(row=0, column=0, columnspan=4)

# Button layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('C', 5, 0)
]

# Create the buttons and place them on the grid
for (text, row, col) in buttons:
    if text == "=":
        button = tk.Button(window, text=text, font=("Arial", 14), width=5, height=2, command=evaluate)
    elif text == "C":
        button = tk.Button(window, text=text, font=("Arial", 14), width=5, height=2, command=clear)
    else:
        button = tk.Button(window, text=text, font=("Arial", 14), width=5, height=2, command=lambda key=text: press(key))
    
    button.grid(row=row, column=col)

# Run the main event loop
window.mainloop()
