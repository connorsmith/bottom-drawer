'''
Array of n integers in sorted order. How quickly could we check if an integer was 
in the set?

Binary searching is the answer - log(n) time
'''

# recursive implementation
def binarySearch(inputList, val):
    # assumes that the input list is sorted

    # checking the stopping conditions
    if inputList == []:
        return False

    listLength = len(inputList)

    middleIndex = int(len(inputList)/2.0)

    if inputList[middleIndex] == val:
        return True

    if inputList[middleIndex] < val:
        return binarySearch(inputList[middleIndex+1:], val)
    else:
        return binarySearch(inputList[:middleIndex], val)

def main():
    testArray = [1,3,4,5,8,10,11]

    searchValueList = [1,2,3,12]

    for val in searchValueList:
        print("%s in array %s: %s"%(val, testArray, binarySearch(testArray, val)))

if __name__ == "__main__":
    main()