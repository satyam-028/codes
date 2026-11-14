# n = [h for h in range(1,101)]
# print(n)




# n = [h for h in range(1,101) if h%2==0]
# print(n)



s = "hello"
d = [g for g in s]
print(d)


import tkinter as tk
from tkinter import ttk

# Create the main application window
root = tk.Tk()
root.title("Radio Button Example")
root.geometry("300x200")

# Define a variable to hold the selected radio button value
selected_option = tk.StringVar(value="Option 1")

# Function to display selected option
def show_selected():
    selected_label.config(text=f"Selected: {selected_option.get()}")

# Create radio buttons
radio1 = ttk.Radiobutton(root, text="Option 1", variable=selected_option, value="Option 1", command=show_selected)
radio2 = ttk.Radiobutton(root, text="Option 2", variable=selected_option, value="Option 2", command=show_selected)
radio3 = ttk.Radiobutton(root, text="Option 3", variable=selected_option, value="Option 3", command=show_selected)

# Place radio buttons on the window
radio1.pack(pady=5)
radio2.pack(pady=5)
radio3.pack(pady=5)

# Label to display the selected option
selected_label = ttk.Label(root, text="Selected: Option 1")
selected_label.pack(pady=20)

# Run the application
root.mainloop()
