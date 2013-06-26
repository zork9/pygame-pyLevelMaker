
# Copyright (C) Johan Ceuppens 2010
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


import pygame
from pygame.locals import *
from types import *
from time import *
from widget import *

class TileboxBase(Widget):
    "Room with a (big) map"
    def __init__(self,xx,yy,relx,rely,ww,hh):
        Widget.__init__(self,xx,yy,ww,hh)
	self.tiles = []
#        self.relativex = xx
#        self.relativey = yy 
 
    def draw(self,screen):
	### adda tilebox frame picture here
	Widget.draw(self, screen)	

	for w in self.tiles:
		w.draw(screen)

    def addtile(self, t):
	self.tiles.append(t)

    def undomove(self):
        if self.direction == "north":
            self.movedown()
        elif self.direction == "south":
            self.moveup()
        elif self.direction == "west":
            self.moveright()
        elif self.direction == "east":
            self.moveleft()

    def moveup(self):
        self.direction = "north"
        self.relativey = self.relativey - 10

    def movedown(self):
        self.direction = "south"
        self.relativey = self.relativey + 10

    def moveleft(self):
        self.direction = "west"
        self.relativex = self.relativex - 10
	### print "relx=%d" % self.relativex
	
    def moveright(self):
	if self.relativex >= 0:
		self.moveleft()
        self.direction = "east"
        self.relativex = self.relativex + 10
