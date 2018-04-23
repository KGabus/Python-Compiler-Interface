#!/usr/bin/python3
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import os
import subprocess

root = Tk()
root.title("Compiler Interface")


output_str = StringVar()
output_str.set("Gabus.out")
std_sel_option = StringVar()
std_sel_option.set(1)
debug_selected = IntVar()

compile_array = ["g++"]


def exit_program():
    exit()


def file_selection():
    sel_file = filedialog.askopenfilename()
    if sel_file:
        sel_file = root.tk.splitlist(sel_file)
        compile_array.append(sel_file[0])         #the first thing in the list will be the filename
        sel_file = sel_file[0]
        sel_file = os.path.basename(sel_file)       #remove file path for display purposes
        debug_test(sel_file)
        selected_files_box.insert(END, sel_file)    #add file to listbox
        debug_test(compile_array)


def debug_test(thing):
    print(thing)

def compile_event():
    print(output_entrybox.get())
    print(std_sel_option.get())
    print(debug_selected.get())

    if len(compile_array) == 1:
        messagebox.showerror("Required Information Missing", "You must select at least one file.")
        return

    compile_array.append("-o")
    compile_array.append(output_str.get())
    compile_array.append(std_sel_option.get())

    if debug_selected.get():
        compile_array.append("-g")
    debug_test(compile_array)

    compile_result = subprocess.Popen(compile_array, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (out, error) = compile_result.communicate()

    if error:
        messagebox.showerror("Compile Error", error)
    if out:
        messagebox.showinfo("Result", out)

#remove things from the compile array in case they hit compile again
    if "-g" in compile_array:
        compile_array.remove("-g")

    if std_sel_option.get() in compile_array:
        compile_array.remove(std_sel_option.get())

    if "-o" in compile_array:
        compile_array.remove("-o")

    compile_array.remove(output_str.get())
    debug_test(compile_array)

    debug_selected.set(0)
    std_sel_option.set("-std=c++98")


title_label = Label(text="Compiler Interface")
title_label.grid(row=1, columnspan=5)

file_select_button = Button(text="Select Files", width=27, command=file_selection)
file_select_button.grid(row=2, column=1, columnspan=2, sticky="s")

selected_files_box = Listbox(selectmode=MULTIPLE, height=17, width=30)
selected_files_box.grid(row=3, column=1, rowspan=4, columnspan=2, padx=5, pady=0, sticky="s")

options_labelframe = LabelFrame(text="Compile Options")
options_labelframe.grid(row=3, column=3, columnspan=2)

debug_checkbox = Checkbutton(options_labelframe, text="-g (Debug)", variable=debug_selected)
debug_checkbox.pack(side=TOP)

std_labelframe = LabelFrame(options_labelframe, text="-std Options")
std_labelframe.pack(side=TOP)

std_98_rbutt = Radiobutton(std_labelframe, text="c++98", variable=std_sel_option, value="-std=c++98")
std_98_rbutt.pack(side=TOP)
std_98_rbutt.select()

std_11_rbutt = Radiobutton(std_labelframe, text="c++11", variable=std_sel_option, value="-std=c++11")
std_11_rbutt.pack(side=TOP)

std_14_rbutt = Radiobutton(std_labelframe, text="c++14", variable=std_sel_option, value="-std=c++14")
std_14_rbutt.pack(side=TOP)

std_17_rbutt = Radiobutton(std_labelframe, text="c++17", variable=std_sel_option, value="-std=c++17")
std_17_rbutt.pack(side=TOP)

entry_label = Label(text="Output File Name:")
entry_label.grid(row=7, column=1, sticky="w", padx=5)

output_entrybox = Entry(width=30, textvariable=output_str)
output_entrybox.grid(row=8, column=1, columnspan=3, sticky="w", padx=5)

compile_button = Button(text="Compile", command=compile_event)
compile_button.grid(row=8, column=3, sticky="e")

exit_button = Button(text="Exit", command=exit_program)
exit_button.grid(row=8, column=4, padx=5)


root.mainloop()

