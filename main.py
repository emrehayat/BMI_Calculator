from tkinter import *

window = Tk()
window.title("BMI CALCULATOR")
window.minsize(width=350, height=450)

label_1 = Label(text="ENTER YOUR WEIGHT (kg)")
label_1.place(x=100, y=50)

label_2 = Label(text="ENTER YOUR HEIGHT (m)")
label_2.place(x=100, y=200)

entry_1 = Entry()
entry_1.place(x=105, y=100)

entry_2 = Entry()
entry_2.place(x=105, y=250)
def click_button():
    your_input = entry_1.get()
    your_input_2 = entry_2.get()

    try:
        weight =  float(your_input)
        height =  float(your_input_2)
    except:
        result_label.config(text="Enter valid values\nfor weight and height")
        return
    if weight <= 0 or height <= 0:
        result_label.config(text="Weight and height must be\npositive(+) numbers")
        return

    bmi = weight / (height ** 2)

    if bmi < 18.5:
        result_label.config(text=""f"Your BMI is {round(bmi, 2)}.\nYou are Underweight", fg="red")
    elif 18.5 <= bmi < 24.9:
        result_label.config(text=""f"Your BMI is {round(bmi, 2)}.\nYou are Healthy Weight", fg="green")
    elif 25 <= bmi < 29.9:
        result_label.config(text=""f"Your BMI is {round(bmi, 2)}.\nYou are Overweight", fg="red")
    else:
        result_label.config(text=""f"Your BMI is {round(bmi, 2)}.\nYou are Obesity", fg="red")

my_button = Button(text="RESULT", command=click_button)
my_button.place(x=140, y=300)


result_label = Label(text="")
result_label.place(x=110, y=350)

window.mainloop()