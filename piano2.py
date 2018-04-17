from time import sleep
from array import *
import RPi.GPIO as GPIO

#Set variables
do1=31
re=32
mi=33
sol=35
la=36
si=37
do2=38
relai_1=11 #Relai lie a la porte
relai_2=13 #relai utilise seulement pour indicationdu sonor du demarrage du script
SleepTime=.3
SleepRelai=2

#set GPIO sumbering and define input/outupt pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(do1,GPIO.IN)
GPIO.setup(re,GPIO.IN)
GPIO.setup(mi,GPIO.IN)
GPIO.setup(sol,GPIO.IN)
GPIO.setup(la,GPIO.IN)
GPIO.setup(si,GPIO.IN)
GPIO.setup(do2,GPIO.IN)
GPIO.setup(relai_1,GPIO.OUT)
GPIO.output(relai_1,GPIO.HIGH)
GPIO.setup(relai_2,GPIO.OUT)
GPIO.output(relai_2,GPIO.HIGH)

#Signal du demarrage utilisant le relai 2
for x in range(0,3):
    GPIO.output(relai_2,GPIO.LOW)
    sleep(.5)
    GPIO.output(relai_2,GPIO.HIGH)
    sleep(.5)

#initialisation de la variable de type tableau(array) opur la solution
a_solution = array('i',[do1,mi,re,sol,do2,la,si])

#initialisation de l'indice du tableau. L'indice du tableau commence a 0. 
i_min=0
i_max=6
i=i_min

try:
    while True:
        if GPIO.input(do1)==1:
            print "do1=close"
            sleep(SleepTime)
            if a_solution[i]==do1:
                if i==i_max:
                    print "Reussi!!!"
                    print i
                    #ALLUMER LE RELAI
                    GPIO.output(relai_1,GPIO.LOW)
                    sleep(SleepRelai)
                    #ETEINDRE LE RELAI
                    GPIO.output(relai_1,GPIO.HIGH)
                    i=i_min
                else:
                    i=i+1
                    print "Bon!!! Continue"
                    print i
            else:
                i=i_min
                print "Pas bon! Reset compteur"
                print i
        
        if GPIO.input(re)==1:
            print "re=close"
            sleep(SleepTime)
            if a_solution[i]==re:
                if i==i_max:
                    print "Reussi!!!"
                    print i
                    #ALLUMER LE RELAI
                    GPIO.output(relai_1,GPIO.LOW)
                    sleep(SleepRelai)
                    #ETEINDRE LE RELAI
                    GPIO.output(relai_1,GPIO.HIGH)
                    i=i_min
                else:
                    i=i+1
                    print "Bon!!! Continue"
                    print i
            else:
                i=i_min
                print "Pas bon! Reset compteur"
                print i

        if GPIO.input(mi)==1:
            print "mi=close"
            sleep(SleepTime)
            if a_solution[i]==mi:
                if i==i_max:
                    print "Reussi!!!"
                    print i
                    #ALLUMER LE RELAI
                    GPIO.output(relai_1,GPIO.LOW)
                    sleep(SleepRelai)
                    #ETEINDRE LE RELAI
                    GPIO.output(relai_1,GPIO.HIGH)
                    i=i_min
                else:
                    i=i+1
                    print "Bon!!! Continue"
                    print i
            else:
                i=i_min
                print "Pas bon! Reset compteur"
                print i

        if GPIO.input(sol)==1:
            print "sol=close"
            sleep(SleepTime)
            if a_solution[i]==sol:
                if i==i_max:
                    print "Reussi!!!"
                    print i
                    #ALLUMER LE RELAI
                    GPIO.output(relai_1,GPIO.LOW)
                    sleep(SleepRelai)
                    #ETEINDRE LE RELAI
                    GPIO.output(relai_1,GPIO.HIGH)
                    i=i_min
                else:
                    i=i+1
                    print "Bon!!! Continue"
                    print i
            else:
                i=i_min
                print "Pas bon! Reset compteur"
                print i

        if GPIO.input(la)==1:
            print "la=close"
            sleep(SleepTime)
            if a_solution[i]==la:
                if i==i_max:
                    print "Reussi!!!"
                    print i
                    #ALLUMER LE RELAI
                    GPIO.output(relai_1,GPIO.LOW)
                    sleep(SleepRelai)
                    #ETEINDRE LE RELAI
                    GPIO.output(relai_1,GPIO.HIGH)
                    i=i_min
                else:
                    i=i+1
                    print "Bon!!! Continue"
                    print i
            else:
                i=i_min
                print "Pas bon! Reset compteur"
                print i

        if GPIO.input(si)==1:
            print "si=close"
            sleep(SleepTime)
            if a_solution[i]==si:
                if i==i_max:
                    print "Reussi!!!"
                    print i
                    #ALLUMER LE RELAI
                    GPIO.output(relai_1,GPIO.LOW)
                    sleep(SleepRelai)
                    #ETEINDRE LE RELAI
                    GPIO.output(relai_1,GPIO.HIGH)
                    i=i_min
                else:
                    i=i+1
                    print "Bon!!! Continue"
                    print i
            else:
                i=i_min
                print "Pas bon! Reset compteur"
                print i

        if GPIO.input(do2)==1:
            print "do2=close"
            sleep(SleepTime)
            if a_solution[i]==do2:
                if i==i_max:
                    print "Reussi!!!"
                    print i
                    #ALLUMER LE RELAI
                    GPIO.output(relai_1,GPIO.LOW)
                    sleep(SleepRelai)
                    #ETEINDRE LE RELAI
                    GPIO.output(relai_1,GPIO.HIGH)
                    i=i_min
                else:
                    i=i+1
                    print "Bon!!! Continue"
                    print i
            else:
                i=i_min
                print "Pas bon! Reset compteur"
                print i



except IndexError:
    print "Error exception"

finally:
    #cleanup the GPIO pins before ending
    GPIO.cleanup()
