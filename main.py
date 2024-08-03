from tkinter import *
def cal():
    num = int(val.get())
    res = round(num * 1.6)
    ans.config(text=res)


window = Tk()
window.title("Miles to Km converter")
window.minsize(500, 300)
window.config(padx=100, pady=100)

val = Entry()
val.grid(column=1, row=0)

mile_label = Label(text="miles")
mile_label.grid(column=2, row=0)

equals = Label(text="is equal to")
equals.grid(column=0, row=1)

ans = Label(text=0)
ans.grid(column=1, row=1)

km = Label(text="Km")
km.grid(column=2, row=1)

button = Button(text="Calculate", command=cal)
button.grid(column=1, row=2)
button.config(padx=10, pady=10)

window.mainloop()
