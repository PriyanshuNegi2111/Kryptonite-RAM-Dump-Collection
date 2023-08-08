import datetime
import tkinter as tk
from tkinter import filedialog, ttk
from tkinter import messagebox
import subprocess
import getpass

app = tk.Tk()
app.geometry("900x400")
app.title(string="Ram Dump Collection Tool")

frame = tk.Frame(app)
frame.pack(fill="both", expand=True)

options = ["Windows", "Linux"]
selected_option = tk.StringVar()
option_combobox = ttk.Combobox(frame, textvariable=selected_option, 
                               values=options, state="readonly")
option_combobox.grid(row=1, column=0, padx=10, pady=10)

file_path_var = tk.StringVar()

current_time = datetime.datetime.now().time()
Time = current_time.strftime("%H:%M")

def dumpIT():
    module_name = "lime"
    check_module_command = ["lsmod"]
    completed_process = subprocess.run(check_module_command, capture_output=True, text=True)

    if module_name in completed_process.stdout:
        # Unload the module
        unload_command = ["sudo", "rmmod", module_name]
        subprocess.run(unload_command)

# Load the module
    load_command = ["sudo", "insmod", "./lime-5.16.0-12parrot1-amd64.ko", f"path=/{Time}.mem", "format=raw"]
    subprocess.run(load_command)

dump_button = tk.Button(frame, text="Dump", command=dumpIT)
dump_button.grid(row=3, column=0, padx=10, pady=10)

analyze_button = tk.Button(frame, text="Analyze")
analyze_button.grid(row=4, column=0, padx=10, pady=10)

app.mainloop()
