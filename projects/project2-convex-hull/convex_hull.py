from which_pyqt import PYQT_VER
if PYQT_VER == 'PYQT5':
    from PyQt5.QtCore import QLineF, QPointF, QObject
elif PYQT_VER == 'PYQT4':
    from PyQt4.QtCore import QLineF, QPointF, QObject
elif PYQT_VER == 'PYQT6':
    from PyQt6.QtCore import QLineF, QPointF, QObject
else:
    raise Exception('Unsupported Version of PyQt: {}'.format(PYQT_VER))



import time

# Some global color constants that might be useful
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

# Global variable that controls the speed of the recursion automation, in seconds
PAUSE = 0.75

#
# This is the class you have to complete.
#
class ConvexHullSolver(QObject):

# Class constructor
    def __init__( self):
        super().__init__()
        self.pause = True

# Some helper methods that make calls to the GUI, allowing us to send updates
# to be displayed.

    def showTangent(self, line, color):
        self.view.addLines([line],color)
        if self.pause:
            time.sleep(PAUSE)

    def eraseTangent(self, line):
        self.view.clearLines(line)

    def blinkTangent(self,line,color):
        self.showTangent(line,color)
        self.eraseTangent([line])

    def showHull(self, polygon, color):
        self.view.addLines(polygon,color)
        if self.pause:
            time.sleep(PAUSE)

    def eraseHull(self,polygon):
        self.view.clearLines(polygon)

    def showText(self,text):
        self.view.displayStatusText(text)


# This is the method that gets called by the GUI and actually executes
# the finding of the hull
    def compute_hull( self, points: list, pause, view):
        self.pause = pause
        self.view = view
        assert( type(points) == list and type(points[0]) == QPointF )

        t1 = time.time()
        # SORT THE POINTS BY INCREASING X-VALUE
        points.sort(key=lambda p: p.x())
        t2 = time.time()

        t3 = time.time()
        A = 2
        polygon = self.divide_and_conquer(points, A)
        # REPLACE THE LINE ABOVE WITH A CALL TO YOUR DIVIDE-AND-CONQUER CONVEX HULL SOLVER
        t4 = time.time()

        # when passing lines to the display, pass a list of QLineF objects.  Each QLineF
        # object can be created with two QPointF objects corresponding to the endpoints
        hull = []
        for i in range(len(polygon)):
            hull.append(QLineF(polygon[i], polygon[(i + 1) % len(polygon)]))
        self.showHull(hull,RED)
        self.showText('Time Elapsed (Convex Hull): {:3.5f} sec'.format(t4-t3))

    
    def divide_and_conquer(self, points: list, a: int):
        # print('divide')
        if len(points) <= 3:
            if len(points) == 3:
                slope1 = (points[1].y() - points[0].y()) / (points[1].x() - points[0].x())
                slope2 = (points[2].y() - points[0].y()) / (points[2].x() - points[0].x())
                if slope1 > slope2:
                    return [points[0], points[1], points[2]]
                else:
                    return [points[0], points[2], points[1]]
            return points
        parts, left = divmod(len(points), a)
        # split = [points[i * parts + min(i, left):(i + 1) * parts + min(i + 1, left)] for i in range(a)]
        split = []
        for i in range(a):
            split.append(points[i * parts + min(i, left):(i + 1) * parts + min(i + 1, left)])

        y1 = []
        for i in range(a):
            y1.append(self.divide_and_conquer(split[i], a))
            # print('divide return')
        y = self.merge(y1, a)
        # print('merge return')
        return y


            
    def merge(self, y: list, a: int):
        # print('merge')
        L = y[0]
        R = y[1]
        for i in range(a - 1):
            # #DEBUG
            # shapeR = []
            # shapeL = []
            # for i in range(len(L)):
            #     shapeL.append(QLineF(L[i], L[((i + 1) % len(L))]))
            # self.showHull(shapeL, BLUE)
            # for i in range(len(R)):
            #     shapeR.append(QLineF(R[i], R[((i + 1) % len(R))]))
            # self.showHull(shapeR, BLUE)

            upper = self.findUpperTangent(L,R)
            lower = self.findLowerTangent(L,R)
            temp = []

            i = lower[0]
            while True:
                temp.append(L[i])
                if i == upper[0]:
                    break
                i = (i + 1) % len(L)

            # Traverse R from upper[1] to lower[1] in a circular manner
            i = upper[1]
            while True:
                temp.append(R[i])
                if i == lower[1]:
                    break
                i = (i + 1) % len(R)
            
            # self.eraseHull(shapeL)
            # self.eraseHull(shapeR)

            # tempLines = []
            # for i in range(len(temp)):
            #     tempLines.append(QLineF(temp[i], temp[((i + 1) % len(temp))]))
            # self.showHull(tempLines, (0, 255, 255))
            # self.eraseHull(tempLines)
            L = temp


        return L

            

    def findUpperTangent(self, L: list[QPointF], R: list[QPointF]):
        rightMostL = L.index(max(L, key=lambda p: p.x()))
        leftMostR = R.index(min(R, key=lambda p: p.x()))



        # line = QLineF(L[rightMostL], R[leftMostR])
        # self.blinkTangent(line, GREEN)
        done = False
        temp = (L[rightMostL].y() - R[leftMostR].y()) / (L[rightMostL].x() - R[leftMostR].x())
        done = False
        while not done:
            done = True
            while temp > ((L[(len(L) - 1 if rightMostL == 0 else rightMostL - 1)].y() - R[leftMostR].y()) / (L[(len(L) - 1 if rightMostL == 0 else rightMostL - 1)].x() - R[leftMostR].x())):
                r = (len(L) - 1 if rightMostL == 0 else rightMostL - 1)
                temp = (L[r].y() - R[leftMostR].y()) / (L[r].x() - R[leftMostR].x())
                rightMostL = r
                done = False
                # #DEBUG
                # line = QLineF(L[rightMostL], R[leftMostR])
                # self.blinkTangent(line, GREEN)
            while temp < ((R[(0 if leftMostR == len(R) - 1 else leftMostR + 1)].y() - L[rightMostL].y()) / (R[(0 if leftMostR == len(R) - 1 else leftMostR + 1)].x() - L[rightMostL].x())):
                r = (0 if leftMostR == len(R) - 1 else leftMostR + 1)
                temp = (R[r].y() - L[rightMostL].y()) / (R[r].x() - L[rightMostL].x())
                leftMostR = r
                done = False

                # #DEBUG
                # line = QLineF(L[rightMostL], R[leftMostR])
                # self.blinkTangent(line, GREEN)
        return [rightMostL, leftMostR]
    

    def findLowerTangent(self, L: list[QPointF], R: list[QPointF]):
        # print('lower')
        rightMostL = L.index(max(L, key=lambda p: p.x()))
        leftMostR = R.index(min(R, key=lambda p: p.x()))
        

        done = False
        temp = (L[rightMostL].y() - R[leftMostR].y()) / (L[rightMostL].x() - R[leftMostR].x())
        done = False
        while not done:
            done = True
            while temp < ((L[(0 if rightMostL == len(L) - 1 else rightMostL + 1)].y() - R[leftMostR].y()) / (L[(0 if rightMostL == len(L) - 1 else rightMostL + 1)].x() - R[leftMostR].x())):
                r = (0 if rightMostL == len(L) - 1 else rightMostL + 1)
                temp = (L[r].y() - R[leftMostR].y()) / (L[r].x() - R[leftMostR].x())
                done = False
                rightMostL = r

                # #  DEBUG
                # line = QLineF(L[rightMostL], R[leftMostR])
                # self.blinkTangent(line, RED)
            while temp > ((R[(len(R) - 1 if leftMostR == 0 else leftMostR - 1)].y() - L[rightMostL].y()) / (R[(len(R) - 1 if leftMostR == 0 else leftMostR - 1)].x() - L[rightMostL].x())):
                r = (len(R) - 1 if leftMostR == 0 else leftMostR - 1)
                temp = (R[r].y() - L[rightMostL].y()) / (R[r].x() - L[rightMostL].x())
                leftMostR = r
                done = False

                # #DEBUG
                # line = QLineF(L[rightMostL], R[leftMostR])
                # self.blinkTangent(line, RED)
        return [rightMostL, leftMostR]

