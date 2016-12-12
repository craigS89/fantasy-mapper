# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.



import cPickle as pickle
import tkFileDialog
class markers:
    def __init__(self):
        pass
__author__ = "k1221169"
__date__ = "$15-Dec-2015 11:56:49$"

stri ='file.png'
stri.lstrip('.png')
print
def saveall(a,b):
        c = a.replace('.png', '.pickle')
        file = c
        print file

        with open(file, 'wb') as handle:
            pickle.dump(b,handle)


def loadall(a):
    a.replace('.png', '.pickle')
    file = a
    with open(file, 'rb') as handle:
        c = pickle.load(handle)
    return c

#loadall()
