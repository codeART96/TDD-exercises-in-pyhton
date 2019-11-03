import sys
sys.path.append('../src')

import string_calculator

def test_add():
    assert string_calculator.add("") == 0
    

    assert string_calculator.add("1") == 1
    assert string_calculator.add("2") == 2
   
    assert string_calculator.add("1,2") == 3
    assert string_calculator.add("2,3") == 5
   
   
    assert string_calculator.add("1,2,3,4") == 10
    assert string_calculator.add("1,4,5,6") == 16
    
    assert string_calculator.add("1\n2") == 3
    assert string_calculator.add("3\n4") == 7
    
    assert string_calculator.add("//:\n1:2:3") == 6
    assert string_calculator.add("3\n4") == 6
    
    
    assert string_calculator.add("//---\n1---2---3") == 6
    assert string_calculator.add("//-!:o-\n1-1;o-2-!;o-3") == 6
    assert string_calculator.add("//-!o-\n15-!o-12-!o-3") == 30    