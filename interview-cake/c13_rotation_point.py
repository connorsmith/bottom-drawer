'''
Given a sorted array that has been rotated, find the index of rotation.
'''

# trivial implementation, with O(n) performance
def findRotationPointLinear(inputList):
    for i in range(len(inputList)-1):
        if inputList[i+1] < inputList[i]:
            return i+1
    # if the array wasn't actually rotated
    return 0

# taking advantage of the almost sort nature of the list -> O(log(n))
def findRotationPointBinary(inputList):
    startIndex = 0
    endIndex = len(inputList) - 1
    middleIndex = int(len(inputList)/2.0)

    if inputList[startIndex] < inputList[endIndex]:
        return 0

    while startIndex < endIndex:
        if inputList[startIndex] < inputList[middleIndex]:
            startIndex = middleIndex
        else:
            endIndex = middleIndex
        middleIndex = (endIndex + startIndex) / 2
    
    # print("start index: %s, end index: %s, middle index: %s"%(startIndex, endIndex, middleIndex))
    return endIndex+1


def main():
    # test case 1
    words = [
        'ptolemaic',
        'retrograde',
        'supplant',
        'undulate',
        'xenoepist',
        'asymptote', # <-- rotates here!
        'babka',
        'banoffee',
        'engender',
        'karpatka',
        'othellolagkage'
    ]
    
    print('Using linear search, rotation point: %s' %(words[findRotationPointLinear(words)]))
    print('Using binary search, rotation point: %s\n' %(words[findRotationPointBinary(words)]))

    # test case 2
    words = [
        'zebra',
        'angler',
        'broom',
        'cobra'
    ]
    
    print('Using linear search, rotation point: %s' %(words[findRotationPointLinear(words)]))
    print('Using binary search, rotation point: %s\n' %(words[findRotationPointBinary(words)]))

    # test case 3
    words = [
        'comedian'
        'xylophone',
        'avocado',
    ]
    
    print('Using linear search, rotation point: %s' %(words[findRotationPointLinear(words)]))
    print('Using binary search, rotation point: %s\n' %(words[findRotationPointBinary(words)]))

    
if __name__ == "__main__":
    main()