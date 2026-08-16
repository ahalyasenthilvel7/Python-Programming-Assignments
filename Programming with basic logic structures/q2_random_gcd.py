""" Question 2: random_gcd() """
"""
Inputs: None
Output: randomly generates two integers in range [1, 100] and returns gcd
"""
import math
from random import randint
def random_gcd():
    x = randint(1,100)
    y = randint(1,100)
    result = math.gcd(x,y)
    print("x"+"y"+":" ,str(x),str(y))
    return result

""" Test 2 """
def test_random_gcd():
    print("Testing random_gcd...")
    # Check whether the result is actually the GCD of the two printed numbers
    result = random_gcd() # should print x and y
    print("gcd:", result) # prints the result
    print("... done!")

if __name__ == '__main__':
    test_random_gcd()