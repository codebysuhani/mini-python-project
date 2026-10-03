import tkinter as tk  #Python's built-in library used to create GUI (Graphical User Interface) applications.
from time import strftime   #Take the strftime function from the time module and make it available in this program 

root = tk.Tk()  #This creates the main window of our application.
root.title("DIGITAL CLOCK")  #This sets the title of our window.

def time():
    string = strftime('%H:%M:%S %p \n %D')  #It gets the current time and date and stores it in string.
    label.config(text=string)
    label.after(1000,time)  #This is what makes the clock update every second.

label = tk.Label(root,font=('calibri', 45, 'bold'), background='pink', foreground='black')
label.pack(anchor='center')  #This tells Tkinter where/how to place the label.

time()  #This calls the function we created earlier.

root.mainloop()  #This keeps the Tkinter window running.
