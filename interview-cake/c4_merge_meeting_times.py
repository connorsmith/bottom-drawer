def overlap(time1, time2):
    '''
    Helper function.
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

def condenseTimesV3(meetingTimes):
    # sort the meetingTimes based on start time, breaking ties with end time

    # iterate through the list and keep merging items

def condenseTimesV2(meetingTimes):
    '''
    This is an improvement for some inputs, but still
    suffers from an O(n^2) run time in the worst case 
    depending on the ordering of the meeting times.
    '''

    condensedTimes = []   
    overlapFlag = False

    for meeting in meetingTimes:
        # the first meeting
        if condensedTimes == []:
            condensedTimes.append(meeting)
        else:
            # keep track of whether there was an insertion
            loopFlag = False 
            for i in range(len(condensedTimes)):
                # check to see if there was an overlap
                overlapTuple = overlap(condensedTimes[i], meeting)
                if overlapTuple:
                    condensedTimes[i] = overlapTuple
                    overlapFlag = True
                    loopFlag = True
                    break
                else:
                    if meeting[0] < condensedTimes[i][0]:
                        condensedTimes.insert(i, meeting)
                        loopFlag = True
                        break

            if not loopFlag:
                condensedTimes.append(meeting)

        print("Current condensedTimes: %s" %(condensedTimes))

    while overlapFlag:
        condensedTimes, overlapFlag = condenseTimes(condensedTimes)

    return (condensedTimes, overlapFlag)

def condenseTimes(meetingTimes):
    '''
    Worst case is O(n^2) if there are no overlaps at all

    This could be improved by keeping the condensedTimes list sorted.
    '''

    condensedTimes = []   
    overlapFlag = False

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
        condensedTimes, unused_temp = condenseTimesV2(meetingTimes)
        print("%s becomes %s\n"%(meetingTimes, condensedTimes))

if __name__ == "__main__":
    main()

'''
Additional questions:

What if we had an upper bound on the input values? Could we make improvements and would they cost us memory?

Could this be done "In-place"? What are the pros and cons of this approach?
'''