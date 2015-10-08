def main():
    sampleInput = [1, 7, 3, 4]

    print("Input: %s produced Output: %s" %(sampleInput, get_product_array_v3(sampleInput)))

def get_product_array_bonus(inputList):
    # allowe to use division this time

    pass

def get_product_array_v3(inputList):
    ''' 
    Returns a list of the products of all elements of the input 
    list, except the one at the index itself.
    
    Example
      input [1, 7, 3, 4]
      output [7*3*4, 1*3*4, 1*7*4, 1*7*3]

    Requires two iterations through the input list and only
    allocates space for the output array, which is an 
    improvement both in time and space over the first solution.
    '''

    outputList = [1] * len(inputList)
    
    # get all of the products before the index
    prod = 1
    for i in range(len(inputList)-1):
        prod *= inputList[i]
        outputList[i+1] = prod

    # get all of the products after the index
    prod = 1
    for i in range(len(inputList)-1, -1, -1):
        outputList[i] *= prod
        prod *= inputList[i]

    return outputList

def get_product_array_v2(inputList):

    prevProds = [1]
    prod = 1
    for i in range(len(inputList)-1):
        prod *= inputList[i]
        prevProds.append(prod)

    afterProds = [1]
    prod = 1

    # *** iterate through a list backwards
    for i in range(len(inputList)-1, 0,  -1):
        prod *= inputList[i]
        afterProds.append(prod)
    afterProds.reverse() 

    print(prevProds)
    print(afterProds)

    # *** iterate through two lists simultaneously
    outputList = [a*b for a,b in zip(prevProds, afterProds)]

    return outputList

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