import tkinter as tk
from random import randrange
my_w = tk.Tk()
width,height=410,410 # set the variables 
d=str(width)+"x"+str(height+40)
my_w.geometry(d) 
c1 = tk.Canvas(my_w, width=width-10, height=height-10)
c1.grid(row=1,column=0,padx=5,pady=5)
x1,y1,x2,y2=5,5,width-5,height-5
gap=25

def my_draw():
    global x1,y1,x2,y2    
    color_c='#%02x%02x%02x' % (randrange(256), randrange(256), randrange(256))
    c1.create_oval(x1, y1, x2,y2,fill=color_c)
    #c1.create_rectangle(x1, y1, x2,y2,fill=color_c)
    x1,y1,x2,y2=x1+gap,y1+gap,x2-gap,y2-gap
    print(x1)
   
    if (x1<(width/2)):
        c1.after(500,my_draw)
        
    else:
        return    
my_draw()
def restart():
    global x1,y1,x2,y2
    x1,y1,x2,y2=5,5,width-5,height-5
    
    my_draw()
b1=tk.Button(my_w,text='Restart',command=lambda:restart())
b1.grid(row=2,column=0)
my_w.mainloop()