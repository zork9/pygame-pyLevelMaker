
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

class Map(Widget):
    "Room with a (big) map"
    def __init__(self,xx,yy,relx,rely,ww,hh):
        Widget.__init__(self,xx,yy,ww,hh)
	self.tiles = []
        self.relativex = relx
        self.relativey = rely
	self.w = ww
	self.h = hh
	### NOTE seperate in files 
	self.tilew = 16
	self.tileh = 16
	self.tiles = []

	### generate the empty tables
	self.generateemptytilelist()

        self.background = pygame.image.load('./pics/blank.bmp').convert()

    def put(self, tile, xx, yy):
	self.tiles[yy /self.tileh][xx / self.tilew] = tile.id 
	print "configured a tile!"

 
    def draw(self,screen,tilebox):
        screen.blit(self.background, (0+self.relativex, 0+self.relativey))
	for yy in range(0, self.h / self.tileh): 
		for xx in range(0, self.w / self.tilew): 
        		t = tilebox.getimage(self.tiles[yy][xx])
        		if t:
				screen.blit(t, (xx*self.tilew+self.relativex, yy*self.tileh+self.relativey))
			
    def generateemptytilelist(self):
	for yy in range(0,self.h / self.tileh):
		l = []
		for xx in range(0,self.w / self.tilew):
			l.append(0)
		self.tiles.append(l)
	### print "tilelist=%s" % self.tiles

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
