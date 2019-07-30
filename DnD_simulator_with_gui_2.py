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
import NPC_class


config = configparser.ConfigParser(strict=False)
config.read("settings.cfg")


class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()  # Call the inherited classes __init__ method
        self.ui = uic.loadUi('DnD_gui.ui', self)  # Load the .ui file
        self.myMap = mainMap()
        self.update_map_matrix(self.myMap)
        self.show()  # Show the GUI
        self.ui.Button1.clicked.connect(self.on_click)

        self.hero = None

        self.show()

    @pyqtSlot()
    def on_click(self):
        print('Running Game')
        self.create_map_matrix(self.myMap)
        self.hero = NPC_class.Hero(config.get('Hero_conf', 'Hname'))
        self.generate_char()



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

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Ui_MainWindow()
    app.exec_()


if __name__ == "__main__":
    main()


