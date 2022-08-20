import heapq


def computeDistanceMap(costMap, starts):
    maxDistance = 2000
    sizeY = len(costMap)
    sizeX = len(costMap[0])
    distMap = [[maxDistance for x in range(sizeX)] for y in range(sizeY)]

    # Starting positions have a distance of zero and are scheduled
    # for visiting at that distance

    pq = []
    for posStart in starts:
        heapq.heappush(pq, (0, posStart))

    while pq:
        dist, pos = heapq.heappop(pq)

        # Has this node already been visited?

        if distMap[pos[1]][pos[0]] <= dist:
            continue

        # Visit this node

        distMap[pos[1]][pos[0]] = dist

        # Schedule neighbors for visiting

        for dPos in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            posNew = (pos[0] + dPos[0], pos[1] + dPos[1])
            if posNew[0] < 0 or posNew[0] >= sizeX:
                continue
            if posNew[1] < 0 or posNew[1] >= sizeY:
                continue
            distNew = dist + costMap[posNew[1]][posNew[0]]
            if distNew >= distMap[posNew[1]][posNew[0]]:
                continue
            heapq.heappush(pq, (distNew, posNew))

    return distMap


def costForChar(c):
    impassableCost = 2000
    passableCost = 1
    return impassableCost if c == 'X' else passableCost


def parseInputMap(mapIn):
    # return [[costForChar(c) for c in row] for row in mapIn.split()]
    return [[costForChar(c) for c in row] for row in mapIn]


def printDistanceMap(distMap):
    maxDistance = 2000
    for row in distMap:
        for dist in row:
            if dist == maxDistance:
                c = '-'
            else:
                c = chr(dist % 10 + ord('0'))
            print(c, end='')
        print('')

# Test


if __name__ == "__main__":

    inputMap='''
    XXXXXXXXXXXXXXXXXXXX
    X.........X........X
    XXXXXXXXX.X...XX...X
    X.........X...XX...X
    X.X.......X...XX...X
    X.X.......X........X
    X.XXXXXX.....XXXXXXX
    X......X.....X.....X
    X......X.....X.....X
    XXXXXXXXXXXXXXXXXXXX
    '''

    costMap = parseInputMap(inputMap)
    distMap = computeDistanceMap(costMap, [(1, 1), (4, 4)])
    printDistanceMap(distMap)
