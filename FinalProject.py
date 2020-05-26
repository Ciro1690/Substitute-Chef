from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
from tkinter import filedialog
import json
import requests

#Creates the title
root = Tk()
root.title("Substitute Chef")
root.geometry("500x600")
root.configure(background="grey")

#Insert an Image
my_img = ImageTk.PhotoImage(Image.open("chef.jpg"))
image = Label(image=my_img)
image.grid(row=1,column=0)

name = Entry(root, width = 50)
name.grid(row=2,column=0)
name.get()


#Allows you to click on the button
def myClick():
    myLabel = Label(root,text="Welcome to Substitute Chef, Chef "+name.get() + "!")
    myLabel.grid(row=3,column=0)

#Connect button with myClick
myButton = Button(root,text="Enter your name in the text box and click here.",command=myClick,fg="blue")
myButton.grid(row=4,column=0,pady=10)

#get zipcode and show city
def zip_lookup():

    try:
        api_request = requests.get(
            "http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zip.get() + "&distance=100&API_KEY=2BD82EC1-20B4-4EB0-8A1F-49D2771204C4")
        api = json.loads(api_request.content)
        city = api[0]['ReportingArea']

        myLabel = Label(root,text=city,font=("Helvetica",15))
        myLabel.grid(row=5,column=0,pady=10)

    except Exception as e:
        api = "Error"

zip = Entry(root)
zip.grid(row=6,column=0)

zipButton = Button(root, text="Lookup zipcode",command=zip_lookup,fg="blue")
zipButton.grid(row=7,column=0,pady=10)

#Drop down menu for positions
def show_positions():
    myLabel = Label(root,text=var.get()).grid(row=8,column=0)

var = StringVar()
var.set("Prep Cook")
drop = OptionMenu(root,var, "Prep Cook", "Line Cook", "Sous Chef")
drop.grid(row=9,column=0)
myButton = Button(root,text="Show Selection",command=show_positions).grid(row=10,column=0,pady=(0,10))

#Drop down menu for availability
def show_availability():
    myLabel = Label(root,text=var1.get()).grid(row=11,column=0)

var1 = StringVar()
var1.set("Individual Shifts")
drop = OptionMenu(root,var1, "Individual Shifts", "Part time", "Full time")
drop.grid(row=12,column=0)
myButton = Button(root,text="Show Selection",command=show_availability).grid(row=13,column=0,pady=(0,10))

#Creates a popup when you click the button for the disclaimer
def popup():
    messagebox.showinfo("Equal Opportunity Employment","We do not discriminate employment based on race, sex, religion etc.")
Button(root, text="Disclaimer", command=popup,fg="blue").grid(row=14,column=0)

#Quit to get out of program
button_quit = Button(root,text="Exit program",command=root.quit,fg="blue")
button_quit.grid(row=15,column=0,pady=20)

root.mainloop()