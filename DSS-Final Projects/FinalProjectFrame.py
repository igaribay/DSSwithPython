from tkinter import *

def clear():
#-----Implement reset logic here -----------------------------------------------
    print("Implement reset logic here ")

root = Tk()
root.title('Industiral Engineering & Management Systems - Undergraduate Course')
root.geometry("1024x1024")

# create all of the main containers
header_frame = Frame(root, bg='cyan', width=450, height=50)
input_frame = Frame(root, bg='gray', width=450, height=200)
output_frame = Frame(root, bg='gray', width=450, height=200)
footer_frame = Frame(root, bg='cyan', width=450, height=20)

# layout all of the main containers
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

header_frame.grid(row=0, sticky="nsew")
input_frame.grid(row=1, sticky="nsew")
output_frame.grid(row=2, sticky="nsew")
footer_frame.grid(row=3, sticky="nsew")


label1 = Label(header_frame, bg="Cyan", fg="Black", height=2, text="DECISION SUPPORT SYSTEMS With Python")
label1.pack(fill=X)
label2 = Label(header_frame, bg="Gray", fg="Magenta", height=2, text="<Enter title of the project>")
label2.pack(fill=X)

label3 = Label(input_frame, bg="black", fg="White", text="Input Block")
label3.pack(fill=X)
label4 = Label(input_frame, bg="Magenta", fg="Black", width=2, wraplength=1, text="Final")
label4.pack(side=RIGHT, fill=Y)

#-----Implement here to display appropriate input fields---------------------------

inner_frame = Frame(input_frame, bg='gray', width=450, height=20)
inner_frame.pack(side=BOTTOM, fill=X)
button1 = Button(inner_frame, text="Results", bg="gray", fg="black" )
button1.pack(side=LEFT)
button2 = Button(inner_frame, text="Reset", bg="gray", fg="black", command=clear)
button2.pack(side=RIGHT)

#-----Implement the core logic here -----------------------------------------------

label5 = Label(output_frame, bg="black", fg="White", text="Output Block")
label5.pack(fill=X)
label6 = Label(output_frame, bg="Magenta", fg="Black", width=2, wraplength=1, text="Project")
label6.pack(side=RIGHT, fill=Y)

label7 = Label(footer_frame, bg="black", fg="White", text="Copy Right @2018, Complex Adaptive Systems Lab.")
label7.pack(fill=X)


#
# menu = Menu(root)
# root.config(menu=menu)
#
# subMenu = Menu(menu)
# menu.add_cascade(label="File", menu=subMenu)
# subMenu.add_command(label="New Project..", command=sample)
# subMenu.add_command(label="New File..", command=sample)
# subMenu.add_command(label="Save As", command=sample)
# subMenu.add_separator()
# subMenu.add_command(label="Settings", command=sample)
# subMenu.add_command(label="Exit", command=sample)
#
# editMenu = Menu(menu)
# menu.add_cascade(label="Edit", menu=editMenu)
# editMenu.add_command(label="Undo", command=sample)
# editMenu.add_command(label="Redo", command=sample)
# editMenu.add_command(label="Cut", command=sample)
# editMenu.add_command(label="Copy", command=sample)
# editMenu.add_command(label="Paste", command=sample)
#
# #-----Appropriate output(plots, tables, text, etc) should be displayed in this block-----------------------------------------------
# label4 = Label(topFrame, bg="White", fg="black", text="Output Block")
# label4.grid(columnspan=3)
#
# entry1 = Entry(topFrame)
# entry1.grid(row=1, column=1)

root.mainloop()
