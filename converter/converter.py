"""********************"""
# import libraries
"""********************"""
from sympy import * 
import time  
import RPi.GPIO as GPIO


"""********************"""
# dedicate logic symbols to input pins for switches and an output pin
"""********************"""
pinA = 7	#GPIO4
pinB = 11	#GPIO17
pinC = 13	#GPIO21
pinD = 15	#GPIO22
pinOUT = 12	#GPIO18

GPIO.setup(pinA,GPIO.IN)
GPIO.setup(pinB,GPIO.IN)
GPIO.setup(pinC,GPIO.IN)
GPIO.setup(pinD,GPIO.IN)
GPIO.setup(pinOUT,GPIO.OUT)

"""********************"""
# methods
"""********************"""
# simplify logic sentence to conjunctive normal form
def simp(r):
	return to_cnf(r, True)

# and gate
def And(a,b):
    if a == True :
        if b == True :
            return True
    else : 
        return False

# or gate
def Or(a,b):
    if a == True:
        return True
    elif b == True:
        return True
    else :
        return False

# not gate
def Not(a):
    if a == False:
        return True
    else:
        return False


"""********************"""
# main
"""********************"""
def main():
	#Take in logic statement from user
	raw = raw_input('Please enter a logic statement with A, B, C, D, &, |, ~, (): ')
	print "Your logic statement %s has been simplified to %s" % (raw, simp(raw))
	while True:
		A = bool(GPIO.input(pinA))	
		B = bool(GPIO.input(pinB))
		C = bool(GPIO.input(pinC))
		D = bool(GPIO.input(pinD))
		exec 'isTrue = ' + simp(raw)
		while isTrue:
			GPIO.output(pinOUT,GPIO.HIGH)
		GPIO.output(pinOUT,GPIO.LOW)


"""********************"""
# execute 
"""********************"""
if __name__ == "__main__":
	main()
