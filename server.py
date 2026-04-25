import sys, Ice
import Demo
from const import *

class PrinterI(Demo.Printer):
    def printString(self, s, current=None):
        print(s)
        return s

    def printUpperCase(self, s, current=None): # Novo
        print(s.upper())
        return s.upper()

class CalculatorI(Demo.Calculator):
    def soma(self, a, b, current=None):
        return a + b
    def subtrair(self, a, b, current=None):
        return a - b
    def multiplicar(self, a, b, current=None):
        return a * b

communicator = Ice.initialize(sys.argv) 

adapter = communicator.createObjectAdapterWithEndpoints("SimpleAdapter", f"default -p {DOOR}")
object = PrinterI()
adapter.add(object, communicator.stringToIdentity("SimplePrinter"))
calculator = CalculatorI()
adapter.add(calculator, communicator.stringToIdentity("SimpleCalculator"))

adapter.activate()

communicator.waitForShutdown()