
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
from time import *
from types import *

class WidgetChildren:
	""
	def __init__(self):
		self.list = []

	def add(self, c):
		self.list.append(c)	

	def remove(self,c):
		self.list.remove(c)

class Widget(WidgetChildren): 
    ""
    def __init__(self,xx,yy):
	WidgetChildren.__init__(self)
    	self.x = xx
	self.y = yy

    def draw(self,screen):
	for w in self.list:
		w.draw(screen) 
