import tkinter as tk
from tkinter import messagebox

def compute_square_root():
    try:
        number = float(entry_number.get())
        result = number ** 0.5
        label_result.config(text=f"Square Root: {result:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Invalid Input. Please enter a valid number.")

# Create the main window
root = tk.Tk()
root.title("Square Root Calculator")

# Entry field for input number
entry_number = tk.Entry(root)
entry_number.pack(pady=10)

# Button to compute square root
btn_compute = tk.Button(root, text="Compute Square Root", command=compute_square_root)
btn_compute.pack()

# Label to display the result
label_result = tk.Label(root, text="Square Root: ")
label_result.pack(pady=10)

# Start the main event loop
root.mainloop()
