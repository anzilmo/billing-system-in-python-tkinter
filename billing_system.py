# billing system
from collections.abc import ItemsView
from operator import itemgetter
import tkinter as tk
from tkinter import ttk
def calculet():
    Quantity=float(quatity_text.get())
    price=float(price_text.get())
    total=Quantity*price
    total_text.delete(0,tk.END)
    total_text.insert(0,total)

def add():
    grande_total=0
    item=item_text.get()
    quy=quatity_text.get()
    price=price_text.get()
    total=total_text.get()


    table.insert("",tk.END, values=(item,quy,price,total))   

    item_text.delete(0,tk.END)
    quatity_text.delete(0,tk.END) 
    price_text.delete(0,tk.END)
    total_text.delete(0,tk.END)

    for item in table.get_children():
        valuse=table.item(item,"values")
        ind_total=float(valuse[3])
        grande_total+=ind_total
        g_total.configure(text=f"Total sell : {grande_total}")


Window = tk.Tk()
Window.title("billing model")
Window.geometry("800x500")
heading=tk.Label(Window,text="Billind Model")
heading.pack()

item_detals=tk.Frame(Window)
item_detals.pack()
for col in range(4):
    item_detals.columnconfigure(col,minsize=200)


item_label=tk.Label(item_detals,text=("Item Name"),font=("Arial",15))
item_label.grid(row=0,column=0)
item_quatity=tk.Label(item_detals,text=("Quantity."),font=("Arial",15))
item_quatity.grid(row=0,column=1)
item_price=tk.Label(item_detals,text=("Price"),font=("Arial",15))
item_price.grid(row=0,column=2)
item_total=tk.Label(item_detals,text=("Total Bill Amount"),font=("Arial",15))
item_total.grid(row=0,column=3)

item_text =tk.Entry(item_detals,font=("Arial",15),width=15)
item_text.grid(row=1,column=0)
quatity_text =tk.Entry(item_detals,font=("Arial",15),width=15,justify="right")
quatity_text.grid(row=1,column=1)
price_text =tk.Entry(item_detals,font=("Arial",15),width=15, justify="right")
price_text.grid(row=1,column=2)
total_text =tk.Entry(item_detals,font=("Arial",15),width=15,justify="right")
total_text.grid(row=1,column=3)

cla_btn =tk.Button(item_detals,text='Add amo',font=("arial",15),bg='red',fg='white',command=calculet)
cla_btn.grid(row=2,column=2,padx=10,pady=10)
add_btn =tk.Button(item_detals,text='Add table',font=("arial",15),bg='red',fg='white',command=add)
add_btn.grid(row=2,column=3,padx=10,pady=10)
prin_btn=tk.Button(item_detals,text="print",font=("arial",15),bg='red',fg='white',command=calculet)
prin_btn.grid(row=2,column=1,padx=10,pady=10)


table =ttk.Treeview(item_detals,columns=('item','quantity','price','total'),show="headings")
table.grid(row=3,column=0,columnspan=4,padx=5,pady=5)
table.heading("#1",text='Item')
table.heading("#2",text='Quantity')
table.heading("#3",text='Price')
table.heading("#4",text='Total')

g_total=tk.Label(Window, text="Total sell:",fg='green',font=("Arial",20))
g_total.pack(pady=5)

Window.mainloop()