#!/usr/bin/python3
from tkinter import *
from tkinter import filedialog

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
std_sel_option = StringVar()
std_sel_option.set(1)
debug_selected = IntVar()


def exit_program():
    exit()


def file_selection():
    #todo: file selector: figure out how to add multiple files and get the listbox to scrool hori
    sel_files = filedialog.askopenfilenames()
    sel_files = root.tk.splitlist(sel_files)
    selected_files_box.insert(END, sel_files)
    debug_test(sel_files)

def debug_test(list):
    print(list)


def file_remove():
    #todo: file remove if I get that far
    print("Should maybe remove selected files")


def g_check():
    #todo: -g checkbox
    print("It's not going to work anyway")
    print(debug_selected.get())


def radio_sel():
    #todo: implement radio buttons setting something
    print("Radio buttons work better when the selection actually does something")
    print(std_sel_option.get())


def compile_event():
    print(output_entrybox.get())
    print(std_sel_option.get())
    print(debug_selected.get())




title_label = Label(text="Compiler Interface")
title_label.grid(row=1, columnspan=5)

file_select_button = Button(text="Select Files", command=file_selection)
file_select_button.grid(row=2, column=1, sticky="s")

file_remove_button = Button(text="Remove Selected", command=file_remove)
file_remove_button.grid(row=2, column=2, sticky="s")

#file_select_label = Label(text="Selected Files")
#file_select_label.grid(row=2, column=1)

selected_files_box = Listbox(selectmode=MULTIPLE, height=17, width=30)
selected_files_box.grid(row=3, column=1, rowspan=4, columnspan=2, padx=5, pady=0, sticky="s")

selected_files_xscroll = Scrollbar(selected_files_box, orient="horizontal")

options_labelframe = LabelFrame(text="Compile Options")
options_labelframe.grid(row=3, column=3, columnspan=2)

debug_checkbox = Checkbutton(options_labelframe, text="-g", variable=debug_selected, command=g_check)
debug_checkbox.pack(side=LEFT)

std_labelframe = LabelFrame(options_labelframe, text="-std Options")
std_labelframe.pack(side=LEFT)

std_98_rbutt = Radiobutton(std_labelframe, text="c++98", variable=std_sel_option, value="-std=c++98", command=radio_sel)
std_98_rbutt.pack(side=LEFT)
std_98_rbutt.select()

std_11_rbutt = Radiobutton(std_labelframe, text="c++11", variable=std_sel_option, value="-std=c++11", command=radio_sel)
std_11_rbutt.pack(side=LEFT)

std_14_rbutt = Radiobutton(std_labelframe, text="c++14", variable=std_sel_option, value="-std=c++14", command=radio_sel)
std_14_rbutt.pack(side=LEFT)

std_17_rbutt = Radiobutton(std_labelframe, text="c++17", variable=std_sel_option, value="-std=c++17", command=radio_sel)
std_17_rbutt.pack(side=LEFT)

entry_label = Label(text="Output File Name:")
entry_label.grid(row=4, column=3, sticky="w", padx=5)

output_entrybox = Entry(width=55, textvariable=output_str)
output_entrybox.grid(row=4, column=2, columnspan=2, sticky="e", padx=5)

compile_button = Button(text="Compile", command=compile_event)
compile_button.grid(row=5, column=3, sticky="e", padx=5)

compile_result_label = Label(text="Compile Result:")
compile_result_label.grid(row=5, column=3, sticky="sw", padx=5)

compile_result_textbox = Text(height=10)
compile_result_textbox.grid(row=6, column=3, padx=5)

exit_button = Button(text="Exit", command=exit_program)
exit_button.grid(row=7, column=3, sticky="e", padx=5, pady=5)


root.mainloop()

