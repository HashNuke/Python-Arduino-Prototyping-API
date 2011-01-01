#import the lib
from arduino import Arduino

import time

#specify the port as an argument
my_board = Arduino('/dev/ttyUSB0')

#declare output pins as a list/tuple
my_board.output([11,12,13])

#perform operations
i=0
while(i<10):
    my_board.setHigh(13)
    time.sleep(1)
    my_board.setLow(13)
    time.sleep(1)
    i+=1
