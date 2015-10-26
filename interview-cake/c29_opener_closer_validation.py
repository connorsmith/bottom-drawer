from include import Stack

def validateOpenersAndClosers(inString):
    s = Stack.Stack()

    openerAndCloserDict = {'}':'{', ']':'[', ')':'('}

    for character in inString:
        if character in openerAndCloserDict.values():
            s.insert(character)
        elif character in openerAndCloserDict.keys():
            popMatch = s.pop() == openerAndCloserDict[character]
            if not popMatch:
                return False
    return True


def main():

    testCaseList = []
    testCaseList.append(["{ [ ] ( ) }", True])
    testCaseList.append(["{ [ ( ] ) }", False])
    testCaseList.append(["{ [ }", False])
    testCaseList.append(["}", False])
    testCaseList.append(["", True])

    for index, testCase in enumerate(testCaseList):
        print("Test Case %s passed: %s"%(index+1, validateOpenersAndClosers(testCase[0])==testCase[1]))

if __name__ == "__main__":
    main()