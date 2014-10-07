import random
import elements

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

  def calculateDamage(self, cardPower, targetResWeak, targetWeakness, equipmentQuality):
    #cardPower         : Physical/Magical power
    #targetResWeak     : targetCard resist/weak, dictionary, e.g. "Fire" : 1 (neutral) 2 (double damage)
    #                  0 (immune) -1 (absorbs)
    #Equipment         : Weapon or magic boosting gear
    
    randomMod = random.uniform(0,0.4)
    rawDamage = self.attackModifier * cardPower * equipmentQuality * randomMod
    
    if self.elementType.getType() in targetResWeak:
        adjustedDamage = rawDamage * targetResWeak[self.elementType.getType()]
        return adjustedDamage
    
    
    


class defend(action):
  def __init__(self):
    self.successChance = 0.98
    
  def calculateDefenceBoost(self, currentDefence):
    randomMod = random.uniform(0,0.2)
    boost = randomMod + currentDefence + 0.15
    return boost
      

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
    self.actiontype = melee()
    self.successChance = 0.5
    self.attackModifier = 2
    
class dragonBreathFire(attack):
  def __init__(self):
    self.actiontype = magic()
    self.elementType = fire()
    
#Test section
a = dragonBreathFire()
    