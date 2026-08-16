""" Question 8: identify_dog_breed """
"""
Inputs: weight (integer) and coat_length (string)
Output: corresponding dog breed (see Workbook for table)
"""
def identify_dog_breed(weight, coat_length):
    breed = ""
    if (weight<20):
        if coat_length == "short":
            breed = "Swedish Vallhund"
        elif coat_length == "long":
            breed = "Shetland Sheepdog"
        else:
            breed = "Mudi"      
    elif(weight <50) :
        if coat_length == "short":
            breed = "Pembroke Welsh Corgi"
        elif coat_length == "long":
            breed = "Bearded Collie"
        else:
            breed = "Australian Shepherd"
    elif(weight<80):
        if coat_length == "short":
            breed = "Belgian Malinois"
        elif coat_length == "long":
            breed = "Collie"
        else:
            breed = "German shepherd"    
    else:
        if coat_length == "short":
            breed = "Beauceron"
        elif coat_length == "long":
            breed = "Old English Sheepdog"
        else:
            breed = "Bouvier des Flandres"
         
    return breed

""" Test 8 """
def test_identify_dog_breed():
    print("Testing identify_dog_breed...", end="")
    assert(identify_dog_breed(25, "short") == "Pembroke Welsh Corgi")
    assert(identify_dog_breed(95, "long") == "Old English Sheepdog")
    assert(identify_dog_breed(19, "medium") == "Mudi")
    assert(identify_dog_breed(50, "long") == "Collie")
    print("... done!")

if __name__ == '__main__':
    test_identify_dog_breed()