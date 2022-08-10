from time import sleep
import time
import ntptime
import utime
import machine
import umail

drill1 = machine.Pin(2, machine.Pin.IN, machine.Pin.PULL_UP)
drill2 = machine.Pin(13, machine.Pin.IN, machine.Pin.PULL_UP)
drill3 = machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_UP)
drill4 = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_UP)
drill5 = machine.Pin(5, machine.Pin.IN, machine.Pin.PULL_UP)
drill6 = machine.Pin(4, machine.Pin.IN, machine.Pin.PULL_UP)

while True:
    #Get current time from internet
    try:
      ntptime.settime()
    except:
      print('error setting time')
    #Unpack time into variables
   
    year, month, day, hour, minute, second, ms, dayinyear = utime.localtime()

    print(drill1.value()) #for testing, can be removed for production
    print(drill2.value())  # for testing, can be removed for production
    print(drill3.value())  # for testing, can be removed for production
    print(drill4.value())  # for testing, can be removed for production
    print(drill5.value())  # for testing, can be removed for production
    print(drill6.value())  # for testing, can be removed for production

    if drill1.value() == 1:
        drill1state = "Present"
    else:
        drill1state = "Removed"

    if drill2.value() == 1:
        drill2state = "Present"
    else:
        drill2state = "Removed"

    if drill3.value() == 1:
        drill3state = "Present"
    else:
        drill3state = "Removed"

    if drill4.value() == 1:
        drill4state = "Present"
    else:
        drill4state = "Removed"


    if drill5.value() == 1:
        drill5state = "Present"
    else:
        drill5state = "Removed"

    if drill6.value() == 1:
        drill6state = "Present"
    else:
        drill6state = "Removed"

    #Send morning email
    if hour == 13 and minute == 30:
        smtp = umail.SMTP('1.2.3.4', 25, username='Someusername@domain.com')
        smtp.to('user@domain.com')
        smtp.send("Drill 1 state: {} \nDrill 2 State: {} \nDrill 3 State: {} \nDrill 4 State: {} \nDrill 5 State: {} \nDrill 6 State: {}".format(drill1state, drill2state, drill3state, drill4state, drill5state, drill6state))
        smtp.quit()

    #Send evening email
    if hour == 1 and minute == 30:
        smtp = umail.SMTP('1.2.3.4', 25, username='Someuser@domain.com')
        smtp.to('SomeUser@domain.com')
        smtp.send("Drill 1 state: {} \nDrill 2 State: {} \nDrill 3 State: {} \nDrill 4 State: {} \nDrill 5 State: {} \nDrill 6 State: {}".format(drill1state, drill2state, drill3state, drill4state, drill5state, drill6state))
        smtp.quit()

    time.sleep(50)
