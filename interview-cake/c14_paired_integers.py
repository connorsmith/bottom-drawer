def doesMoviePairExist(movieLengths, flightLength):
    '''
    Assumptions:
        - don't watch the same movie twice
        - only watching exactly two movies
        - optimize for runtime over memory

    Future Improvements:
        - close but not over (within 20 minutes of end time)
        - not limited to 2 movies
        - returns the list of movies to watch
    '''

    possiblePairHash = {}
    pairExists = False

    for movie in movieLengths:
        if movie in possiblePairHash:
            pairExists = True
            break
        else:
            pairTime = flightLength - movie
            if pairTime not in possiblePairHash:
                # add it
                possiblePairHash[pairTime] = 1
            else:
                # increment it, might be useful information to have later
                possiblePairHash[pairTime] += 1

    # runtime is O(n) and space is O(n)
    return pairExists

def main():
    movieLengths = [87, 82, 93, 61, 45, 113, 117, 500]
    testFlightLengths = [120, 150, 180, 210, 1000]

    for flightLength in testFlightLengths:
        print("Flight length: %s minutes - %s"%(flightLength, doesMoviePairExist(movieLengths, flightLength)))

if __name__ == "__main__":
    main()