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
from rootwidget import *
from textbutton import *


class Game:
    "Main function"
    def __init__(self):
	self.screenwidth = 1024
	self.screenheight = 768
        pygame.init()
        pygame.font.init()
        screen = pygame.display.set_mode((self.screenwidth, self.screenheight))
        self.font = pygame.font.SysFont("Times", 14)


	self.tilew = 16
	self.tileh = 16
	self.selectedtile = None
	self.tileboxw = 300
	self.tilebox = Tilebox(self.screenwidth-self.tileboxw,768-600,self.tileboxw,0,self.tileboxw,self.screenheight)
	self.tilebox.addtile(Tile(0,0,0,0,self.tilew,self.tileh,3.1,"./pics/tile-tree-1-16x16.bmp"))
	self.tilebox.addtile(Tile(0,0,0,0,self.tilew,self.tileh,3.2,"./pics/tile-tree-2-16x16.bmp"))
	self.tilebox.addtile(Tile(0,0,0,0,self.tilew,self.tileh,3.3,"./pics/tile-tree-3-16x16.bmp"))
	self.tilebox.addtile(Tile(0,0,0,0,self.tilew,self.tileh,3.4,"./pics/tile-tree-4-16x16.bmp"))
	
	self.tilebox.sort()
	self.map = Map(0,0,0,0,1024,768)
	### self.rootwidget.add(self.map)
	### self.rootwidget.add(self.tilebox)
	self.rootwidget = RootWidget(0,0,0,0,self.screenwidth,self.screenheight)
	### FIX split args into procedures

	self.upbutton = TextButton(self.screenwidth - 280,0,0,0,16,16,"./pics/tile-tree-1-16x16.bmp","./pics/tile-tree-2-16x16.bmp",self.font,"Up")
	self.upbutton.connect(self.scrollup, None)	
	self.rootwidget.add(self.upbutton)

	self.downbutton = TextButton(self.screenwidth - 280 + 16,0,0,0,16,16,"./pics/tile-tree-1-16x16.bmp","./pics/tile-tree-2-16x16.bmp",self.font,"Down")
	self.downbutton.connect(self.scrolldown, None)	
	self.rootwidget.add(self.downbutton)

	self.leftbutton = TextButton(self.screenwidth - 280 + 16 + 16,0,0,0,16,16,"./pics/tile-tree-1-16x16.bmp","./pics/tile-tree-2-16x16.bmp",self.font,"Left")
	self.leftbutton.connect(self.scrollleft, None)	
	self.rootwidget.add(self.leftbutton)

	self.rightbutton = TextButton(self.screenwidth - 280 + 16 + 16 + 16,0,0,0,16,16,"./pics/tile-tree-1-16x16.bmp","./pics/tile-tree-2-16x16.bmp",self.font,"Right")
	self.rightbutton.connect(self.scrollright, None)	
	self.rootwidget.add(self.rightbutton)


        blankimage = pygame.image.load('./pics/blank.bmp').convert()
        ## There are several title screens in the ./pics/ directory
        self.x = 0
        self.y = 0
	self.prevselect = None 
	gameover = 0      
	self.prevpos0 = -1
	self.prevpos1 = -1 
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
				self.prevpos0 = pos[0]
				self.prevpos1 = pos[1]
				print "get_pos() = (%s,%s)" % (pos[0],pos[1])
				
				if pos[0] < self.tilebox.x and self.selectedtile:
					self.map.put(self.selectedtile,pos[0]-self.map.relativex,pos[1]-self.map.relativey)
					flag = 1
					print "selected tile !"
	
				if pos[0] > self.tilebox.x and pos[1] > self.tilebox.y:	
					self.selectedtile = self.tilebox.get(pos[0],pos[1])
				if pos[0] > self.tilebox.x and pos[1] < self.tilebox.y:
					self.rootwidget.click(pos[0],pos[1])
               		if event.type == pygame.MOUSEBUTTONUP:
				sleep(0.2)
				pos = pygame.mouse.get_pos()
				### unclick the previously clicked widget
				self.rootwidget.unclick(self.prevpos0,self.prevpos1)
				###self.rootwidget.unclick(pos[0],pos[1])
	
		self.map.draw(screen,self.tilebox)
		self.tilebox.draw(screen)
		self.rootwidget.draw(screen)
	       	pygame.display.update()

    def scrollup(self, args):
	print "Scroll up!"
        self.map.relativey -= 10

    def scrolldown(self, args):
	print "Scroll Down!"
        self.map.relativey += 10

    def scrollleft(self, args):
	print "Scroll left!"
        self.map.relativex -= 10

    def scrollright(self, args):
	print "Scroll right!"
        self.map.relativex += 10

				    
if __name__ == "__main__":
    foo = Game()



