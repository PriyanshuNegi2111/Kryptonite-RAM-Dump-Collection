import shutil

from pathlib import Path

import hashlib

import datetime

import tkinter as tk

from tkinter import filedialog, ttk

from tkinter import messagebox

import subprocess

import getpass

import sys

import os



app = tk.Tk()

app.geometry("900x400")

app.title(string="Ram Dump Collection Tool")



frame = tk.Frame(app)

frame.pack(fill="both", expand=True)





file_path_var = tk.StringVar()





current_time = datetime.datetime.now().time()

Time = current_time.strftime("%H_%M")





def md5_hash_string(input_string):

    md5_hash = hashlib.md5()

    md5_hash.update(input_string.encode('utf-8'))

    return md5_hash.hexdigest()



MD5 = md5_hash_string(Time)



def get_os_name():

    if os.name == "posix":

        return "Linux"

    elif os.name == "nt":

        return "Windows"



def dumpIT():

    selected_platform = get_os_name()

    if selected_platform == "Windows":



        folder_path = Path(f"{MD5}")

        folder_path.mkdir(parents=True, exist_ok=True)

        cmd_command = f"winpmem.exe {MD5}.raw"

        startup_info = subprocess.STARTUPINFO()

        startup_info.dwFlags |= subprocess.STARTF_USESHOWWINDOW

        startup_info.wShowWindow = subprocess.SW_HIDE



        completed_process = subprocess.run(

            cmd_command, shell=True, text=True,

            stdout=subprocess.PIPE, stderr=subprocess.PIPE,

            startupinfo=startup_info

        )

        if completed_process.returncode == 1:

            app.destroy()



        source_file_path = f"{MD5}.raw"

        destination_folder = f"{MD5}"

        shutil.move(source_file_path, destination_folder)





    else:

        current_directory = os.getcwd()

        folder_path = f"{current_directory}/{MD5}"

        os.makedirs(folder_path, exist_ok=True)

        module_name = "lime"

        check_module_command = ["lsmod"]

        completed_process = subprocess.run(

            check_module_command, capture_output=True, text=True

        )



        if module_name in completed_process.stdout:

            # Unload the module

            unload_command = ["sudo", "rmmod", module_name]

            subprocess.run(unload_command)



        # Load the module

        load_command = ["sudo", "insmod", "./lime-5.16.0-12parrot1-amd64.ko", f"path={current_directory}/{MD5}/{MD5}.mem", "format=raw"]

        subprocess.run(load_command)

        

        # Process completed_process for Linux

        if completed_process.returncode == 0:

            print("Done")

            app.destroy()



dump_button = tk.Button(frame, text="Dump", command=dumpIT)

dump_button.grid(row=3, column=0, padx=10, pady=10)



analyze_button = tk.Button(frame, text="Analyze")

analyze_button.grid(row=4, column=0, padx=10, pady=10)



app.mainloop()

  
