def get_highest_product(inList):
    '''
    Returns the highest product of three integers in the input list. 

    Assumes that there are at least three elements in the list.
    '''
    maxVals = [0] * 3
    minVals = [0] * 3

    # this could be improved by using actual queues, not sure about the efficiency of Python lists 
    for val in inList:
        if val > maxVals[0]:
            maxVals.insert(0, val)
            maxVals.pop()
        if val < minVals[0]:
            minVals.insert(0 ,val)
            minVals.pop()

    return max( (minVals[0] * minVals[0] * maxVals [0]), (maxVals[0] * maxVals[1] * maxVals[2]) )    


def main():
    inList = [-10, -10, 1, 3, 2]
    print("Highest product from %s is %s" % (inList, get_highest_product(inList)))

    '''
    How would you extend to the product of 4 elements? Of k elements?

    4 is trivial, just keep track of the largest and smallest 4 elements, max is one of three options:
        1 - product of largest 4 
        2 - product of smallest 4
        3 - product of largest 2 and smallest 2

    Extending to k items, just keep track of the k largest and smallest elements. When it comes time to 
    compute the product use a deque to remove items from the largest and smallest deques in pairs, comparing
    which of the two is larger. Do this for the even numbers, then multiply by the remaining highest number.

    If the highest product is really large, how could you protect against this?

    Using a long int (larger integer type), and manually checking against the largest possible sized integer,
    which is sys.maxint in Python (although apparently Python will throw an error if there's overflow)
    '''

if __name__ == "__main__":
    main()