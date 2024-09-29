'''My Calculator Test'''
from calculator import Calculator

def test_addition():
    '''testing add'''
    assert Calculator.add(2,2) == 4

def test_subtraction():
    '''testing subtraction'''
    assert Calculator.subtract(5,2) == 3

def test_multiplication():
    '''testing multiplication'''
    assert Calculator.multiply(2,3) == 6

def test_devide():
    '''testing devision'''
    assert Calculator.devide(6,3) == 2
