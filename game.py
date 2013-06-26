#!/usr/local/bin/python
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

from map import *
from tilebox import *
from tile import *

class Game:
    "Main function"
    def __init__(self):
	self.screenwidth = 1024
	self.screenheight = 768
        pygame.init()
        pygame.font.init()
        screen = pygame.display.set_mode((self.screenwidth, self.screenheight))
        font = pygame.font.SysFont("Times", 14)

	self.selectedtile = None
	self.tileboxw = 300
	self.tilebox = Tilebox(self.screenwidth-self.tileboxw,0,self.tileboxw,0)
	self.tilebox.addtile(Tile(0,0,0,0,3.1,"./pics/tile-tree-1-16x16.bmp"))
	self.tilebox.addtile(Tile(0,0,0,0,3.2,"./pics/tile-tree-2-16x16.bmp"))
	self.tilebox.addtile(Tile(0,0,0,0,3.3,"./pics/tile-tree-3-16x16.bmp"))
	self.tilebox.addtile(Tile(0,0,0,0,3.4,"./pics/tile-tree-4-16x16.bmp"))

	self.map = Map(0,0,0,0,1024,768)
	self.tilebox.sort()

        blankimage = pygame.image.load('./pics/blank.bmp').convert()
        ## There are several title screens in the ./pics/ directory
        self.x = 0
        self.y = 0
	self.prevselect = None 
	gameover = 0       
        while gameover == 0:
		flag = 0
		self.prev = None
            	screen.blit(blankimage, (0,0))
        	for event in pygame.event.get():
               		if event.type == QUIT:
               			return
               		elif event.type == KEYDOWN:
               			gameover = 1
				return
               		if event.type == pygame.MOUSEBUTTONDOWN:
				pos = pygame.mouse.get_pos()
				print "get_pos() = (%s,%s)" % (pos[0],pos[1])
				
				if pos[0] < self.tilebox.x and self.selectedtile:
					self.map.put(self.selectedtile,pos[0],pos[1])
					flag = 1
					print "selected tile !"
	
				if pos[0] > self.tilebox.x:	
					self.selectedtile = self.tilebox.get(pos[0],pos[1])
	
		self.map.draw(screen,self.tilebox)
		self.tilebox.draw(screen)
	       	pygame.display.update()
				    
if __name__ == "__main__":
    foo = Game()



