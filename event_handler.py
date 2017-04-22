import Tkinter as tk


def doorbell(event):
	print("You rang the doorbell!")


window = tk.Tk()
window.geometry("300x200")

label1 = tk.Label(text="Banana")
label1.grid(column=0, row=0)

label2 = tk.Label(text="Apple")
label2.grid(column=1, row=0)

button1 = tk.Button(window, text="Doorbell")
button1.grid(column=0, row=1)

button2 = tk.Button(window, text="10")
button2.grid(column=1, row=1)

button1.bind("<Button-1>", doorbell)

window.mainloop()