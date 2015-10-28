def permutationIsAPalindrome(inString):
    seenDict = {}

    for character in inString:
        if character not in seenDict:
            seenDict[character] = 1
        else:
            del seenDict[character]

    return len(seenDict.keys()) <= 1

def main():

    testCaseList = []
    testCaseList.append(["civic", True])
    testCaseList.append(["iivcc", True])
    testCaseList.append(["civil", False])
    testCaseList.append(["iivlc", False])

    for index, testCase in enumerate(testCaseList):
        print("Test Case %s passed: %s"%(index+1, permutationIsAPalindrome(testCase[0])==testCase[1]))

if __name__ == "__main__":
    main()