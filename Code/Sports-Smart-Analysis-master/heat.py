import cv2
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Arc
import seaborn as sns
import mysql.connector
import uiTesting as ut
import ui
import easygui


def heat(x, y, sports):
	if (sports == 1):
		img = cv2.imread("media/football.jpg")
	elif sports == 0:
		img = cv2.imread("media/football.jpg")

	fig, ax = plt.subplots()

	ax.imshow(img, aspect='equal', origin='upper')

	plt.ylim(max(plt.ylim()), min(plt.ylim()))

	# Tidy Axes
	plt.axis('on')
	possition =[
		x,y
	]
	sns.kdeplot(possition, shade=True, color='blue', label='KDE Plot')

	plt.show()
