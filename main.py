from tkinter import *
from tkinter import ttk

win = Tk()
win.title("Sachith Priyamantha")
win.config(bg = "cyan")
win.geometry("600x500")


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

win.mainloop()