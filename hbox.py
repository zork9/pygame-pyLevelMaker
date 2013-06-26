
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

class hbox(Widget):
    ""
    def __init__(self,xx,yy,relx,rely,ww,hh,imgfilename):
        Widget.__init__(self,xx,yy,ww,hh)
        self.bgimage = pygame.image.load(imgfilename).convert()
	self.bgoffsetx = 20 
	self.bgoffsety = 20 

    def draw(self,screen):
	### adda box frame picture here
        screen.blit(self.bgimage, (self.x, self.y))
	Widget.draw(self, screen)	

	for w in self.list:
		w.draw(screen)

    def doclick(self):
	1

    def dounclick(self):
	1
