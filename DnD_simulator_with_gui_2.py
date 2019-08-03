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

config = configparser.ConfigParser(strict=False)
config.read("settings.cfg")


class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()  # Call the inherited classes __init__ method
        self.ui = uic.loadUi('DnD_gui.ui', self)  # Load the .ui file

        self.myMap = mainMap()
        self.myMap.side = 600 / config.getint("map", "columns") - 0.2
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

        self.show()

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
                    xy = self.myMap.mapMatrix[x, y][0]
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
        myMap.__init__()
        myMap.makeRooms()
        myMap.makeRoomPaths()
        pen = QtGui.QPen(QtCore.Qt.black)
        brush = QtGui.QBrush(QtCore.Qt.black)
        # scene = QtWidgets.QGraphicsScene()
        self.graphicsView.setScene(self.scene)
        side = 600 / config.getint("map", "columns") - 0.2
        for x in range(myMap.rows):
            for y in range(myMap.columns):
                xy = myMap.mapMatrix[x, y][0]
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
        self.hero.populate_space_on_grid_pyqt5(self.myMap, self.side)
        self.update_unit_on_map(self.hero)

        dij = self.DIJmap(verbose=True)
        while True:
            self.update()
            QtWidgets.QApplication.processEvents()
            weight, direction = self.check_neighbors_sells(self.hero, dij)
            self.move_unit(self.hero,dij,direction)
            sleep(1)


    def move_unit(self,unit, dij, direction):
        # if dij[unit.location[0]+self.dx[direction]][unit.location[1]+self.dy[direction]] == 2000:
        #     print("can't move in this direction")
        #     return
        new_x = unit.location[0] + self.dx[direction]
        new_y = unit.location[1] + self.dy[direction]
        unit.location = (new_x, new_y)
        self.update_unit_on_map(unit)

    def check_neighbors_sells(self,unit,map):
        xy = [0,0]
        weight = 2000
        direction = 0
        for cell in range(self.freedom_directions):
            xy_new = ([unit.location[1]+self.dy[cell]], [unit.location[0]+self.dx[cell]])
            weight_new = (map[unit.location[1]+self.dy[cell]][unit.location[0]+self.dx[cell]])
            # print(weight_new)
            if weight > weight_new:
                weight = weight_new
                xy = xy_new
                direction = cell
        # print(weight,xy,direction)
        return (weight,direction)

    def update_unit_on_map(self,unit):
        unit.populate_space_on_grid_pyqt5(self.myMap, self.side, unit.location)
        pen = QtGui.QPen(unit.color)
        brush = QtGui.QBrush(unit.color)
        self.graphicsView.setScene(self.scene)
        x_offset = unit.location[0] * self.side
        y_offset = unit.location[1] * self.side
        diameter = self.side
        self.scene.addEllipse(x_offset, y_offset, diameter, diameter, pen, brush)
        self.show()


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Ui_MainWindow()
    app.exec_()


if __name__ == "__main__":
    main()


