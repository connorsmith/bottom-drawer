def getSumOfArithmeticSeries(n):
    return 0.5 * n * (1 + n)

def main():
    l = [1,2,3,4,5,6,7,7,8,9,10]
    countdownSum = getSumOfArithmeticSeries(10)

    for number in l:
        countdownSum -= number

    print(-1*countdownSum)

if __name__ == "__main__":
    main()