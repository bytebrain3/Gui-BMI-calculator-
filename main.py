import tkinter as tk
from tkinter import ttk

def calculate():
    weights = float(weight_Entry.get())
    heights = float(heightentry.get())
    #output_var.set(heights)
	
    cal = float(heights*30.48/100)
    BMI = float(weights/cal**2)
    bmi = format(BMI, '.2f')
    output.config(text=f"Your BMI : {bmi}")
	
    undr = 18.5
    normal = 18.5
    normal2 = 24.9
    over = 25
    over2 = 29.9
    obese = 30
    obese2 = 34.9
    extrem = 35
    bmi = float(bmi)
    if bmi < undr:
	situation.config(text="You Are Underweight")
    elif bmi <= normal:
	situation.config(text=f"it's normal ")
    elif bmi <= normal2:
	situation.config(text="it's normal")
    elif bmi <= over:
	situation.config(text="it’s over")
    elif bmi <= over2:
	situation.config(text="it’s over")
    elif bmi <= obese:
	situation.config(text="it’s Obese")
    elif bmi <= obese2:
	situation.config(text="it’s Obese")
    elif bmi >= extrem:
	situation.config(text="it’s  Extream")
#Creat window 
window = tk.Tk()
# define the size of window 
window.geometry("700x500")
# define the title of window 
window.title("BMI Calculator")
# define background colour
window.configure(bg='#121929')

#top label [BMI calculator]
text = ttk.Label(master = window,
				text= "BMI CALCULATOR",
				background="#121929",
				foreground="white").pack(pady=10)

#for weight Label [weight]
weight = ttk.Label(master = window,
		   text="Width",
		   background="#121929",
		   foreground="white").pack(pady=2)
# input the weight value 				  
weight_Entry = tk.Entry(master= window,
			background="#121929",
                	foreground="white")
#for display  the input label 
weight_Entry.pack()

#for heights label [height]
height = ttk.Label(master = window,
		   text="height",
		   background="#121929",
		   foreground="white").pack(pady=5)
#inpit the heights 
heightentry = tk.Entry(master = window,
		       background="#121929",
		       foreground="white")
#for display the heights input feild 
heightentry.pack(pady=5)

#for perform the calculat task it's creat a button				  				  
btn = ttk.Button(master = window,
		 text = "calculate",
		 command = calculate)
#display the button 
btn.pack(pady=5)

#output display the Actual BMI [your bmi is : {bmi}]
output = ttk.Label(master = window,
		   text = "",
		   background='#121929',
		   font ="monospace 12 bold",
		   foreground="white")
#disply the output lable 
output.pack(pady=5)
#for display the current position of your body . According to the BMI CALCULATOR 
situation = ttk.Label(master = window,
		      text = "",
		      background='#121929',
		      font ="monospace 8 bold",
		      foreground="white")
situation.pack(padx=5)

window.mainloop()
