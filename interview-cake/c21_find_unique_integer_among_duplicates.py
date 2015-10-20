def getUniqueID(inArray):
    '''
    Given an int array that contains many duplicates and a single 
    unique ID, find it and return it.
    '''
    
    pairDictionary = {}

    for quadID in inArray:
        # print(quadID)
        # print(pairDictionary)
        if quadID in pairDictionary:
            del pairDictionary[quadID]
        else:
            pairDictionary[quadID] = 1

    return pairDictionary.keys()

def getUniqueIDSpaceOptimized(inArray):
    a = 0

    for quadID in inArray:
        a = a ^ quadID

    return a

def main():
    # should return 9 as the unique integer
    testArray = [1,2,5,3,2,5,3,1,9,3,4,3,4]

    print("Unique ID was: %s"%(getUniqueID(testArray)))
    print("With space optimized solution, unique ID was: %s"%(getUniqueIDSpaceOptimized(testArray)))


if __name__ == "__main__":
    main()