#import validate function and pytest module
from numb3rs import validate
import pytest

#main function calls test_functions
def main():
    test_format()
    test_range()

#test format validation
def test_format():
    assert validate(r"1.2.3.4") == True
    assert validate(r"1.2.3") == False
    assert validate(r"1.2") == False
    assert validate(r"1") == False

#test range of numbers in ip
def test_range():
    assert validate(r"255.255.255.255") == True
    assert validate(r"1000.255.255.255") == False
    assert validate(r"255.1000.255.255") == False
    assert validate(r"255.255.1000.255") == False
    assert validate(r"255.255.255.1000") == False
    


if __name__ == "__main__":
    main()