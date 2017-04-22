import Tkinter as tk

window = tk.Tk()
window.geometry("300x200")

label1 = tk.Label(text="Banana")
label1.grid(column=0, row=0)

label2 = tk.Label(text="Apple")
label2.grid(column=1, row=0)

label3 =tk.Label(text="Cherry")
label3.grid(column=2,row=0)

button1 = tk.Button(text="5")
button1.grid(column=0, row=1)

button2 = tk.Button(text="10")
button2.grid(column=1, row=1)

button3 = tk.Button(text="15")
button3.grid(column=2, row=1)

window.mainloop()