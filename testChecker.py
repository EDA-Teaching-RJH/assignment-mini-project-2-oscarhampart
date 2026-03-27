from cardChecker import isValidCard #Import custom library

def testCardChecker(): #Testing the custom library
    assert isValidCard("SJ") == True #Testing inputs, jack
    assert isValidCard("H10") == True #Testing inputs, number 10
    assert isValidCard("ck") == True #Testing inputs, if .upper is working

    assert isValidCard("diamondK") == False #Testing inputs, these will not work 
    assert isValidCard("aliseuhbgijbsv4578691") == False

    print("Testing complete.")

if __name__ == "__main__": #Test starts when main is run
    testCardChecker()

