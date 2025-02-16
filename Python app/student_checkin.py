import tkinter as tk
from tkinter import messagebox
import sqlite3
from datetime import datetime
import pandas as pd

root = tk.Tk()
root.title("Student Check-In System")
root.geometry("500x400")

# Create an entry widget for CWID
cwid_label = tk.Label(root, text="Enter CWID:", font=("Arial", 12))
cwid_label.pack(pady=5)
cwid_entry = tk.Entry(root, width=40, font=("Arial", 12))
cwid_entry.pack(pady=5)

# Create a listbox to display registered courses
course_listbox = tk.Listbox(root, width=50, height=10, font=("Arial", 12))
course_listbox.pack(pady=10)

# Create a frame for the buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

# Create buttons
checkin_button = tk.Button(button_frame, text="Check In", command=lambda: check_in(cwid_entry.get()), font=("Arial", 12))
checkin_button.grid(row=0, column=0, padx=5)

checkout_button = tk.Button(button_frame, text="Check Out", command=lambda: check_out(cwid_entry.get()), font=("Arial", 12))
checkout_button.grid(row=0, column=1, padx=5)

report_button = tk.Button(button_frame, text="Generate Report", command=generate_report, font=("Arial", 12))
report_button.grid(row=0, column=2, padx=5)