import configparser
import random


class MainMap:
    def __init__(self):
        config = configparser.ConfigParser(strict=False)
        config.read("settings.cfg")
        self.columns = config.getint("map", "columns")
        self.rows = config.getint("map", "rows")
        self.numberOfRooms = config.getint("map", "numberOfRooms")
        self.roomMinSize = config.getint("map", "roomMinSize")
        self.roomMaxSize = config.getint("map", "roomMaxSize")
        self.mapMatrix = {}
        self.makeMatrixDict()
        self.roomsList = []
        self.side = 0

    def makeMatrixDict(self):
        for x in range(self.columns):
            for y in range(self.rows):
                self.roomsList = []
                self.mapMatrix[y, x] = [1, None]

    def makeRoom(self):
        for tries in range(20):
            size = random.randrange(self.roomMinSize, self.roomMaxSize)  # + 2
            x_start = random.randrange(0, self.rows - size)
            y_start = random.randrange(0, self.columns - size)
            room = [x_start, y_start, size]
            if self.checkRoomLocation(room):
                self.roomsList.append(room)
                for x in range(x_start, x_start + size):
                    for y in range(y_start, y_start + size):
                        self.mapMatrix[x, y][0] = None

                # for x in range(x_start, x_start + size + 1):
                #     self.mapMatrix[x, y_start][0] = 1
                #     self.mapMatrix[x, y_start + size][0] = 1
                #
                # for y in range(y_start, y_start + size + 1):
                #     self.mapMatrix[x_start, y][0] = 1
                #     self.mapMatrix[x_start + size, y][0] = 1

                break

    def checkRoomLocation(self, testRoom):

        def intersects(testRoom, room):
            # (R1.topLeft.x < R2.bottomRight.x) &&
            # (R1.bottomRight.x > R2.topLeft.x) &&
            # (R1.topLeft.y < R2.bottomRight.y) &&
            # (R1.bottomRight.y > R2.topLeft.y)
            return not (
                    testRoom[0] <= room[0] + room[2] and
                    testRoom[0] + testRoom[2] >= room[0] and
                    testRoom[1] <= room[1] + room[2] and
                    testRoom[1] + testRoom[2] >= room[1]
            )

        for room in self.roomsList:
            if not intersects(testRoom, room):
                return False
        return True

    def makeRooms(self):
        for room in range(self.numberOfRooms):
            self.makeRoom()

    def makeRoomPath(self, point_a, point_b):
        def forx(x, y, d):
            for xa in range(d):
                self.mapMatrix[x + xa, y][0] = None

        def fory(x, y, d):
            for ya in range(d):
                self.mapMatrix[x, y + ya][0] = None

        if point_a[0] > point_b[0]:
            forx(point_b[0], point_a[1], point_a[0] - point_b[0] + 1)
            if point_a[1] > point_b[1]:
                fory(point_b[0], point_b[1], point_a[1] - point_b[1] + 1)
            else:
                fory(point_b[0], point_a[1], point_b[1] - point_a[1] + 1)
        else:
            forx(point_a[0], point_b[1], point_b[0] - point_a[0] + 1)
            if point_b[1] > point_a[1]:
                fory(point_a[0], point_a[1], point_b[1] - point_a[1] + 1)
            else:
                fory(point_a[0], point_b[1], point_a[1] - point_b[1] + 1)

    def makeRoomPaths(self):
        points = []
        for room in self.roomsList:
            room_senter_x = random.randrange(room[0], room[0] + room[2])
            room_senter_y = random.randrange(room[1], room[1] + room[2])
            # print (room_senter_x,room_senter_y)
            points.append([room_senter_x, room_senter_y])

        # create a pathway from point a to point b
        for n in range(len(points) - 1):
            self.makeRoomPath(points[n], points[n + 1])
            # print (points[n],points[n+1])

    def printMap(self):
        print('Map:')
        for x in range(self.rows):
            for y in range(self.columns):
                xy = self.mapMatrix[x, y][0]
                if xy is None:
                    print(' . ', end="")  # space
                elif xy == 1:
                    print(' O ', end="")  # obstacle
                elif xy == 2:
                    print(' S ', end="")  # start
                elif xy == 3:
                    print(' R ', end="")  # route
                elif xy == 4:
                    print(' F ', end="")  # finish
                else:
                    print(' X ', end="")
            print("")
        # print("exiting on map print for debug")
        # sys.exit()

    def freeSpaces(self):
        freespace = []
        for xy in list(self.mapMatrix.keys()):
            # print (xy)
            if self.mapMatrix[xy][0] != 1:
                freespace.append(xy)
        return freespace

    def DIJFreeSpaces(self):
        xy = []
        for x in range(self.rows):
            row = ""
            for y in range(self.columns):
                sell = self.mapMatrix[y, x][0]
                if sell == 1:
                    row = row + "X"
                else:
                    row = row + "."
            xy.append(row)
        # for row in xy:
        #     print (row)
        return xy
