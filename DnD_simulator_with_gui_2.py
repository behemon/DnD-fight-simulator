import random
import os,sys
import configparser
import copy
from time import sleep
from A_star_algorithm import pathFind
from PyQt5 import QtWidgets, uic, QtCore, QtGui
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QPainter, QBrush, QPen
from PyQt5.QtWidgets import QPushButton
from dictionaries import *
import monster_dictionary as MD
from map_generator import mainMap
from NPC_class import *
import dijkstra_algorithm as dij
import gog
import Raycasting

config = configparser.ConfigParser(strict=False)
config.read("settings.cfg")


class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()  # Call the inherited classes __init__ method
        self.ui = uic.loadUi('DnD_gui.ui', self)  # Load the .ui file
        self.scene = None
        self.FOV_list = []

        # self.myMap = mainMap()
        # self.myMap.side = 600 / config.getint("map", "columns") - 0.2
        self.myMap = gog.Map()
        self.side = 600 / config.getint("map", "columns") - 0.2

        self.freedom_directions = 8  # number of possible directions to move on the map
        if self.freedom_directions == 4:
            self.dx = [1, 0, -1, 0]
            self.dy = [0, 1, 0, -1]
        elif self.freedom_directions == 8:
            self.dx = [1, 1, 0, -1, -1, -1, 0, 1]
            self.dy = [0, 1, 1, 1, 0, -1, -1, -1]

        # self.scene = QtWidgets.QGraphicsScene()
        # self.painter = QPainter()
        self.show()  # Show the GUI
        self.ui.Button1.clicked.connect(self.on_click)

        self.hero = None
        self.units_list = []

    @pyqtSlot()
    def on_click(self):
        print('Running Game')
        self.scene = QtWidgets.QGraphicsScene()
        self.create_map_matrix(self.myMap)
        # self.DIJmap(verbose=True)
        self.hero = Hero(config.get('Hero_conf', 'Hname'))
        self.generate_char()
        self.run_game()

    # interest_points - is a list of tuples of interest points no the free space map
    def DIJmap(self, interest_points=[], verbose=False):

        if len(interest_points) is 0:
            interest_points = random.choices(self.myMap.freeSpaces(), k=1)
        dijmap = dij.computeDistanceMap(dij.parseInputMap(self.myMap.DIJFreeSpaces()), interest_points)

        min = -2000
        xy = [0,0]
        for line in dijmap:
            for sell in line:
                if sell == 2000:
                    continue
                if sell > min:
                    min = sell

        if verbose:
            # scene = QtWidgets.QGraphicsScene()
            self.graphicsView.setScene(self.scene)
            for x in range(self.myMap.rows):
                for y in range(self.myMap.columns):
                    # xy = self.myMap.mapMatrix[x, y][0]
                    xy = self.myMap.mdict[x, y][0]
                    sell = dijmap[y][x]
                    if sell == 2000:
                        continue

                    pen = QtGui.QColor(255, 255 - 255/min*sell, 0)
                    brush = QtGui.QColor(127, 255 - 255/min*sell, 0)
                    side = 600 / config.getint("map", "columns") - 0.2
                    # print(sell)
                    r = QtCore.QRectF(QtCore.QPointF(x * side, y * side), QtCore.QSizeF(side, side))
                    self.scene.addRect(r, pen, brush)
        return dijmap

    def create_map_matrix(self, myMap):
        # myMap.__init__()
        # myMap.makeRooms()
        # myMap.makeRoomPaths()
        myMap.generateLevel()
        myMap.useCellularAutomata()
        myMap.make_map_dict()
        pen = QtGui.QPen(QtCore.Qt.black)
        brush = QtGui.QBrush(QtCore.Qt.black)
        # scene = QtWidgets.QGraphicsScene()
        self.graphicsView.setScene(self.scene)
        side = 600 / config.getint("map", "columns") - 0.2

        # for x in range(myMap.rows):
        #     for y in range(myMap.columns):
        #         xy = myMap.mapMatrix[x, y][0]
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
        # side = 600 / config.getint("map", "columns") - 0.2
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
        print(len(self.scene.items()))  # counts the amount of items on board

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
        self.test_actions()

    def test_actions(self):
        # while len(self.units_list) > 1 or self.hero not in self.units_list:
        while True:
            for unit in self.units_list:
                if unit.type is "monster":  # monster move
                    unit.dij = self.DIJmap([self.hero.location], False)
                    # self.update()

                    weight, direction = self.check_neighbors_sells(unit, unit.dij)
                    if weight > 0 and direction is not -1: # distance to target 0 - the target is next cell
                        self.move_unit(unit, direction)
                    else:
                        self.delete_unit(unit)
                    sleep(0.1/len(self.units_list))
                else:  # hero moves
                    sleep(0.8 / len(self.units_list))
                    self.move_unit(unit, random.choice(range(self.freedom_directions)))
                    print (self.myMap.mdict)
                    Raycasting.fov_calc(unit.location[0], unit.location[1], 15, self.myMap.level, self.myMap.mdict, 50, 50)
                    # print(self.myMap.level)

                QtWidgets.QApplication.processEvents()  # UPDATES THE scene !!!! not self.show or self.update !!!!
            self.update_map_FOV()
            QtWidgets.QApplication.processEvents()  # UPDATES THE scene !!!! not self.show or self.update !!!!

    def delete_unit(self, unit):
        self.scene.removeItem(unit.qtitem)
        self.myMap.mdict[unit.location] = [0, None]
        self.units_list.remove(unit)

    def test_movment(self):
        dij = self.DIJmap(verbose=False)

        while True:
            # self.update()
            QtWidgets.QApplication.processEvents()
            weight, direction = self.check_neighbors_sells(self.hero, dij)
            self.move_unit(self.hero, dij, direction)
            sleep(0.1) # turn time
            if weight < 1:
                break

    def move_unit(self,unit, direction):
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


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Ui_MainWindow()
    app.exec_()


if __name__ == "__main__":
    main()


