""" Question 4: duplicated_ids """
"""
Input: list of dictionaries
Output: list of duplicated id keys in given dictionaries
        must run in linear time
"""
def duplicated_ids(L):
    seen = set()
    duplicates = set()
    for student in L:
        student_id = student["id"]
        if student_id in seen:
            duplicates.add(student_id)
        else:
            seen.add(student_id)
    return list(duplicates)


""" Test 4 """
def test_duplicated_ids():
    print("Testing duplicated_ids...", end='')
    L = [ {"id": 1, "major": "computer science", "gpa": 4},
          {"id": 2, "major": "mathematics", "gpa": 3.5},
          {"id": 3, "major": "chemical engineering", "gpa": 3.7} ]
    assert(duplicated_ids(L) == [])
    L1 = [ {"id": 5, "major": "statistics", "gpa": 3.3},
           {"id": 5, "major": "economics", "gpa": 4.0},
           {"id": 5, "major": "mechanical engineering", "gpa": 3.1},
           {"id": 2, "major": "drama", "gpa": 3.5},
           {"id": 2, "major": "art", "gpa": 2.7} ]
    assert(duplicated_ids(L1) == [5, 2] or duplicated_ids(L1) == [2, 5])
    
    # if your code is failing this case, check the efficiency!
    d = {"id": 0, "major": "business", "gpa": 3.0}
    L2 = [d]*30000
    assert(duplicated_ids(L2) == [0])
    print("... done!")

if __name__ == '__main__':
    test_duplicated_ids()