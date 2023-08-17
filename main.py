from tkinter import *
from tkinter import ttk

win = Tk()
win.title("Sachith Priyamantha")
win.config(bg = "cyan")
win.geometry("600x570")


name_label = Label(win,text="Sachi Weather App",
                   font=("monospace",35,"bold"))

name_label.place(x=50,y=60,height=50,width=500)

list_name = ["Central Province",
    "Eastern Province",
    "North Central Province",
    "Northern Province",
    "North Western Province",
    "Sabaragamuwa Province",
    "Southern Province",
    "Uva Province",
    "Western Province"]
com = ttk.Combobox(win,text="Sachi Weather App",values=list_name,
                   font=("monospace",20,"bold"))
com.place(x=50,y=120,height=40,width=500)

done_button = Button(win,text="Done",
                   font=("monospace",20,"bold"))
done_button.place(y=190,height=50,width=100,x=250)


w_label = Label(win,text="Weather Climate",
                   font=("monospace",20))
w_label.place(y=260,height=50,width=210,x=25)
w_label1 = Label(win,text="",
                   font=("monospace",20))
w_label1.place(y=260,height=50,width=210,x=250)


wb_label = Label(win,text="Weather Description",
                   font=("monospace",16))
wb_label.place(y=330,height=50,width=210,x=25)
wb_label1 = Label(win,text="",
                   font=("monospace",16))
wb_label1.place(y=330,height=50,width=210,x=250)


temp_label = Label(win,text="Temperature",
                   font=("monospace",20))
temp_label.place(y=400,height=50,width=210,x=25)
temp_label1 = Label(win,text="",
                   font=("monospace",20))
temp_label1.place(y=400,height=50,width=210,x=250)


per_label = Label(win,text="Pressure",
                   font=("monospace",20))
per_label.place(y=470,height=50,width=210,x=25)
per_label1 = Label(win,text="",
                   font=("monospace",20))
per_label1.place(y=470,height=50,width=210,x=250)








win.mainloop()