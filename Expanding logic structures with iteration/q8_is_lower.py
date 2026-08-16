""" Question 8: is_lower """
"""
Input: string s
Output: True if s contains at least one character and every char is lowercase
        False otherwise
"""
def is_lower(s):
    if len(s)==0:
        return False
    for i in s:
        if ('A'<=i<='Z'):
            return False
        elif ('a'<=i<='z'):
            return True

    return False

""" Test 8 """
def test_is_lower():
    print("Testing is_lower...", end='')
    assert(is_lower("") == False)
    assert(is_lower("a") == True)
    assert(is_lower("123a") == True)
    assert(is_lower("Hello") == False)
    assert(is_lower("hello!") == True)
    print("... done!")

if __name__ == '__main__':
    test_is_lower()