def overlap(time1, time2):
    '''
    Returns None if the slots don't overlap, or a tuple consisting of the 
    union of the two time slots if they do.
    '''

    if time1[0] < time2[0]:
        earlierStart = time1
        laterStart = time2
    else:
        earlierStart = time2
        laterStart = time1

    if earlierStart[1] >= laterStart[0]:
        condensedTime = (earlierStart[0], max(earlierStart[1], laterStart[1]))
    else:
        condensedTime = None

    return condensedTime

def condenseTimes(meetingTimes):

    condensedTimes = []   
    overlapFlag = False

    # worst case is O(n^2) if there are no overlaps at all
    for meeting in meetingTimes:
        if condensedTimes == []:
            condensedTimes.append(meeting)
        else:
            loopFlag = False
            for i in range(len(condensedTimes)):
                overlapTuple = overlap(condensedTimes[i], meeting)
                if overlapTuple:
                    condensedTimes[i] = overlapTuple
                    overlapFlag = True
                    loopFlag = True
                    break

            if not loopFlag:
                condensedTimes.append(meeting)

    while overlapFlag:
        condensedTimes, overlapFlag = condenseTimes(condensedTimes)

    return (condensedTimes, overlapFlag)


def main():
    testCaseList = [[(1, 2), (2, 3)], 
        [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)],
        [(1, 5), (2, 3)], 
        [(1, 10), (2, 6), (3, 5), (7, 9)]]

    # *** Pythonic loop counter using enumerate
    for idx, meetingTimes in enumerate(testCaseList):
        print("Test Case %s"%(idx))
        condensedTimes, unused_temp = condenseTimes(meetingTimes)
        print("%s becomes %s\n"%(meetingTimes, condensedTimes))

if __name__ == "__main__":
    main()