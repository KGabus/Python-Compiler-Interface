#!/usr/bin/python3
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import os
import subprocess


"""
class Window(Frame):
    def __init__(self):
        super().__init__()
        self.init_window()



    def init_window(self):
        self.master.title("G++ Compiler")        #set title
        self.pack(fill=BOTH, expand=True)  #set widget to take full space of root window

        self.columnconfigure(1)
        self.columnconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)

        selected_std = StringVar()
        selected_std = "1"

        output_str = StringVar()

        title_label = Label(self, text="Compiler Interface")
        title_label.grid(row=1, columnspan=5)

        file_select_button = Button(self, text="Select Files", command=self.file_selection)
        file_select_button.grid(row=2, column=1)

        file_remove_button = Button(self, text="Remove Selected", command=self.file_remove)
        file_remove_button.grid(row=2, column=2)

        file_select_label = Label(self, text="Selected Files")
        file_select_label.grid(row=3, column=1)

        selected_files_box = Listbox(self)
        selected_files_box.grid(row=4, column=1, rowspan=5, columnspan=2, padx=0)

        options_labelframe = LabelFrame(self, text="Compile Options")
        options_labelframe.grid(row=3, column=3, columnspan=2)

        debug_checkbox = Checkbutton(options_labelframe, text="-g", command=self.g_check)
        debug_checkbox.pack(side=LEFT)

        std_options_labelframe = LabelFrame(options_labelframe, text="-std Options")
        std_options_labelframe.pack(side=LEFT)
#todo: fix the radio buttons at some point
        std_98_rbutton = Radiobutton(std_options_labelframe, text="c++98", variable=selected_std, value="1")
        std_98_rbutton.pack(side=LEFT)

        std_11_rbutton = Radiobutton(std_options_labelframe, text="c++11", variable=selected_std, value="2")
        std_11_rbutton.pack(side=LEFT)

        std_14_rbutton = Radiobutton(std_options_labelframe, text="c++14", variable=selected_std, value="3")
        std_14_rbutton.pack(side=LEFT)

        std_17_rbutton = Radiobutton(std_options_labelframe, text="c++17", variable=selected_std, value="4")
        std_17_rbutton.pack(side=LEFT)

        entry_label = Label(self, text="Output File Name:")
        entry_label.grid(row=4, column=3, sticky="w")

        output_entrybox = Entry(self, textvariable=output_str)
        output_entrybox.grid(row=4, column=3, columnspan=3, sticky="e", padx=5)

        compile_button = Button(self, text="Compile", command=self.compile_event(output_str))#, selected_std))
        compile_button.grid(row=5, column=4)

        exit_button = Button(self, text="Exit", command=self.exit_program)
        exit_button.grid(row=5, column=5, sticky="e", padx=5, pady=5)

    def exit_program(self):
        exit()

    def file_selection(self):
        #todo: file selector
        print("Implement file selection at some point")

    def file_remove(self):
        #todo: file remove if I get that far
        print("Should maybe remove selected files")

    def g_check(self):
        #todo: -g checkbox
        print("It's not going to work anyway")

    def radio_sel(self, std_selected_option):
        #todo: implement radio buttons setting something
        print("Radio buttons work better when the selection actually does something")
        #print(std_selected_option)

    def compile_event(self, out_str):
        print(out_str)
    #    print(std_string)


root = Tk()

root.geometry("600x300")
app = Window()
root.mainloop()
"""


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

