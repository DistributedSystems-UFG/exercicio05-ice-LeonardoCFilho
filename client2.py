import sys, Ice
import Demo
from const import *

communicator = Ice.initialize(sys.argv)

base1 = communicator.stringToProxy(f"SimplePrinter1:tcp -h 98.90.53.6 -p {DOOR}")
base2 = communicator.stringToProxy(f"SimplePrinter2:tcp -h 98.90.53.6 -p {DOOR}")
printer1 = Demo.PrinterPrx.checkedCast(base1)
printer2 = Demo.PrinterPrx.checkedCast(base2)
if (not printer1) or (not printer2):
    raise RuntimeError("Invalid proxy")

printer1.printString("Hello World from printer1!")
printer2.printString("Hello World from printer2!")

communicator.waitForShutdown()
