from tkinter import *
win=Tk()
win.title('cows and bulls')
e = Entry(win,width=35,borderwidth=5,bg='yellow')
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)
def click(x):
    current=e.get()
    
    e.delete(0,END)
    e.insert(0,str(current)+str(x))

def clear():
    e.delete(0,END)

from random import *

def bingo():
    user_entry=(e.get())
    e.delete(0,END)
    y = str(randint(1000,9999))
    L=[]
    for i in y:
        L.append(i)
    if user_entry!=y:
        cows = 0
        bulls = 0
        for i in range(4):
            if user_entry[i]==y[i]:
                cows = cows+1
            if user_entry[i]!=y[i] and user_entry[i] in L:
                bulls = bulls+1
        e.insert(0,'no of cows:'+str(cows)+'  '+'no of bulls:'+str(bulls))
        
       
        
        
        
    else:
        e.insert(0,'game over the random no generated:'+user_entry)
        
    
   
    
btn1 = Button(win,text="1",padx=40,pady=20,command=lambda:click(1))
btn2 = Button(win,text="2",padx=40,pady=20,command=lambda:click(2))
btn3 = Button(win,text="3",padx=40,pady=20,command=lambda:click(3))
btn4 = Button(win,text="4",padx=40,pady=20,command=lambda:click(4))
btn5 = Button(win,text="5",padx=40,pady=20,command=lambda:click(5))
btn6 = Button(win,text="6",padx=40,pady=20,command=lambda:click(6))
btn7 = Button(win,text="7",padx=40,pady=20,command=lambda:click(7))
btn8 = Button(win,text="8",padx=40,pady=20,command=lambda:click(8))
btn9 = Button(win,text="9",padx=40,pady=20,command=lambda:click(9))
btn0 = Button(win,text="0",padx=40,pady=20,command=lambda:click(0))

btneql = Button(win,text='=',padx=40,pady=20,command=lambda:bingo())
btnclr = Button(win,text='clear',padx=79,pady=20,command=lambda:clear())
btnclr.grid(row=4,column=1,columnspan=2)
btneql.grid(row=4)
btn1.grid(row=1,column=0)
btn2.grid(row=1,column=1)
btn3.grid(row=1,column=2)
btn4.grid(row=2,column=0)
btn5.grid(row=2,column=1)
btn6.grid(row=2,column=2)
btn7.grid(row=3,column=0)
btn8.grid(row=3,column=1)
btn9.grid(row=3,column=2)

win.mainloop()
