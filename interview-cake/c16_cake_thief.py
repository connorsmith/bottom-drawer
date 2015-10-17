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
    bagSize = 20

    print(getBagValue(bagSize, cakeTuple))

if __name__ == "__main__":
    main()