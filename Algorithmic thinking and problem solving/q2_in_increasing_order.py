""" Question 2: in_increasing_order """
"""
Input: list of strings
Output: True if strings are in order of increasing length, False otherwise
"""
def in_increasing_order(words):
    for i in range(1, len(words)):
        if len(words[i]) < len(words[i-1]):
            return False
    return True
def test_in_increasing_order():
    print("Testing in_increasing_order...", end="")
    assert(in_increasing_order([ "a", "to", "be", "what", "ready", "said", "welcome" ]) == False)
    assert(in_increasing_order([ "a", "to", "be", "what", "said", "ready", "welcome" ]) == True)
    assert(in_increasing_order([ "night", "last" ]) == False)
    assert(in_increasing_order([ "one", "six", "two" ]) == True)
    assert(in_increasing_order([ ]) == True)
    print("... done!")

if __name__ == '__main__':
    test_in_increasing_order()