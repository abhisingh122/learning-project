# # making google search

# from googlesearch import search as s

# keywords=input("enter a query")
# result = s(keywords,5)
# for i in result:
#     print(i)



# digital clock
import tkinter
from time import strftime
from tkinter import font
def clock():
    time1=strftime("%H : %M : %S %p")
    label.config(text=time1,font=("arial",150))
    label.after(1000,clock)

root=tkinter.Tk()
label=tkinter.Label(root)
label.pack()
clock()
root.mainloop()
    
