'''
Write a function to return the rectangular intersection
of two input rectangles.
'''

# could also be written as a1, length1
def getAxialOverlap(a1,a2,b1,b2):
    '''
    Given the two pairs of axial coordinates, return the 
    intersection or None,None.

    If they intersect at a point, the point will be returned 
    along with height and width equal to zero.
    '''
    # ensure that the input is correctly order
    if a2 < a1:
        a1,a2 = a2,a1
    if b2 < b1:
        b1,b2 = b2,b1

    if a1 > b1:
        a1,a2,b1,b2 = b1,b2,a1,a2

    # at this point rectangle a has a start point left of b

    if b1 <= a2:
        return b1, min(b2,a2)-b1
    else:
        return None, None



def getIntersection(r1, r2):
    xNew, widthNew = getAxialOverlap(r1['x'],r1['x']+r1['width'],r2['x'],r2['x']+r2['width'])
    yNew, heightNew = getAxialOverlap(r1['y'],r1['y']+r1['height'],r2['y'],r2['y']+r2['height'])

    # print(xNew,yNew, widthNew, heightNew)
    if xNew == None or yNew == None:
        return None
    else:
        overlapRectangle = {
        'x':xNew,'y':yNew,'width':widthNew,'height':heightNew
        }

        return overlapRectangle

def main():
    rect1 = {
    'x':0,'y':0,'width':10,'height':10
    }

    rect2 = {
    'x':10,'y':10,'width':10,'height':10
    }

    rect3 = {
    'x':5,'y':5,'width':10,'height':10
    }

    rect4 = {
    'x':0,'y':0,'width':2,'height':2
    }

    rect5 = {
    'x':20,'y':20,'width':2,'height':2
    }

    rect6 = {
    'x':10,'y':0,'width':10,'height':10
    }

    # first test case, point intersection
    print(getIntersection(rect1, rect2))

    # second test case, partial intersection
    print(getIntersection(rect1, rect3))

    # third test case, one subsumes the other
    print(getIntersection(rect1, rect4))

    # fourth test case, no intersection
    print(getIntersection(rect1, rect5))

    # fifth test case, edge intersection
    print(getIntersection(rect1, rect6))

if __name__ == "__main__":
    main()