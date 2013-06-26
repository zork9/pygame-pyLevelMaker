
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
from button import *

class TextButton(Button):
    ""
    def __init__(self,xx,yy,relx,rely,ww,hh,upfilename,downfilename,font,text):
        Button.__init__(self,xx,yy,relx,rely,ww,hh,upfilename,downfilename)
        self.upimage = pygame.image.load(upfilename).convert()
        self.downimage = pygame.image.load(downfilename).convert()
	self.image = self.upimage
	self.text = text
	self.font = font 
 
    def draw(self,screen):
	Button.draw(self, screen)
	## FIX centering text
	screen.blit(self.font.render(self.text, 8, (255,255,255)), (self.x,self.y))

	Widget.draw(self,screen)

    def doclick(self):
	Button.doclick(self)

    def dounclick(self):
	Button.dounclick(self)


