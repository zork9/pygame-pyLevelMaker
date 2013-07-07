
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

class Tilesheetbox(TileboxBase):
    ""
    def __init__(self,xx,yy,relx,rely,ww,hh):
        TileboxBase.__init__(self,xx,yy,relx,rely,ww,hh)
	self.tilew = 16
	self.tileh = 16

	self.surfacesw = 10
	self.surfacesh = 10
	self.surfaces = []
	for y in range(0,self.surfacesh):
		for x in range(0,self.surfacesw):
			### surface = pygame.Surface((self.tilew,self.tileh))
			### self.surfaces.append(surface)
			self.surfaces.append(None)

        self.tilesimage = pygame.image.load("./pics/tilesheet1.bmp").convert()
	self.splitintosurfaces()

	### FIX surface.get_bounding_rect
    def splitintosurfaces(self):
	pxarray = pygame.PixelArray(self.tilesimage)
	surfacepxarray = pygame.PixelArray(pygame.Surface((self.tilew,self.tileh))) 

	xoff = 0
	yoff = 0

	for y in range(0,self.surfacesh):
		for x in range(0,self.surfacesw):
			surface = pygame.Surface((self.tilew,self.tileh))
			for i in range(0,self.tileh):
				for j in range(0,self.tilew):
					surfacepxarray[j,i] = pxarray[j,i]

			self.surfaces[y*self.surfacesw+x] = surfacepxarray 
			###surfacepxarray = []
			yoff += self.tileh
		xoff += self.tilew


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
