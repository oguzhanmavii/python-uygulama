import tkinter as Tkinter
from datetime import datetime
from tkinter import filedialog


counter=0
running=False


def counter_label(label):
    def count():
        if running:
            global counter
            if counter == 0:
                display = 'Hazir!'
            else:
                tt = datetime.utcfromtimestamp(counter)
                string =tt.strftime('%H:%M:%S')
                display=string

            label['text']=display

            label.after(1000,count)
            counter=counter+1

    count()


def Start(label):
    global running
    running = True
    counter_label(label)
    start['state']='disable'
    stop['state']='normal'
    reset['state']='normal'

def Stop(label):
    global running
    running = False
    start['state'] = 'normal'
    stop['state'] = 'disabled'
    reset['state']='normal'


def Reset(label):
    global counter
    counter = 0
    if not running:
        reset['state']='disable'
        label['text']='00:00:00'
    else:
        label['text']='00:00:00'


root=Tkinter.Tk()
root.title('Kronometre App')
root.configure(bg='orange')
root.geometry("700x350")
label=Tkinter.Label(root,text='Hazir!',fg='red',font='Verdana 30 bold')
label.place(relx=0.5,rely=0.5,anchor='center')
label.pack()
f=Tkinter.Frame(root,width=300,height=300)

start=Tkinter.Button(f,text='Basla',width=6,command=lambda:Start(label))
stop=Tkinter.Button(f,text='Durdur',width=6,state='disable',command=lambda:Stop(label))
reset=Tkinter.Button(f,text='Sifirla',width=6,state='disable',command=lambda:Reset(label))
f.pack(anchor='center',pady=5)
start.pack(side='left')
stop.pack(side='left')
reset.pack(side='left')
root.mainloop()