import pygame
import random
import math
from pygame.locals import *
import pygame_gui

state_coi=1
class BLV():
	def __init__(self):
		self.hos=[]
		self.hos.append(pygame.mixer.Sound('vao.wav'))
		self.hos.append(pygame.mixer.Sound('kovao.wav'))
		self.hos.append(pygame.mixer.Sound('coi.wav'))
		self.hos.append(pygame.mixer.Sound('cham.wav'))
		self.ho=self.hos[0]
	def vao(self):
		start_time=3000#(s)
		end_time=15000
		self.ho=self.hos[0]
		self.ho.play(maxtime=end_time - start_time, fade_ms=start_time)
	def kovao(self):
		start_time=17000#(s)
		end_time=20000
		self.ho=self.hos[1]
		self.ho.play(maxtime=end_time - start_time, fade_ms=start_time)
	def coi(self):
		self.ho=self.hos[2]
		self.ho.play()
	def cham(self):
		self.ho=self.hos[3]
		self.ho.play()
	def stop(self):
		self.ho.stop()

		