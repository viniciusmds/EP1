from FGAme import *
from math import *

world.add.margin(10)
world.gravity = 500
bullet = world.add.circle(20, pos=(50,50), color='red', damping = 0.015)
bullet.vel = (240, 700)

class Wind:

	def __init__(self, wind_spd=Vec(0,0)):
		self.wind_spd = wind_spd
	
	def wind_accel(self, wind_spd, r=1):
		if wind_spd == (0,0):
			pass
		else:
			Fx = (1/2)*wind_spd[0]*wind_spd[0]*r
			Fy = (1/2)*wind_spd[1]*wind_spd[1]*r
			ax = Fx/bullet.mass
			ay = Fy/bullet.mass
			if wind_spd[0]>0:
				if wind_spd[1]>0:
					bullet.vel += Vec(ax,ay)
				else:
					bullet.vel += Vec(ax,-ay)
			else:
				if wind_spd[1]>0:
					bullet.vel += Vec(-ax,ay)
				else:
					bullet.vel += Vec(-ax,-ay)

	def update(self):
		self.wind_accel(self.wind_spd)
				
vento = Wind(Vec(-50,0))

def update():
	vento.update()

run()
