#Imports the moduels needed
import Tkinter as tk 
 
from PIL import Image, ImageTk #EDIT: This module worked for me after I installed Pillow in my computer from "http://pillow.readthedocs.io/en/4.1.x/installation.html"
import webbrowser #imports the module for URL links
import io, base64 #imports the module for letting images be seen without changing code

#adds the URL and window for the program tkinter
URL = "http://pizzahut.com.au" #the URL used
window = tk.Tk() #this makes the tkinter window appear
window.title("window App") #title of the app
window.geometry("500x500") #size of the app

#define IntVar variables
cvar = tk.IntVar()
cvar2 = tk.IntVar()
cvar3 = tk.IntVar()

#defines the webbrowser function
def open_ph(event):
	webbrowser.open_new_tab(URL) 

#define the main button and the click button
button = tk.Button(window, text="Welcome to Awesome pizza")
button.grid(column=0, row=0)
button.bind("<Button-1>", open_ph)

#define check buttons
check1 = tk.Checkbutton(window, text="Meat Lovers", variable=cvar, onvalue=1, offvalue=0)
check1.grid(column=0, row=1, padx=(5, 95))
check2 = tk.Checkbutton(window, text="Supreme", variable=cvar2, onvalue=1, offvalue=0)
check2.grid(column=0, row=3, padx=(10, 120))
check3 = tk.Checkbutton(window, text="Vegetarian", variable=cvar3, onvalue=1, offvalue=0)
check3.grid(column=0, row=5, padx=(10, 120))

#define the option menu
choice = tk.OptionMenu(window, tk.IntVar(), "Select your size!", "Small", "Medium", "Large")
choice.grid(column=1, row=0, padx=(5, 95))

#define labels
name_label = tk.Label(text="Name")
name_label.grid(column=1, row=1, padx=(10, 120))
number_label = tk.Label(text="Contact number")
number_label.grid(column=1, row=3, padx=(5, 95))
address_label = tk.Label(text="Delivery address")
address_label.grid(column=1, row=5, padx=(5, 95))

#define entries
name_entry = tk.Entry()
name_entry.grid(column=1, row=2, padx=(5, 95), sticky="EWNS")
number_entry = tk.Entry()
number_entry.grid(column=1, row=4, padx=(5, 95), sticky="EWNS")
address_entry = tk.Entry()
address_entry.grid(column=1, row=6, padx=(5, 95), sticky="EWNS")

#defines the print function for the message board
def message_customer():
	print(name_entry.get())
	print(number_entry.get())
	print(address_entry.get())
	name = Person(name_entry.get(), number_entry.get(), address_entry.get())                                                  
	text_answer = tk.Text(master=window, height=10, width=20)
	text_answer.grid(column=1, row=7, padx=(10, 120))
	text_answer.insert("1.0", "Thank you {name} for your order,it should arrive at {address} within 30 mintues!, we will contact you on {number} when we are close".format(name=name.name, number=name.number, address=name.address))

#define click button function
click_button = tk.Button(text="Complete Order", command=message_customer)
click_button.grid(column=1, row=7, padx=(5, 95))

#create class method
class Person:
	def __init__(self, name, number=None, address=None):
		self.name = name
		self.number = number
		self.address = address

#configuration of main button and click button
button.configure(foreground="white", background="black")
click_button.configure(foreground="white", background="black")
#configurations of labels
name_label.configure(foreground="white", background="black")
number_label.configure(foreground="white", background="black")
address_label.configure(foreground="white", background="black")
#configuration of the options menu and the tkinter window
choice.configure(foreground="white", background="black")
window.configure(background="red")

#encodes the images from .jpg or .png files to base64 string(lets others view the image)
img_b64 = '''
'''
# Decode the JPEG data & "wrap" it into file-like object
fh = io.BytesIO(base64.b64decode(img_b64))

image = Image.open(fh, mode = 'r')
image.thumbnail((100, 100), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(image)
label_image = tk.Label(image=photo)
label_image.grid(column=0, row=2, padx=(5, 95))

img2_b64 = '''
'''
fh = io.BytesIO(base64.b64decode(img2_b64))

second_photo = Image.open(fh, mode = 'r')
second_photo.thumbnail((100, 100)), Image.ANTIALIAS
second_photo = ImageTk.PhotoImage(second_photo)
label_second_photo = tk.Label(image=second_photo)
label_second_photo.grid(column=0, row=4, padx=(5, 95))

img3_b64 = '''
'''
fh = io.BytesIO(base64.b64decode(img3_b64))

third_picture = Image.open(fh, mode = 'r')
third_picture.thumbnail((100, 100)), Image.ANTIALIAS
third_picture = ImageTk.PhotoImage(third_picture)
label_third_picture = tk.Label(image=third_picture)
label_third_picture.grid(column=0, row=6, padx=(5, 95))

window.mainloop()#lets the window stay open, very important