
# NAME          :            Muhammad Hammad
# ROLL NO       :            0520
# EMAIL         :            mhammmad.503@gmail.com
# PROJECT NAME  :            Currency Converter App




# import library
from currency_converter import CurrencyConverter
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk
from tkinter import *


# currency list
currency = ["USD","EUR","CAD","INR","GBP","JPY","CHF","BGN","NZD","AUD","TRY","IDR","MYR","BRL","CNY","CZK","DKK","HKD","HUF","ISK","KRW","MXN"]


# import colour
clr0 = "#FFFFFF"   #"white"
clr1 = "#060708"   #"black"
clr2 = "#1E90FF"   #"dodger blue"
clr3 = "#E85051"   #"red"


# define variable
c = CurrencyConverter()


# create route
route = tk.Tk()
route.geometry("550x350")
route.title("Currency Converter")
route.config(bg=clr0)
route.resizable(height=FALSE, width=FALSE)


# main frame
main = Frame(route,relief="solid",width=300,height=260,bg=clr0)
main.grid(row=1,column=0)


# define function
def clicked():
     try:
        amount = float(value.get())
        currency1 = str(combo1.get())
        currency2 = str(combo2.get())
        data = c.convert(amount,currency1,currency2)

      
# display result
        result_text = f"{round(data ,2)}  {currency2}"
        lebel5 = tk.Label(main,text=result_text, font = "Times 18 bold",relief="solid",anchor=tk.CENTER,width=16,height=2,bg=clr2)
        lebel5.place(x=30, y=20)
    
        
# display error
     except ValueError:
        messagebox.showerror("Error", "invalid currency/currency not supported. Please enter a valid currency.")
     except ZeroDivisionError:
        messagebox.showerror("Error", "Cannot divide by zero.")
     except Exception as e:
        messagebox.showerror("Error", f"Conversion failed: {e}")


# top frame
top = Frame(route,width=600,height=60,bg=clr2)
top.grid(row=0,column=0)
    

# create title 
label1 = tk.Label(route,text= "Currency Converter",font= "arial 25 bold",bg=clr2,fg=clr1,anchor=CENTER)
label1.place (x=130, y=10)


# create entry box
value = Entry(route,width=22,relief="solid",justify=CENTER,font="Ivy 12 bold",bg=clr0,fg=clr1,)
value.place(x = 160, y = 240)


# create from label
from_label = Label(route,text="From",width=8,height=1,relief="flat",anchor=NW,font="Ivy 10 bold",bg=clr0,fg=clr1,)
from_label.place(x = 150, y = 150)


# create combobox 1
combo1 = ttk.Combobox(route,width=12,justify=CENTER,font="Ivy 10 ")
combo1["values"] = (currency)


# create to label
to_label = Label(route,text="To",width=8,height=1,relief="flat",anchor=NW,font="Ivy 10 bold",bg=clr0,fg=clr1,)
to_label.place(x = 280, y = 150)


# create combobox 2
combo2 = ttk.Combobox(route,width=12,justify=CENTER,font="Ivy 10")
combo2["values"] = (currency)


# create button
button= tk.Button(route,text = "Enter",font= "Ivy 18 bold",width=12,bg=clr2,fg=clr1, command =clicked)
button.place (x=170, y=290)


# combobox entery palace
combo1.place (x=150,y=180) 
combo2.place (x=280,y=180)


# run the mainloop
route.mainloop()
