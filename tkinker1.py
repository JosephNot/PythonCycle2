import tkinter as tk

def convert():
    try:
        celsius = float(temp_entry.get())
    except:
        result_label.config(text="Please enter a numerical value")
        
    fahrenheit = celsius * 1.8 + 32
    fahrenheit = "Fahrenheit: " + str(fahrenheit)
    result_label.config(text=fahrenheit)


def clear(): 
    temp_entry.delete(0, tk.END)
    result_label.config(text="") 

# Variables
window = tk.Tk()
temp_entry = tk.Entry(window)
result_label = tk.Label(window, text="")

window.title("Temperature Converter") 
window.geometry("320x180") 

tk.Label(window, text="Celsius:").grid(row=0, column=0, padx=10, pady=10)

temp_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Button(window, text="Convert", command=convert).grid(row=1, column=0, padx=10, pady=10)
result_label.grid(row=2, column=1, padx=10, pady=10)

tk.Button(window, text="Clear", command=clear).grid(row=1, column=1, padx=10, pady=10)

window.mainloop()