from calculator.calculation import Calculation
from calculator.operations import add,subtract,multiply,devide

class Calculator:
    @staticmethod
    def add(a,b):
        calculation = Calculation(a,b,add)
        return calculation.get_result()
    @staticmethod
    def subtract(a,b):
        calculation = Calculation(a,b,subtract)
        return calculation.get_result()
    @staticmethod
    def multiply(a,b):
        calculation = Calculation(a,b,multiply)
        return calculation.get_result()
    @staticmethod
    def devide(a,b):
        calculation = Calculation(a,b,devide)
        return calculation.get_result()
