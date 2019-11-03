import sys
sys.path.append('../src')

import simple_calculator

def test_add():
    assert simple_calculator.add(0, 0) == 0
    assert simple_calculator.add(-1, -1) == -2
    assert simple_calculator.add(4, 5) == 9 
    assert simple_calculator.add(1, 2, 3) == 6

def test_multiply():
    assert simple_calculator.multiply(0, 0) == 0
    assert simple_calculator.multiply(1, 2) == 2
    assert simple_calculator.multiply(4, 5) == 20 
    assert simple_calculator.multiply(1, 2, 3) == 6
