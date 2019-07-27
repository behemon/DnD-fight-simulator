import random
import os,sys
import configparser
import copy
from time import sleep
import tkinter
from tkinter import N, S, E, W
from A_star_algorithm import pathFind
import PyQt5
from PyQt5 import QtWidgets, uic, QtCore, QtGui
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QPushButton
from dictionaries import *
import monster_dictionary as MD
from map_generator import mainMap


config = configparser.ConfigParser(strict=False)
config.read("settings.cfg")


class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__() # Call the inherited classes __init__ method
        ui = uic.loadUi('DnD_gui.ui', self) # Load the .ui file
        self.myMap = mainMap()
        # self.create_map_matrix(myMap)
        self.update_map_matrix(self.myMap)
        self.show()  # Show the GUI
        ui.Button1.clicked.connect(self.on_click)

        self.show()

    @pyqtSlot()
    def on_click(self):
        print('Running Game')
        self.create_map_matrix(self.myMap)

    def create_map_matrix(self, myMap):
        myMap.__init__()
        myMap.makeRooms()
        myMap.makeRoomPaths()
        pen = QtGui.QPen(QtCore.Qt.black)
        brush = QtGui.QBrush(QtCore.Qt.black)
        scene = QtWidgets.QGraphicsScene()
        self.graphicsView.setScene(scene)
        side = 600 / config.getint("map", "columns") - 0.2
        for x in range(myMap.rows):
            for y in range(myMap.columns):
                xy = myMap.mapMatrix[x, y][0]
                r = QtCore.QRectF(QtCore.QPointF(x * side, y * side), QtCore.QSizeF(side, side))
                if xy is 1:
                    scene.addRect(r, pen, brush)
                else:
                    scene.addRect(r, pen)

    def update_map_matrix(self, myMap):
        myMap.__init__()
        myMap.makeRooms()
        myMap.makeRoomPaths()
        pen = QtGui.QPen(QtCore.Qt.black)
        brush = QtGui.QBrush(QtCore.Qt.black)
        scene = QtWidgets.QGraphicsScene()
        self.graphicsView.setScene(scene)
        side = 600 / config.getint("map", "columns") - 0.2
        for x in range(myMap.rows):
            for y in range(myMap.columns):
                xy = myMap.mapMatrix[x, y][0]
                r = QtCore.QRectF(QtCore.QPointF(x * side, y * side), QtCore.QSizeF(side, side))
                if xy is 1:
                    scene.addRect(r, pen, brush)
                else:
                    scene.addRect(r, pen)


def main():

    app = QtWidgets.QApplication(sys.argv)
    window = Ui_MainWindow()
    app.exec_()


if __name__ == "__main__":
    main()


