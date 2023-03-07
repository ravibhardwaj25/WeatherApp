from tkinter import *
from tkinter import ttk
import requests

def data_get():
    city = city_name.get()
    # Here '&appid = your_api(your openweather api)' you need to create account on openweathermap.org to get your unique api.
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=your_api").json()
    w_label1.config(text=data["weather"][0]["main"])
    wd_label1.config(text=data["weather"][0]["description"])
    temp_label1.config(text=str(int(data["main"]["temp"]-273.15)))
    pres_label1.config(text=data["main"]["pressure"])
    humid_label1.config(text=data["main"]["humidity"])
    wind_label1.config(text=data["wind"]["speed"]*3.6)

win = Tk()
win.title("Weather App")
win.config(bg="light blue")
win.geometry("600x700")

img= PhotoImage(file="R.png")
label= Label(image=img)
label.place(x=0,y=0)
name_label= Label(win,text="Weather Today",
                  font=("Time New Roman",35,"bold"))
name_label.place(x=75,y=50,height=50,width=450)

city_name= StringVar()
list_name= ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]
com= ttk.Combobox(win,values=list_name,
                  font=("Time New Roman",25,"bold","italic"),textvariable=city_name)
com.place(x=75,y=120,height=50,width=450)

w_label= Label(win,text="Weather",
                  font=("Time New Roman",17,"bold"))
w_label.place(x=55,y=210,height=50,width=250)
w_label1= Label(win,text="",
                  font=("Time New Roman",17,"bold"))
w_label1.place(x=325,y=210,height=50,width=250)

wd_label= Label(win,text="Weather Description",
                  font=("Time New Roman",17,"bold"))
wd_label.place(x=55,y=280,height=50,width=250)
wd_label1= Label(win,text="",
                  font=("Time New Roman",17,"bold"))
wd_label1.place(x=325,y=280,height=50,width=250)

temp_label= Label(win,text="Temperature",
                  font=("Time New Roman",17,"bold"))
temp_label.place(x=55,y=350,height=50,width=250)
temp_label1= Label(win,text="",
                  font=("Time New Roman",17,"bold"))
temp_label1.place(x=325,y=350,height=50,width=250)

pres_label= Label(win,text="Pressure",
                  font=("Time New Roman",17,"bold"))
pres_label.place(x=55,y=420,height=50,width=250)
pres_label1= Label(win,text="",
                  font=("Time New Roman",17,"bold"))
pres_label1.place(x=325,y=420,height=50,width=250)

humid_label= Label(win,text="Humidity",
                  font=("Time New Roman",17,"bold"))
humid_label.place(x=55,y=490,height=50,width=250)
humid_label1= Label(win,text="",
                  font=("Time New Roman",17,"bold"))
humid_label1.place(x=325,y=490,height=50,width=250)

wind_label= Label(win,text="Wind Speed",
                  font=("Time New Roman",17,"bold"))
wind_label.place(x=55,y=560,height=50,width=250)
wind_label1= Label(win,text="",
                  font=("Time New Roman",17,"bold"))
wind_label1.place(x=325,y=560,height=50,width=250)

done_button= Button(win,text="Done",
                  font=("Time New Roman",20,"bold"),command=data_get)
done_button.place(x=200,y=630,height=50,width=200)

win.mainloop()