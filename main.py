from random import *


class Uebische:
  def __init__(self, name):
    self.name = name
    self.gladness = 50
    self.stimulus = 0
    self.hp = 10
    self.alive = True
  def sleep(self):
    print('Sleep time')
    self.gladness -= 3
    self.hp += 0,5
    self.stimulus -= 50
  def chill(self):
    print('Cheel time')
    self.gladness += 10000
    self.hp -= 0,5
    self.stimulus += 100
  def is_alive(self):
    if self.gladness <= 0:
      print('Depression...')
      self.alive = False
    elif self.hp <= 0:
      print('you died!')
      self.alive = False
    elif self.stimulus <= 0:
      print('you do not Interest!')
      self.alive = True
    elif self.stimulus >= 500:
      print('you died!')
      self.alive = False
  def end(self):
    print ('Gladness',self.gladness)
    print ('Hp',self.hp)
    print ('Stimulus',self.stimulus)

  def live(self, day):
    print('Day', day)
    live_cube = randint(1,2)
    if live_cube == 1:
      self.sleep()
    elif live_cube == 2:
      self.chill()
    self.end()
    self.is_alive()

obj = Uebische('Uebische')
for day in range(30):
  if obj.alive == False:
    break
  obj.live(day)