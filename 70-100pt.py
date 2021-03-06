0##########################################
#                                        #
#             Draw a house!              #
#                                        #
##########################################

# Use create_line(), create_rectangle() and create_oval() to make a 
# drawing of a house using the tKinter Canvas widget.

# 70pt: House outline (roof and the house)
# 80pt: Square windows and a door
# 90pt: A door handle plus a chimney!
# 100pt: Green grass on the ground and a red house!

# Minus 5pts if your code has no comments
# Minus 10pts if you only commit once to github

from Tkinter import *
root = Tk()

# Create the canvas widget
drawpad = Canvas(root, width=800,height=600, background='white')
drawpad.grid(row=0, column=1)


# Insert your code here to draw the house!
Housebody = drawpad.create_rectangle(100,200,500,600, fill='red')
line1 = drawpad.create_line(100, 200,300,0)
line2 = drawpad.create_line(500, 200,300,0)
door = drawpad.create_rectangle(200,400,300,600, fill ='brown')
window1 = drawpad.create_rectangle(350,250,450,325, fill = 'blue')
window2 = drawpad.create_rectangle(200,250,300,325, fill = 'blue')




root.mainloop()
