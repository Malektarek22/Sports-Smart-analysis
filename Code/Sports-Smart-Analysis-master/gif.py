import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation
import cv2
import Drawing as draw
import mysql.connector
import uiTesting as ut
import ui
import easygui


def animation(x, y, sports):
    if sports == 1:
        img = cv2.imread("media/football.jpg")
    elif sports == 0:
        img = cv2.imread("media/football.jpg")

    fig, ax = plt.subplots()

    ax.imshow(img, origin='upper')
    plt.ylim(max(plt.ylim()), min(plt.ylim()))
    graph, = plt.plot([], [], color='red' )

    def animate(i):
        graph.set_data(x[:i + 1], y[:i + 1])

        return graph

    ani = FuncAnimation(fig, animate)
    plt.show()

