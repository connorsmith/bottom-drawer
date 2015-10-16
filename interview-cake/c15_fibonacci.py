'''
Simple non-recursive definition.

Apparently there's a way with matrix math to optimize down to o(lgn), later
'''
def fibonacci(n):
    if n in [0,1]:
        return n

    first = 0
    second = 1

    for i in range(n-1):
        second, first = second + first, second

    return second

def main():
    testArray = [0,1,2,3,4]

    for testNum in testArray:
        print(fibonacci(testNum))

if __name__ == "__main__":
    main()