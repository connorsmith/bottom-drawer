def getBagValueOptimized(bag, cakeTupleList):
    '''
    Best case: fill the entire bag with the highest value density cake

    Problem: what if that cake doesn't fit in evenly

    Solution: Build a LUT for each integer kilogram the bag holds
    '''
    
    augmentedCakeList = []

    for cakeTuple in cakeTupleList:
        if cakeTuple[0] == 0:
            if cakeTuple[1] > 0:
                return int('inf')
        else:
            augmentedCakeList.append(   (cakeTuple[0],cakeTuple[1],cakeTuple[1]/cakeTuple[0]))

    # cost of O(nlogn) number of cake options
    augmentedCakeList = sorted(augmentedCakeList, key=lambda val: val[0], reverse = False)

    bestValueList = [0]

    cakeNum = len(augmentedCakeList)

    # cost of O(k) bag size
    for size in range(1,bag+1):
        ind = 0
        currentMax = 0
        temp = 0
        while ind < cakeNum-1 and augmentedCakeList[ind][0] <= size:
            temp = augmentedCakeList[ind][1] + bestValueList[size-augmentedCakeList[ind][0]]
            if temp > currentMax:
                currentMax = temp
            ind += 1
        bestValueList.append(max(currentMax, bestValueList[size-1]))
        # print(bestValueList)


    return bestValueList[bag]

def getBagValue(bag, cakeTuple):
    # empty cake list case
    if cakeTuple == []:
        return 0
    print('%s and %s'%(bag, cakeTuple))

    firstCake = cakeTuple[0]

    # deals with the infinite cake (0, x>0) or air cake (0,0)
    if firstCake[0] == 0:
        if firstCake[1] > 0:
            return int('inf')
        else:
            return getBagValue(bag, cakeTuple[1:])

    if bag == 0:
        return 0

    if firstCake[0] == bag:
        return firstCake[1]

    maxVal = 0
    numberUsed = 0
    while numberUsed*firstCake[0] <= bag:
        tempVal = numberUsed*firstCake[1] + getBagValue(bag - numberUsed*firstCake[0], cakeTuple[1:])
        if tempVal > maxVal:
            maxVal = tempVal
        numberUsed += 1
    return maxVal

def main():
    cakeTuple = [(7, 160), (3, 90), (2, 15),(0,0)]
    # cakeTuple = [(10, 160),(9, 165),(2,10)]
    bagSize = 10

    print(getBagValue(bagSize, cakeTuple))
    print(getBagValueOptimized(bagSize,cakeTuple))

if __name__ == "__main__":
    main()