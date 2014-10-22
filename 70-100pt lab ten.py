

from Tkinter import *
root = Tk()

# The Canvas
drawpad = Canvas(root, width=800,height=600, background='white')
drawpad.grid(row=0, column=1)
#house body
Housebody = drawpad.create_rectangle(100,200,500,600, fill='blue')
Chimney = drawpad.create_rectangle(400,50,450,200, fill = 'black')
roof = drawpad.create_polygon(100,200,300,0,500,200, fill = 'light blue')
door = drawpad.create_rectangle(200,400,300,600, fill ='gold')
#four windows for house
window1 = drawpad.create_rectangle(350,250,450,325, fill = 'black')
window2 = drawpad.create_rectangle(200,250,300,325, fill = 'black')
window3 = drawpad.create_rectangle(350,400,450,475, fill = 'black')
window4 = drawpad.create_rectangle(350,510,450,590, fill = 'black')
#doorknob
doorknob = drawpad.create_oval(280,500,300,520, fill = 'white')
# grass
Grass = drawpad.create_rectangle(0,590,800,600, fill = 'green')

root.mainloop()