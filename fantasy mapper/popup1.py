import sys
import matplotlib
from Tkinter import *
import Tkinter as tk

import tkMessageBox
#class popup1():


info = {}
load = bool
data_sent =bool
def ask():
    top = Toplevel()
    global load, data_sent
    load = False
    data_sent = False

    top.title("load")
    txt = Label(top, text = 'do you wish to load a map file?')
    txt.pack(padx =20, pady = 20)

    def choice():
        global load, data_sent
        load = True
        data_sent = True
        top.destroy()
    def choice2():
        global data_sent
        data_sent = True
        top.destroy()
    yes = Button(top, text="yes", width=20, command= choice )
    no =  Button(top, text="no", width=20, command= choice2 )
    yes.pack()
    no.pack()
    while data_sent == False:
        top.update()

    return load
def useroutput(a):
    top = Toplevel()
    top.title("marker Info")
    top.geometry("300x500+200+200")
    title = Label(top, text = a['title'])
    title.pack(padx =20, pady = 20)
    if a['type'] == 'ob':
        tpe = Label(top, text = 'character')
    if a['type'] == 'or':
        tpe = Label(top, text = 'Item')
    if a['type'] == 'oy':
        tpe = Label(top, text = 'Event')
    tpe.pack(padx =20, pady = 20)
    desc = Label(top, text = 'Description: ' + a['desc'])
    desc.pack(padx =20, pady = 20)
    b = Button(top, text="OK", width=20, command= top.destroy )
    b.pack(side='bottom',padx=5,pady=5)



def userinput():
    global info
    info = {}
    pop = Toplevel()


    pop.title("marker")
    pop.geometry("300x500+200+200")

    #string for title

    frame = Frame(pop)
    entry = Entry(frame)
    entry.pack(side = TOP)
    frame.pack( padx =20, pady =20)



    #radius button for visibility
    frame2 = Frame(pop)
    selection = StringVar()
    radio_1 = Radiobutton(frame2, text = 'Character', variable = selection, value = 'ob')
    radio_2 = Radiobutton(frame2, text = 'Item', variable = selection, value = 'or')
    radio_3 = Radiobutton(frame2, text='Event',  variable = selection, value = 'oy')

    radio_1.select()
    radio_1.pack(side = LEFT)
    radio_2.pack(side = LEFT)
    radio_3.pack(side = LEFT)
    frame2.pack(padx =30, pady =30)
    #radius button for marker type
    frame3 = Frame(pop)
    visible = bool
    check_1 = Checkbutton(frame3, text = 'GM Only', variable = visible, onvalue= True, offvalue= False)

    check_1.pack(side = LEFT)
    frame3.pack(padx =30, pady =30)
    #string for user input
    frame4 = Frame(pop)
    entry4 = Entry(frame4)
    entry4.pack(side = LEFT)
    frame4.pack( padx =20, pady =20)


    def infoPass():

        global info
        info = {'title': entry.get(), 'type': selection.get(), 'vis': visible, 'desc': entry4.get()}
        pop.destroy()


        return info

    #buttons
    label = Label(pop, text="", height=0, width=100)
    label.pack()
    b = Button(pop, text="Cancel", width=20, command= pop.destroy )
    b.pack(side='bottom',padx=5,pady=5)
    b2 = Button(pop, text="Save", width=20, command= infoPass  )
    b2.pack(side='bottom',padx=5,pady=5)

    while info == {}:
        pop.update()

    print info
    return info

#root = Tk()
#a = userinput(root,1,2)
#root.mainloop()


