from tkinter import *
from tkinter import ttk
import requests


def data_get():
    city = city_name.get()
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=02076a56f003e2a2f011aee29d696df9").json()
    w_label1.config(text=data["weather"][0]["main"])
    wb_label1.config(text=data["weather"][0]["description"])
    temp_label1.config(text=str(int(data["main"]["temp"]-273.15)))
    per_label1.config(text=data["main"]["pressure"])











win = Tk()
win.title("Sachith Priyamantha")
win.config(bg = "sky blue")
win.geometry("600x570")


name_label = Label(win,text="Sri Lanka Weather App",
                   font=("monospace",32,"bold"))

name_label.place(x=50,y=60,height=50,width=500)

city_name = StringVar()

list_name = ["Central Province",
    "Eastern Province",
    "North Central Province",
    "Northern Province",
    "North Western Province",
    "Sabaragamuwa Province",
    "Southern Province",
    "Uva Province",
    "Western Province"]
com = ttk.Combobox(win,text="Sachith Weather App",values=list_name,
                   font=("monospace",18,"bold"),textvariable=city_name)
com.place(x=50,y=120,height=40,width=500)

w_label = Label(win,text="Weather Climate",
                   font=("monospace",18))
w_label.place(y=260,height=50,width=210,x=25)
w_label1 = Label(win,text="",
                   font=("monospace",20))
w_label1.place(y=260,height=50,width=210,x=250)


wb_label = Label(win,text="Weather Description",
                   font=("monospace",16))
wb_label.place(y=330,height=50,width=210,x=25)
wb_label1 = Label(win,text="",
                   font=("monospace",18))
wb_label1.place(y=330,height=50,width=210,x=250)


temp_label = Label(win,text="Temperature (°C)",
                   font=("monospace",18))
temp_label.place(y=400,height=50,width=210,x=25)
temp_label1 = Label(win,text="",
                   font=("monospace",20))
temp_label1.place(y=400,height=50,width=210,x=250)


per_label = Label(win,text="Pressure (Hg)",
                   font=("monospace",18))
per_label.place(y=470,height=50,width=210,x=25)
per_label1 = Label(win,text="",
                   font=("monospace",20))
per_label1.place(y=470,height=50,width=210,x=250)

done_button = Button(win,text="Click",
                   font=("monospace",20,"bold"),command=data_get)
done_button.place(y=190,height=50,width=100,x=250)






win.mainloop()