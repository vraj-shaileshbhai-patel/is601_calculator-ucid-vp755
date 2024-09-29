'''My Calculator Test'''
from calculator import add,subtract,multiply,devide

def test_addition():
    '''add'''
    assert add(2,2) == 4

def test_subtraction():
    '''testing subtraction'''
    assert subtract(5,2) == 3

def test_multiplication():
    '''testing multiplication'''
    assert multiply(2,3) == 6

def test_devide():
    '''testing devision'''
    assert devide(6,3) == 2
