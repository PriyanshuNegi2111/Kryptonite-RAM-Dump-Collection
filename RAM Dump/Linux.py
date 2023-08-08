import datetime
import tkinter as tk
from tkinter import filedialog, ttk
from tkinter import messagebox
# from PIL import Image
# from PIL import ImageTk
import subprocess
app = tk.Tk()
app.geometry("900x400")
app.title(string="Ram Dump Collection Tool")
frame = tk.Frame(app)
frame.pack(fill="both", expand=True)
# img = Image.open("/home/ryx/Desktop/Kavach/KryptoniteUpdatedLogo.jpg")
# img = img.resize((400, 150))
# logo_image = ImageTk.PhotoImage(img)
# logo_canvas = tk.Canvas(frame, width=400, height=200)
# logo_canvas.grid(row=0, column=0, padx=10, pady=10)
# logo_canvas.create_image(190, 78, image=logo_image)
options = ["Windows","Linux"]
selected_option = tk.StringVar()
option_combobox = ttk.Combobox(frame, textvariable=selected_option, values=options, state="readonly")
option_combobox.grid(row=1, column=0, padx=10, pady=10)
file_path_var = tk.StringVar()
current_time = datetime.datetime.now().time()
Time = current_time.strftime("%H:%M")
def dumpIT():
    command = f'sudo insmod ./lime-6.3.0-kali1-amd64.ko \"path=/{Time}.mem"'
    sudo_password = "kali123"
    completed_process = subprocess.run(
        command,
        shell=True,
        input=sudo_password.encode('utf-8'),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    if completed_process.returncode == 0:
        messagebox.showinfo("Successfull")
    else:
        messagebox.showerror("Error galat code")
dump_button = tk.Button(frame, text="Dump", command=dumpIT)
dump_button.grid(row=3, column=0, padx=10, pady=10)
analyze_button = tk.Button(frame, text="Analyze")
analyze_button.grid(row=4, column=0, padx=10, pady=10)
app.mainloop()
