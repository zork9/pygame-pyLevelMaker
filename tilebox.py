
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
from tileboxbase import *

class Tilebox(TileboxBase):
    ""
    def __init__(self,xx,yy,relx,rely):
        TileboxBase.__init__(self,xx,yy,relx,rely)
	self.tilew = 16
	self.tileh = 16

    def sort(self):
	xx = self.x 
	yy = 0
	for w in self.tiles:
		w.x += xx  
		xx += self.tilew 

    def gettilefromid(self, id):
	for tile in self.tiles:
		if tile.id == id:
			return tile
	return None

    def getid(self,xx,yy):
	for tile in self.tiles:
		if xx > tile.x and xx < tile.x+self.tilew and yy > tile.y and yy < tile.y+self.tileh:
			print "tile.id = %s" % tile.id	
			return tile.id
		else:
			1 ### print "click tileboxx=%d tileboxy=%d tilex=%d tiley=%d" % (self.x,self.y,self.x+tile.x, self.y+tile.y)
				
    def get(self,xx,yy):
	for tile in self.tiles:
		if xx > tile.x and xx < tile.x+self.tilew and yy > tile.y and yy < tile.y+self.tileh:
			print "tile.id = %s" % tile.id	
			return tile
		else:
			print "click tileboxx=%d tileboxy=%d tilex=%d tiley=%d" % (self.x,self.y,self.x+tile.x, self.y+tile.y)
	return None

    def getimage(self, id):
	for tile in self.tiles:
		if tile.id == id:
			return tile.image
	return None
