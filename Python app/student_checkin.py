import tkinter as tk
from tkinter import messagebox
import sqlite3
from datetime import datetime


def setup_database():
    conn = sqlite3.connect('student_checkin.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            cwid TEXT PRIMARY KEY,
            name TEXT
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS courses (
            course_id TEXT PRIMARY KEY,
            course_name TEXT,
            term TEXT
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS checkins (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cwid TEXT,
            course_id TEXT,
            checkin_time TEXT,
            checkout_time TEXT,
            date TEXT,
            FOREIGN KEY (cwid) REFERENCES students (cwid),
            FOREIGN KEY (course_id) REFERENCES courses (course_id)
        )
    ''')
    conn.commit()
    conn.close()

def check_in(cwid):
    conn = sqlite3.connect('student_checkin.db')
    cursor = conn.cursor()
    
    # Check if the student exists
    cursor.execute('SELECT * FROM students WHERE cwid = ?', (cwid,))
    student = cursor.fetchone()
    if not student:
        messagebox.showwarning("Warning", "Student not found.")
        conn.close()
        return
    
    # Display registered courses
    cursor.execute('SELECT course_id, course_name FROM courses')
    courses = cursor.fetchall()
    course_listbox.delete(0, tk.END)
    for course in courses:
        course_listbox.insert(tk.END, f"{course[0]} - {course[1]}")
    
    # Log check-in time
    selected_course = course_listbox.get(tk.ACTIVE).split(' - ')[0]
    checkin_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute('INSERT INTO checkins (cwid, course_id, checkin_time, date) VALUES (?, ?, ?, ?)', 
                   (cwid, selected_course, checkin_time, datetime.now().strftime('%Y-%m-%d')))
    conn.commit()
    conn.close()
    messagebox.showinfo("Info", "Check-in successful.")

def check_out(cwid):
    conn = sqlite3.connect('student_checkin.db')
    cursor = conn.cursor()
    
    # Log check-out time
    checkout_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute('UPDATE checkins SET checkout_time = ? WHERE cwid = ? AND checkout_time IS NULL', 
                   (checkout_time, cwid))
    conn.commit()
    conn.close()
    messagebox.showinfo("Info", "Check-out successful.")

def generate_report():
    conn = sqlite3.connect('student_checkin.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT c.date, s.name, c.cwid, co.course_name, c.checkin_time, c.checkout_time,
               (strftime('%s', c.checkout_time) - strftime('%s', c.checkin_time)) / 60.0 AS duration
        FROM checkins c
        JOIN students s ON c.cwid = s.cwid
        JOIN courses co ON c.course_id = co.course_id
        WHERE c.date = ?
    ''', (datetime.now().strftime('%Y-%m-%d'),))
    
    rows = cursor.fetchall()
    conn.close()
    
    df = pd.DataFrame(rows, columns=['Date', 'Student Name', 'CWID', 'Course', 'Check-In Time', 'Check-Out Time', 'Duration (minutes)'])
    df.to_excel('daily_report.xlsx', index=False)
    messagebox.showinfo("Info", "Report generated successfully.")

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

if __name__ == "__main__":
    setup_database()
    root.mainloop()