import tkinter
import math
# To provide functionalities
def click(val):
    e = entry.get()  # getting the value
    ans = " "

    try:
        # To clear the last inserted text
        if val == "⌫":
            e = e[0:len(e) - 1]  # deleting the last entered value
            entry.delete(0, "end")
            entry.insert(0, e)
            return
        # To delete everything
        elif val == "AC":
            entry.delete(0, "end")
        # Square root
        elif val == "√":
            ans = math.sqrt(eval(e))
           
        # division operator
        elif val == chr(247):
            entry.insert("end", "/")
            return

        elif val == "=":
            ans = eval(e)

        else:
            entry.insert("end", val)
            return

        entry.delete(0, "end")
        entry.insert(0, ans)

    except SyntaxError:
        pass


# Created the object
root = tkinter.Tk()

# Setting the title and geometry
root.title("Sandeep Calculator")
root.geometry("430x390+90+80")

# Setting the background color
root.config(bg="Blue")


# Entry field
entry = tkinter.Entry(root, font=("Black", 18, "bold"), bg="Cyan", fg="Black", bd=10, width=30)
entry.grid(row=0, column=0, columnspan=8)

# buttons list
button_list = ["1", "2", "3","AC","⌫","4", 
               "5", "6", "+","*","7", "8",
                 "9","-",chr(247),"0","00",".", "=", "√",]
r = 1
c = 0
# Loop to get the buttons on window
for i in button_list:
    # Buttons
    button = tkinter.Button(root, width=5, height=2, bd=2, text=i, bg="Sky blue", fg="black",
                            font=("arial", 18, "bold"), command=lambda button=i: click(button))
    button.grid(row=r, column=c, pady=1)
    c += 1
    if c > 4:
        r += 1
        c = 0

# Makes window on loop
root.mainloop()