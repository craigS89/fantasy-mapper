# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.


import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import popup1 as ap
import markers as mk
import tkFileDialog
import time
__author__ = "k1221169"
__date__ = "$15-Nov-2015 11:29:21$"

#b = mk.loadall()
markerList = []
xplots = []
yplots = []
desc = ''
title = ''
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(np.random.rand(10))
a = ap.ask()
img_path = ''
if a == True:
    img_path = tkFileDialog.askopenfile(mode='rb',title='Choose a file')
    #mk.loadall(img_path)
if a == False:
    img_path = 'original.png'

img = mpimg.imread(img_path)
imgplot = plt.imshow(img)
plt.ylim(ymax=1)
plt.xlim(xmin=1)


def mrkApnd(a, b):


    a.update(b)
    print a
    markerList.append(a)


def onclick(event):

    if spacecheck(event.xdata, event.ydata):
        idx = np.abs(xplots - event.xdata).argmin()
        idy = np.abs(yplots - event.ydata).argmin()
        print xplots[idx]

        for i in markerList:
            if xplots[idx] == i['x'] and yplots[idy] == i['y']:
                print i
                ap.useroutput(i)
    else:
        input1 = ap.userinput()
        input2 = {'x':event.xdata, 'y':event.ydata}
        mrkApnd(input2, input1)
        drawMarks()
        print input1

    return markerList
cid = fig.canvas.mpl_connect('button_press_event', onclick)
def onkey(event):
    print event.key
    if event.key == 'a':
        mk.saveall(img_path,markerList)


sid = fig.canvas.mpl_connect('key_press_event', onkey)
def drawMarks():
    plt.ion()
    for i in markerList:
        xplots.append(i['x'])
        yplots.append(i['y'])
        plt.plot(i['x'], i['y'], i['type'])
    plt.ioff()




def spacecheck(x,y):
    a = bool
    if np.isclose(xplots, x, atol=50.0).any() and np.isclose(yplots, y, atol=50.00).any():
        a=True
        print 'yes'
        return a

def addinfo(a):
    markerList.append(a)
plt.draw()
plt.show()




