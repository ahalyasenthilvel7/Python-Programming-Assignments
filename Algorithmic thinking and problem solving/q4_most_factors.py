""" Question 4: most_factors """
"""
Inputs: two integers, x and y
Output: integer in [x, y] that has the most number of prime factors
        prints out list of all prime factors (not just unique ones)
        ties are resolved in favor of whichever number has the higher sum of factors
"""
def get_factors(num):
    current_factors = []
    factor = 2
    while factor <= num:
        if num % factor == 0:
            current_factors.append(factor)
            num = num // factor
        else:
            factor += 1
    return current_factors

def most_factors(x, y):
    biggest_factors = []
    biggest_num = 0
    for num in range(x, y+1):
        current_factors = get_factors(num)
        if len(current_factors) > len(biggest_factors):
            biggest_factors = current_factors
            biggest_num = num
        elif len(current_factors) == len(biggest_factors):
            if sum(current_factors) > sum(biggest_factors):
                biggest_factors = current_factors
                biggest_num = num
    return biggest_num
    

""" Test 4 """
def test_most_factors():
    print("Testing most_factors...", end="")
    assert(most_factors(100, 110) == 108) # prints [2, 2, 3, 3, 3]
    assert(most_factors(50, 100) == 96) # prints [2, 2, 2, 2, 2, 3]
    assert(most_factors(20, 24) == 24) # prints [2, 2, 2, 3]
    assert(most_factors(40, 45) == 40) # prints [2, 2, 2, 5]
    assert(most_factors(37, 37) == 37) # prints [37]
    print("... done!")
if __name__ == '__main__':
    test_most_factors()
