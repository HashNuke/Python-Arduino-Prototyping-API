# Python Arduino Prototyping API (version: 0.5)

> &copy; 2009-2010 Akash Manohar J <akash@akash.im>
> under the MIT License

The Python Arduino Prototyping API helps you to quickly prototype Arduino programs, 
without having to repeatedly load the program to the Arduino board.

#### Setup:

1. Load prototype.pde onto your Arduino dev board.
2. Import the arduino lib in your python script.


## Methods

*Arduino.output(list_of_output_pins)* - set the output pins

**Digital I/O**

1. *Arduino.setHigh(pin_number)*
2. *Arduino.setLow(pin_number)*
3. *Arduino.getState(pin_number)*
4. *Arduino.getState()* - returns true if pin state is high, else it returns false.

**Analog I/O**

1. *Arduino.analogRead(pin_number)* - returns the analog value
2. *Arduino.analogRead(pin_number, value)* - sets the analog value

**Misc**

1.) *Arduino.turnOff()* - sets all the pins to low state

2.) *Arduino.close()* - closes serial connection. Using this makes sure that you won't have to disconnect & reconnect the Arduino again to recover the serial port.

## Usage example

        #the blink program

        #import the lib
        from arduino import Arduino

        import time

        #specify the port as an argument
        my_board = Arduino('/dev/ttyUSB1')

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
