import sys, Ice
import Demo
from const import *
 
communicator = Ice.initialize(sys.argv)

base = communicator.stringToProxy(f"SimplePrinter:default -p {DOOR}")
printer = Demo.PrinterPrx.checkedCast(base)
if not printer:
    raise RuntimeError("Invalid proxy")

# Função original
printer.printString("Hello World!")

# Nova função
printer.printUpperCase("tudo em maiúsculo")

# Conectar ao novo objeto
base_calc = communicator.stringToProxy(f"SimpleCalculator:default -p {DOOR}")
calculator = Demo.CalculatorPrx.checkedCast(base_calc)

if not calculator:
    raise RuntimeError("Invalid proxy")

x = 25
y = -14
soma = calculator.soma(x, y)
print(f"Soma: {soma}")
subtracao = calculator.subtrair(x, y)
print(f"Subtração: {subtracao}")
multiplicacao = calculator.multiplicar(x, y)
print(f"Multiplicação: {multiplicacao}")
