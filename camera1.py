#! /usr/bin/python2.7

from SimpleCV import *
import time

cam = Camera(1)

while 1:
   img = cam.getImage()
   img.show()

