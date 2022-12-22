

from microbit import *
min =255
max = 0
while True:
    adc = pin0.read_analog()
    volt = (3.3/1023)*adc
    degC = 1000*volt/20
    
    #print((round(degC, 1),))
    if round(degC) < min:
       min = round(degC,1)
    if round(degC) > max:
       max = round(degC)
   # if button_a.was_pressed():
   #     display.scroll(max)
   # if button_b.was_pressed():
   #     display.scroll(min)
    display.scroll(round(degC,1), delay = 100)
    display.scroll(min, delay = 200)
    
    print(round(degC, 1) ,'C')
    
    #print((degC))
    sleep(3000)
    