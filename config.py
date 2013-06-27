
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

class Config:
    ""
    def __init__(self,filename):
	self.filename = filename
	self.buffer = ""

	self.mapwidth = 1024
	self.mapheight = 768

	self.load()
	
    def load(self):
	f = open(self.filename, 'r')
 	self.buffer = f.read()	
	self.parsefile()
	f.close()

    def parsefile(self):
	wordsonline = []
	if self.buffer:
		i = 0 
		j = 0 
		x = 0 
		for c in self.buffer:
			if c == ' ' or c == '\n':
				x = j
				j = i
				wordsonline.append(self.getword(x,j))
			i += 1
		self.put(wordsonline)	

    def getword(self, i,j):
	return self.buffer[i:j]

    def put(self, wordsonline):
	print "words=%s" % wordsonline
	for n in range(0, len(wordsonline)):
		print "n=%d" % n
		if wordsonline[n] == "mapwidth":
			self.mapwidth = int(wordsonline[n+1])	
			print "Configged mapwidth at : %d" % self.mapwidth	
		elif wordsonline[n] == "mapheight":
			self.mapheight = int(wordsonline[n+1])	
			print "Configged mapheight at : %d" % self.mapheight
