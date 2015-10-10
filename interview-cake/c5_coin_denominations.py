def findCombos(amount, denominations):

    if amount == 0:
        return 1

    # no denominations, no coins
    if amount < 0 or denominations == []:
        return 0

    print("In findCombos: a(%s), d(%s)"%(amount, denominations))

    currentCoin, otherCoins = denominations[0], denominations[1:]

    comboNum = 0
    while amount >= 0:
        comboNum += findCombos(amount, otherCoins)
        amount -= currentCoin
    return comboNum


def main():
    testCase = (4, [1,2,3])

    combinations = findCombos(4, [1,2, 3])
    print("Using %s to produce %s, there are %s combinations."
        % (testCase[1], testCase[0], combinations))

if __name__ == "__main__":
    main()