# Practice Question #1 - Apple Stock
from sys import maxint
from random import randint

def main():
    '''
    Identifies the most profit to be made from a single purchase and 
    sale of a stock in a single day, in a single pass and using 
    constant space. 
    '''

    # sampleVals = [299, 300, 305, 306, 303, 300, 310, 280, 290, 295]
    sampleVals = [10, 9, 8, 7, 6, 4]

    currentMaxProfit = -maxint
    currentMin = None

    # should check for minimum length of the array

    # consider using the enumerate function to iterate through

    for val in sampleVals:
        if currentMin:
            if val-currentMin > currentMaxProfit:
                currentMaxProfit = val-currentMin
        if not currentMin or val<currentMin:
            currentMin = val

    return currentMaxProfit

if __name__ == "__main__":
    largestSingleProfit = main()
    print("Largest single profit was %i dollars" % (largestSingleProfit))