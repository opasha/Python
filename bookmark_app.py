import Tkinter as tk
import webbrowser

URL1 = 'https://www.google.com'
URL2 = 'https://www.youtube.com'

def doorbell(event):
	print("You rang the doorbell!")

def open_google(event):
	webbrowser.open_new_tab(URL1)

def open_youtube(event):
	webbrowser.open_new_tab(URL2)


window = tk.Tk()
window.geometry("300x200")

label1 = tk.Label(text="Door")
label1.grid(column=0, row=0)

label2 = tk.Label(text="Websites")
label2.grid(column=1, row=0)

button1 = tk.Button(window, text="Doorbell")
button1.grid(column=0, row=1)

button2 = tk.Button(window, text="Google")
button2.grid(column=1, row=1)

button3 = tk.Button(window, text="Youtube")
button3.grid(column=1, row=2)

button1.bind("<Button-1>", doorbell)  # Button-1 refers to left click of your mouse

button2.bind("<Button-1>", open_google)

button3.bind("<Button-1>", open_youtube)

window.mainloop()