def findCombos(amountLeft, denominations):
    '''
    This is the top down approach, and it makes several repeated
    function calls, wasting time.
    '''
    if amountLeft == 0:
        return 1

    # no denominations remaining, or overspent
    if amountLeft < 0 or denominations == []:
        return 0

    print("In findCombos: a(%s), d(%s)"%(amountLeft, denominations))

    currentDenom, otherDenoms = denominations[0], denominations[1:]

    numberOfCombinations = 0
    while amountLeft >= 0:
        combosReturned = findCombos(amountLeft, otherDenoms)
        numberOfCombinations += combosReturned
        amountLeft -= currentDenom
    return numberOfCombinations

def findCombosBottomUp(amount, denominations):
    '''
    Avoids the call stack memory issues associated with using 
    large denominations or high input values.
    '''
    combinations = [0] * (amount+1);
    combinations[0] = 1

    for coin in denominations:
        for higherAmount in range(coin, amount+1):
            remainder = higherAmount-coin
            combinations[higherAmount] += combinations[remainder]
 
    return combinations[amount]

'''
To-do:

Use memoization to improve the efficiency of the recursive method
Try to return the possible combinations as well as the number of combinations
'''

def main():
    testCase = (4, [1,2,3])

    combinations = findCombosBottomUp(testCase[0], testCase[1])
    print("Using %s to produce %s, there are %s combinations."
        % (testCase[1], testCase[0], combinations))

if __name__ == "__main__":
    main()