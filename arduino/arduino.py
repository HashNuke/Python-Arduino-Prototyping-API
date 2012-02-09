#!/usr/bin/env python

import serial, time

class Arduino(object):

    __OUTPUT_PINS = -1

    def __init__(self, port, baudrate=115200):
        self.serial = serial.Serial(port, baudrate)

    def __str__(self):
        return "Arduino is on port %s at %d baudrate" %(self.serial.port, self.serial.baudrate)

    def output(self, pinArray):
        self.__sendData(len(pinArray))

        if(isinstance(pinArray, list) or isinstance(pinArray, tuple)):
            self.__OUTPUT_PINS = pinArray
            for each_pin in pinArray:
                self.__sendPin(each_pin)
        return True

    def setLow(self, pin):
        self.__sendData('0')
        self.__sendPin(pin)
        return True

    def setHigh(self, pin):
        self.__sendData('1')
        self.__sendPin(pin)
        return True

    def getState(self, pin):
        self.__sendData('2')
        self.__sendPin(pin)
        return self.__formatPinState(self.__getData())

    def analogWrite(self, pin, value):
        self.__sendData('3')
        self.__sendPin(pin)
        hex_value = hex(value)[2:]
        if(len(hex_value)==1):
            hex1 = '0'
            hex2 = hex_value[0]
        else:
            hex1 = hex_value[0]
            hex2 = hex_value[1]
        
        self.__sendData(hex1)
        self.__sendData(hex2)
        return True

    def analogRead(self, pin):
        self.__sendData('4')
        self.__sendPin(pin)
        return self.__getData()

    def turnOff(self):
        for each_pin in self.__OUTPUT_PINS:
            self.setLow(each_pin)
        return True

    def __sendPin(self, pin):
        pin_in_char = chr(pin+48)
        self.__sendData(pin_in_char)

    def __sendData(self, serial_data):
        while(self.__getData()!="what"):
            pass
        self.serial.write(str(serial_data))

    def __getData(self):
        return self.serial.readline().replace("\r\n","")

    def __formatPinState(self, pinValue):
        if pinValue=='1':
            return True
        else:
            return False

    def close(self):
        self.serial.close()
        return True

    """
    def __del__(self):
        #close serial connection once program ends
        #this fixes the problem of port getting locked or unrecoverable in some linux systems
        self.serial.close()
    """
