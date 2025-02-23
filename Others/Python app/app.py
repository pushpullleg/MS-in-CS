import tkinter as tk

# Function to update label text
def change_text():
    label.config(text="Button Clicked!")

# Create the main window
root = tk.Tk()
root.title("Simple Tkinter App")
root.geometry("300x200")  # Set window size

# Create a label
label = tk.Label(root, text="Hello, Tkinter!", font=("Arial", 14))
label.pack(pady=20)  # Add some space

# Create a button
button = tk.Button(root, text="Click Me", command=change_text, font=("Arial", 12))
button.pack()

# Run the Tkinter event loop
root.mainloop()
