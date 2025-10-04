import tkinter

def button_clicked():
    km = float(input.get())*1.60934
    answer.config(text=f': {km}')

window = tkinter.Tk()
window.title("Miles to KM Converter")
window.minsize(width = 300 , height = 200)
window.config(padx = 50, pady = 50)

my_label = tkinter.Label(text = "Miles", font = ("Arial",24,"bold"))
my_label.grid(row = 0, column = 2)
my_label.config(padx = 10, pady = 10)

my_label_2 = tkinter.Label(text = "KM", font = ("Arial",24,"bold"))
my_label_2.grid(row = 1, column = 2)
my_label_2.config(padx = 10, pady = 10)

my_label_3 = tkinter.Label(text = "is equal to", font = ("Arial",24,"bold"))
my_label_3.grid(row = 1, column = 0)
my_label_3.config(padx = 10, pady = 10)

button = tkinter.Button(text = "Calculate", command = button_clicked)
button.grid(row = 2, column = 1)
button.config(padx = 10, pady = 10)


input = tkinter.Entry(width = 5)
input.grid(row = 0, column = 1)

answer = tkinter.Label(text = "", font = ("Arial",24,"bold"))
answer.grid(row = 1, column = 1)
answer.config(padx = 10, pady = 10)


window.mainloop()