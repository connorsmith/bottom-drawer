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
def findRotationPointBinary(inputList)
    pass
    
def main():
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
    
    rotationPoint = findRotationPointLinear(words)

    print('Rotation Point: %s' %(words[rotationPoint]))

if __name__ == "__main__":
    main()