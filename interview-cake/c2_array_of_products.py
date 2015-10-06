def main():
    sampleInput = [1, 7, 3, 4, 0]

    print("Input: %s produced Output: %s" %(sampleInput, get_product_array(sampleInput)))

# this works in O(n) space but O(n^2) time
def get_product_array(inputList):
    '''
    Given a list, this function returns a list of the products
    of the elements of the input list except at the index itself.

    Caveat: no division allowed.

    Example
      input [1, 7, 3, 4]
      output [7*3*4, 1*3*4, 1*7*4, 1*7*3]
    '''

    indexList = [x for x in range(len(inputList))]
    outputList = [1 for x in range(len(inputList))]

    for i in range(len(outputList)):
        for j in range(len(inputList)):
            if j != indexList[i]:
                outputList[i] *= inputList[j]

    return outputList

if __name__ == "__main__":
    main()