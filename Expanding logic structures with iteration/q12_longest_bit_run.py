""" Question 12: longest_bit_run """
"""
Input: string s of 0s and 1s
Output: the length of the longest run of 0s or 1s
"""


def longest_bit_run(s):
    zeros = 0
    ones = 0
    longest = 0
    for i in s:
        if i=='0':
            zeros+=1
            ones = 0
            if zeros>longest:
               longest = zeros
        elif i=='1':
            ones+=1
            zeros = 0
            if ones>longest:
                longest = ones
          
    return longest         

""" Test 12 """
def test_longest_bit_run():
    print("Testing longest_bit_run...", end='')
    assert(longest_bit_run('0') == 1)
    assert(longest_bit_run('011') == 2)
    assert(longest_bit_run('0000') == 4)
    assert(longest_bit_run('01') == 1)
    assert(longest_bit_run('00111100') == 4)
    print("... done!")


if __name__ == '__main__':
    test_longest_bit_run()