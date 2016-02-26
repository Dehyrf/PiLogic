#!/usr/bin/python
# -*- coding: utf-8 -*-
# import libraries

"""********************"""

from sympy import *
import time
import RPi.GPIO as GPIO
from Tkinter import *
from tkMessageBox import askokcancel

# dedicate logic symbols to input pins for switches and an output pin

pinA = 7  # GPIO4
pinB = 11  # GPIO17
pinC = 13  # GPIO21
pinD = 15  # GPIO22
pinOUT = 12  # GPIO18

GPIO.setup(pinA, GPIO.IN)
GPIO.setup(pinB, GPIO.IN)
GPIO.setup(pinC, GPIO.IN)
GPIO.setup(pinD, GPIO.IN)
GPIO.setup(pinOUT, GPIO.OUT)


# methods
# simplify logic sentence to conjunctive normal form

def simp(r):
    return to_cnf(r, True)


# and gate

def And(a, b):
    return a and b


# or gate

def Or(a, b):
    return a or b


# not gate

def Not(a):
    return not a


# main

class Quitter(Frame):

    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack()
        widget = Button(self, text='Quit', command=self.quit)
        widget.pack(expand=YES, fill=BOTH, side=LEFT)

    def quit(self):
        ans = askokcancel('Verify exit', 'Really quit?')
        if ans:
            Frame.quit(self)


def run():

      # raw = raw_input('Please enter a logic statement with A, B, C, D, &, |, ~, (): ')

    raw = ent.get()
    chars = set('ABCD&|~() ,')
    if any(c in chars for c in raw):
        legal = True
    else:
        print 'Illegal characters!'
        legal = False
        exit()
    logic = simp(raw)
    print 'Your logic statement %s has been simplified to %s' % (raw,
            logic)
    while legal:
        A = bool(GPIO.input(pinA))
        B = bool(GPIO.input(pinB))
        C = bool(GPIO.input(pinC))
        D = bool(GPIO.input(pinD))
        isTrue = eval(logic)
        if isTrue:
            GPIO.output(pinOUT, GPIO.HIGH)
        else:
            GPIO.output(pinOUT, GPIO.LOW)


def main():

    # Take in logic statement from user

    root = Tk()
    ent = Entry(root)
    ent.insert(0, 'A & (B | C)')
    ent.pack(side=TOP, fill=X)
    ent.focus()
    ent.bind('<Return>', lambda event: run())
    btn = Button(root, text='Compile', command=run)
    btn.pack(side=LEFT)
    Quitter(root).pack(side=RIGHT)
    root.mainloop()


# execute

if __name__ == '__main__':
    main()
