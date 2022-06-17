# global imports
import sys
import time
import configparser
from PyQt5 import QtWidgets, uic, QtCore, QtGui
from bresenham import bresenham

# local imports
import gog
import Line_of_sight_algorithm as line_of_sight
import A_star_algorithm_2 as Astar
from NPC_class import *


config = configparser.ConfigParser(strict=False)
config.read("settings.cfg")


class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()  # Call the inherited classes __init__ method
        self.ui = uic.loadUi('DnD_gui.ui', self)  # Load the .ui file
        self.scene = None
        self.FOV_list = []

        self.myMap = gog.Map()
        self.side = 600 / config.getint("map", "columns") - 0.2

        self.freedom_directions = 8  # number of possible directions to move on the map
        if self.freedom_directions == 4:
            self.dx = [1, 0, -1, 0]
            self.dy = [0, 1, 0, -1]
        elif self.freedom_directions == 8:
            self.dx = [1, 1, 0, -1, -1, -1, 0, 1]
            self.dy = [0, 1, 1, 1, 0, -1, -1, -1]

        self.show()  # Show the GUI
        self.ui.Button1.clicked.connect(self.on_click)

        self.hero = None
        self.units_list = []
        self.monster_list = []

    def on_click(self):
        print('Running Game')
        self.scene = QtWidgets.QGraphicsScene()
        self.create_map_matrix(self.myMap)
        # self.DIJmap(verbose=True)
        self.hero = Hero(config.get('Hero_conf', 'Hname'))
        self.generate_char()
        self.run_game()

    def create_map_matrix(self, myMap):
        myMap.generateLevel()
        myMap.useCellularAutomata()
        myMap.make_map_dict()
        pen = QtGui.QPen(QtCore.Qt.black)
        brush = QtGui.QBrush(QtCore.Qt.black)

        self.graphicsView.setScene(self.scene)
        side = 600 / config.getint("map", "columns") - 0.2

        for x in range(myMap.map_width):
            for y in range(myMap.map_height):
                xy = myMap.mdict[x, y][0]
                r = QtCore.QRectF(QtCore.QPointF(x * side, y * side), QtCore.QSizeF(side, side))
                if xy is 1:
                    self.scene.addRect(r, pen, brush)
                else:
                    self.scene.addRect(r, pen)

    def update_map_matrix(self, myMap):
        pen = QtGui.QPen(QtCore.Qt.black)
        brush = QtGui.QBrush(QtCore.Qt.black)
        scene = QtWidgets.QGraphicsScene()
        self.graphicsView.setScene(scene)
        for x in range(myMap.rows):
            for y in range(myMap.columns):
                xy = myMap.mapMatrix[x, y][0]
                r = QtCore.QRectF(QtCore.QPointF(x * self.side, y * self.side), QtCore.QSizeF(self.side, self.side))
                if xy is 1:
                    scene.addRect(r, pen, brush)
                else:
                    scene.addRect(r, pen)

    def update_map_FOV(self):
        black_pen = QtGui.QPen(QtCore.Qt.black)
        white_brush = QtGui.QPen(QtCore.Qt.white)
        gray_brush = QtGui.QBrush(QtCore.Qt.gray)
        light_gray_brush = QtGui.QBrush(QtCore.Qt.lightGray)
        black_brush = QtGui.QBrush(QtCore.Qt.black)
        # self.graphicsView.setScene(self.scene)
        # print(len(self.scene.items()))  # counts the amount of items on board

        for sq in self.FOV_list:
            self.scene.removeItem(sq)
        self.FOV_list = []

        for x in range(self.myMap.rows):
            for y in range(self.myMap.columns):

                transform = QtGui.QTransform()
                transform.reset()
                # xy = x * self.side, y * self.side
                # xy = QtCore.QPointF((x+0.5) * self.side, (y+0.5) * self.side)
                xy = QtCore.QPointF(x * self.side, y * self.side)
                item = self.scene.itemAt(xy, transform)
                # print(dir(item))
                # self.scene.removeItem(item)  # remove old squere
                # self.scene.removeItem(self.scene.itemAt(xy, transform))  # remove old squere

                if self.myMap.level[x][y] is 0:
                    r = QtCore.QRectF(QtCore.QPointF(x * self.side, y * self.side), QtCore.QSizeF(self.side, self.side))
                    self.FOV_list.append(self.scene.addRect(r, black_pen, gray_brush))

                if self.myMap.level[x][y] is 2:
                    r = QtCore.QRectF(QtCore.QPointF(x * self.side, y * self.side), QtCore.QSizeF(self.side, self.side))
                    self.FOV_list.append(self.scene.addRect(r, black_pen, light_gray_brush))

                elif self.myMap.level[x][y] is "- ":
                    r = QtCore.QRectF(QtCore.QPointF(x * self.side, y * self.side), QtCore.QSizeF(self.side, self.side))
                    self.FOV_list.append(self.scene.addRect(r, black_pen, white_brush))
                #
                elif self.myMap.level[x][y] is 1:
                    r = QtCore.QRectF(QtCore.QPointF(x * self.side, y * self.side), QtCore.QSizeF(self.side, self.side))
                    self.FOV_list.append(self.scene.addRect(r, black_pen, black_brush))

    def update_unit_on_map(self, unit):
        unit.populate_space_on_grid_pyqt5(self.myMap, self.side, unit.location)
        pen = QtGui.QPen(unit.color)
        brush = QtGui.QBrush(unit.color)
        self.graphicsView.setScene(self.scene)
        x_offset = unit.location[0] * self.side
        y_offset = unit.location[1] * self.side
        diameter = self.side
        unit.qtitem = self.scene.addEllipse(x_offset, y_offset, diameter, diameter, pen, brush)
        # self.show()

    def move_unit(self, unit, direction):
        # if dij[unit.location[0]+self.dx[direction]][unit.location[1]+self.dy[direction]] == 2000:
        #     print("can't move in this direction")
        #     return

        new_x = unit.location[0] + self.dx[direction]
        new_y = unit.location[1] + self.dy[direction]
        if self.myMap.mdict[(new_x,new_y)][0] is 1:
            return

        if unit.qtitem:
            self.scene.removeItem(unit.qtitem)

        if self.myMap.mdict[new_x, new_y][1] is None:
            self.myMap.mdict[unit.location][1] = None
            unit.location = (new_x, new_y)
            self.myMap.mdict[unit.location][1] = unit
        self.update_unit_on_map(unit)

    def check_neighbors_sells(self, unit, map):
        xy = [0,0]
        weight = 1000
        direction = -1
        dot = []
        for cell in range(self.freedom_directions):
            xy_new = ([unit.location[1]+self.dy[cell]], [unit.location[0]+self.dx[cell]])
            x_new = unit.location[1] + self.dy[cell]
            y_new = unit.location[0] + self.dx[cell]
            weight_new = (map[x_new][y_new])
            if 2000 > weight >= weight_new:
                weight = weight_new
                xy = xy_new
                direction = cell
                dot.append(cell)
        # direction mapping
        #   5   6   7
        #   4   X   0
        #   3   2   1
        # print(dot)
        return weight, direction
        # return weight, random.choice(dot)

    def generate_char(self):
        self.ui.label_H_AC.setText(str(self.hero.AC))
        self.ui.label_H_HP.setText(str(self.hero.HitPoints))
        self.ui.label_H_class.setText(str(self.hero.dClass))
        self.ui.label_H_race.setText(str(self.hero.dRaceName))
        self.ui.label_H_name.setText(str(self.hero.name))
        self.ui.label_H_str.setText(str(self.hero.dStr))
        self.ui.label_H_dex.setText(str(self.hero.dDex))
        self.ui.label_H_con.setText(str(self.hero.dCons))
        self.ui.label_H_int.setText(str(self.hero.dInt))
        self.ui.label_H_wiz.setText(str(self.hero.dWis))
        self.ui.label_H_cha.setText(str(self.hero.dCha))

    def run_game(self):
        self.units_list = []
        self.hero.populate_space_on_grid_pyqt5(self.myMap, self.side)
        self.myMap.mdict[self.hero.location][1] = self.hero
        self.update_unit_on_map(self.hero)
        self.units_list.append(self.hero)

        for npc in range(config.getint("monsters", "monster_number")):
            monster = Mob()
            monster.populate_space_on_grid_pyqt5(self.myMap, self.side)
            self.update_unit_on_map(monster)
            self.units_list.append(monster)
            self.monster_list.append(monster)
        self.test()

    def check_line_of_sight(self, mob1, mob2):

        los = list(bresenham(mob1.location[0], mob1.location[1], mob2.location[0], mob2.location[1]))
        can_see = True
        for point in los:
            if point not in self.myMap.freeSpaces():
                can_see = False
                break
        return can_see


    def test(self):

        # self.myMap
        while True:
            time.sleep(0.1)
            # self.update_map_FOV()

            print(self.myMap.mdict[0, 0])

            # for npc in self.monster_list:
            #     self.move_unit(npc, random.choice(range(self.freedom_directions)))

            self.move_unit(self.hero, random.choice(range(self.freedom_directions)))

            for mob in self.monster_list:
                self.check_line_of_sight(self.hero, mob)





            # for unit in self.units_list:
            #     line = (line_of_sight.get_line(self.hero.location,unit.location))
            #     for cell in line:
            #         pass
            QtWidgets.QApplication.processEvents()  # UPDATES THE scene !!!! not self.show or self.update !!!!

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Ui_MainWindow()
    app.exec_()


if __name__ == "__main__":
    main()
