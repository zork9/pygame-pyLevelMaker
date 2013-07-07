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
from buttonbox import *
from tilebox import *
from tilesheetbox import *
from tile import *
from hbox import *
from rootwidget import *
from textbutton import *
from config import *

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
	self.tilesheetbox = Tilesheetbox(self.screenwidth-self.tileboxw,768-300,self.tileboxw,0,self.tileboxw,self.screenheight)
	self.buttonbox = hbox(self.screenwidth-self.tileboxw,0,0,0,150,300,"./pics/levelmaker-border-2-150x300.bmp")
	self.tilebox.addtile(Tile(0,0,0,0,self.tilew,self.tileh,3.1,"./pics/tile-tree-1-16x16.bmp"))
	self.tilebox.addtile(Tile(0,0,0,0,self.tilew,self.tileh,3.2,"./pics/tile-tree-2-16x16.bmp"))
	self.tilebox.addtile(Tile(0,0,0,0,self.tilew,self.tileh,3.3,"./pics/tile-tree-3-16x16.bmp"))
	self.tilebox.addtile(Tile(0,0,0,0,self.tilew,self.tileh,3.4,"./pics/tile-tree-4-16x16.bmp"))
	self.tilebox.addtile(Tile(0,0,0,0,self.tilew,self.tileh,3.5,"./pics/tile-grass-1-16x16.bmp"))
	self.tilebox.addtile(Tile(0,0,0,0,self.tilew,self.tileh,3.6,"./pics/tile-grass-2-16x16.bmp"))
	self.tilebox.addtile(Tile(0,0,0,0,self.tilew,self.tileh,3.7,"./pics/tile-grass-3-16x16.bmp"))
	self.tilebox.addtile(Tile(0,0,0,0,self.tilew,self.tileh,3.8,"./pics/tile-grass-4-16x16.bmp"))
	### self.tilebox.addtile(Tile(0,0,0,0,self.tilew,self.tileh,3.9,"./pics/tile-grass-5-16x16.bmp"))
	### self.tilebox.addtile(Tile(0,0,0,0,self.tilew,self.tileh,3.10,"./pics/tile-grass-6-16x16.bmp"))
	self.tilebox.addtile(Tile(0,0,0,0,self.tilew,self.tileh,3.11,"./pics/tile-grass-7-16x16.bmp"))
	self.tilebox.addtile(Tile(0,0,0,0,self.tilew,self.tileh,3.12,"./pics/tile-grass-8-16x16.bmp"))
	self.tilebox.addtile(Tile(0,0,0,0,self.tilew,self.tileh,3.13,"./pics/tile-grass-9-16x16.bmp"))
	self.tilebox.addtile(Tile(0,0,0,0,self.tilew,self.tileh,3.14,"./pics/tile-grass-10-16x16.bmp"))
	self.tilebox.addtile(Tile(0,0,0,0,self.tilew,self.tileh,3.15,"./pics/tile-grass-11-16x16.bmp"))
	self.tilebox.addtile(Tile(0,0,0,0,self.tilew,self.tileh,3.16,"./pics/tile-border-1-16x16.bmp"))
	self.tilebox.addtile(Tile(0,0,0,0,self.tilew,self.tileh,3.17,"./pics/tile-border-2-16x16.bmp"))
	self.tilebox.addtile(Tile(0,0,0,0,self.tilew,self.tileh,3.18,"./pics/tile-border-3-16x16.bmp"))
	self.tilebox.addtile(Tile(0,0,0,0,self.tilew,self.tileh,3.19,"./pics/tile-border-4-16x16.bmp"))
	self.tilebox.addtile(Tile(0,0,0,0,self.tilew,self.tileh,3.20,"./pics/tile-border-5-16x16.bmp"))
	self.tilebox.addtile(Tile(0,0,0,0,self.tilew,self.tileh,3.21,"./pics/tile-border-6-16x16.bmp"))
	self.tilebox.addtile(Tile(0,0,0,0,self.tilew,self.tileh,3.22,"./pics/tile-border-7-16x16.bmp"))
	self.tilebox.addtile(Tile(0,0,0,0,self.tilew,self.tileh,3.23,"./pics/tile-border-8-16x16.bmp"))
	self.tilebox.addtile(Tile(0,0,0,0,self.tilew,self.tileh,3.24,"./pics/tile-border-9-16x16.bmp"))
	#############################
	# Minish Cap tiles
	#############################
	self.tilebox.addtile(Tile(0,0,0,0,self.tilew,self.tileh,3.25,"./pics/tile2-grass-1-16x16.bmp"))
	### FIX self.tilebox.sort()

        self.config = Config('./pylevelmaker-config') 

	self.map = Map(0,0,0,0,1024,768,self.config) ## NOTE default w and h
	### self.rootwidget.add(self.map)
	self.rootwidget = RootWidget(0,0,0,0,self.screenwidth,self.screenheight)
	self.rootwidget.add(self.buttonbox)

	### FIX split args into procedures

	self.upbutton = TextButton(self.screenwidth - self.tileboxw,0,0,0,64,32,"./pics/button-64x32.bmp","./pics/button-2-64x32.bmp",self.font,"Up")
	self.upbutton.connect(self.scrollup, None)	
	self.rootwidget.add(self.upbutton)

	self.downbutton = TextButton(64 + self.screenwidth - self.tileboxw ,0,0,0,64,32,"./pics/button-64x32.bmp","./pics/button-2-64x32.bmp",self.font,"Down")
	self.downbutton.connect(self.scrolldown, None)	
	self.rootwidget.add(self.downbutton)

	self.leftbutton = TextButton(128 + self.screenwidth - self.tileboxw  ,0,0,0,64,32,"./pics/button-64x32.bmp","./pics/button-2-64x32.bmp",self.font,"Left")
	self.leftbutton.connect(self.scrollleft, None)	
	self.rootwidget.add(self.leftbutton)

	self.rightbutton = TextButton(192 + self.screenwidth - self.tileboxw   ,0,0,0,64,32,"./pics/button-64x32.bmp","./pics/button-2-64x32.bmp",self.font,"Right")
	self.rightbutton.connect(self.scrollright, None)	
	self.rootwidget.add(self.rightbutton)

	self.printbutton = TextButton(256 + self.screenwidth - self.tileboxw    ,0,0,0,64,32,"./pics/button-64x32.bmp","./pics/button-2-64x32.bmp",self.font,"Print")
	self.printbutton.connect(self.printtoconsole, None)	
	self.rootwidget.add(self.printbutton)

	self.printtofilebutton = TextButton(0 + self.screenwidth - self.tileboxw    ,32,0,0,64,32,"./pics/button-64x32.bmp","./pics/button-2-64x32.bmp",self.font,"Fileout")
	self.printtofilebutton.connect(self.printtofile, None)	
	self.rootwidget.add(self.printtofilebutton)

	self.readinfilebutton = TextButton(64 + self.screenwidth - self.tileboxw    ,32,0,0,64,32,"./pics/button-64x32.bmp","./pics/button-2-64x32.bmp",self.font,"Filein")
	self.readinfilebutton.connect(self.readinfile, None)	
	self.rootwidget.add(self.readinfilebutton)

        blankimage = pygame.image.load('./pics/blank-1024x768.bmp').convert()
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
	
            	screen.blit(blankimage, (0,0))
		self.map.draw(screen,self.tilebox)
		self.tilebox.draw(screen)
		self.tilesheetbox.draw(screen)
		self.rootwidget.draw(screen)
	       	pygame.display.update()

    def printtoconsole(self, args):
	print "self.tilelist = "
	print self.map.tiles

    def printtofile(self, args):
	f = open("./output.map", 'w+')
	f.write(str(self.map.tiles))
	f.close()

    def readinfile(self, args):
	self.map.loadfromfile('./output.map')

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



