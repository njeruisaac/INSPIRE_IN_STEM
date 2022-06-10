#1/usr/bin/python
#####################################################
#       Name : Isaac Njeru
#       Date : 7 / 6 / 22.
#####################################################
##############################################################
#gui examples using tkinker

from tkinter import *
window = Tk()
window.title("My Awesome App")
window.config(bg='white')
window.geometry("400x600")
f_name = Label(window,text = 'First Name', font= ('Times New Roman',20))
s_name = Label(window,text = 'Second Name', font= ('Times New Roman',20))
f_name.grid(column=60, row= 100)
s_name.grid(column=60, row= 120)
f_name.config(bg='white')
s_name.config(bg='white')

def open_popup():
    top = Toplevel(window)
    top.geometry("300x300")
    top.title("Pop Up Window")
    top.config(bg = 'Green')

    msg= Label(top,text= "Welcome to top")



btn = Button(window,text="Click Me")
btn.grid(column=120, row=150)
btn.config(bg="White")
btn.config(fg='Gold')

txt_box = Entry(window, text= "Enter Your Name")
txt_box.grid(column=120, row=100)
txt_box.config(bg='white')
txt_box.config(fg='Black')

txt_box = Entry(window, text= "Enter Your Name")
txt_box.grid(column=120, row=120)
txt_box.config(bg='white')
txt_box.config(fg='Black')

window.mainloop()