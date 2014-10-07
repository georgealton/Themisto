import random

#Action Types
class actionType(object):
  def __init__(self):
    self.name = self.__class__.__name__



class melee(actionType):
    pass

class magic(actionType):
    pass

class projectile(actionType):
    pass

class splash(actionType):
    pass


#Action Super Classes
class action(object):
  def __init__(self):
    self.actiontype = ''
    self.successChance = ''

  def run(self):
    pass

  def __successChance__(self):
    if random.random() < self.successChance:
      return True
    else:
      return False


class attack(action):
    
  def __init__(self):
    self.successChance = 0.98
    self.attackModifier = 1

  def calcDamage(self, cardStrength, targetResist, cardWeaponQuality):
    randomMod = random.uniform(0,0.4)
    rawDamage = self.modifier * self.weaponQuality * cardStrength * cardWeaponQuality * randomMod
    resistedDamage = rawDamage * targetResist
    return resistedDamage


class defend(action):
  # removed self for now!
  successChance = 0.98

class item(action):
  pass

class skip(action):
  pass

class cast(action):
  pass


#Actions
class block(defend):
  def __init__(self):
    self.actiontype = melee()

class shield(defend):
  def __init__(self):
    self.actiontype = melee()

class barrier(defend):
  def __init__(self):
    self.actiontype = magic()

class wall(defend):
  def __init__(self):
    self.actiontype = magic()

class criticalShot(attack):
  #More damage, less likely to succeed
  def __init__(self):
    attack.__init__(self)
    self.successChance = 0.5
    self.attackModifier = 2
    