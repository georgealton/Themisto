import logging 
import random

class Deck(object):
  def __init__(self):
    self.Cards = []

  def addCard(self, card):
    if isinstance(card, Card):
      self.Cards.append(card)

  def getCardById(self, id):
    return self.Cards[id]

  def passActionToCard(self, action, card, target_player, target_cardid):

    if hasattr(card, action):
      getattr(card, action)(target_player.getDeck().getCardById(target_cardid))

    self.refreshDeck()
    target_player.getDeck().refreshDeck()

  def refreshDeck(self):
    self.Cards[:] = [c for c in self.Cards if c.status.alive]

  def __len__(self):
    return len(self.Cards)
  def __str__(self):
    return 'Deck: ' + str(self.Cards)

class Status(object):
  def __init__(self):
    self._alive = True
    self.Sleep = False
    self.Poison = False
    self.Blind = False
    self.Frozen = False
  
  @property
  def alive(self):
    return self._alive
  @alive.setter
  def alive(self, value):
    if self.alive != value : 
      self._alive = value
  
# a mixin for cards to handle events 
class CardActions(object):

  def onAttack(self, t):
    t.onAttacked(self, t)

  def onAttacked(self, s, t):
    hit = -random.randint(0,9)

    if(hit == 0 ):
      s.onMiss(self, t)
      return

    logging.info(s.name + ' Damages ' + t.name + ' For ' + str(hit) + ' HP')
    if t.currentHP + hit <= 0 :
      t.onDeath(s)
    else : 
      t.currentHP += hit

  def onDeath(self, source):
    # set the HP to 0 so that it doesn't go negative, and the alive status to false
    self.currentHP = 0
    self.status.alive = False


    logging.info(self.name + ' Is Dead!')

  def defend(self):
    pass

  def onDefend(self):
    pass

  def onAbsorb(self):
    pass

  def onReflect(self):
    pass

  def onSplash(self):
    pass

  def onBuff(self):
    pass

  def onDebuff(self):
    pass

  def onMiss(self, s, t):
    logging.info(self.name + ' Misses ' + t.name + '!!')

  def onElemental(self, t):
    pass

  def speak(self):
    logging.info(self.name)


class CardBaseValues(object):
  pass

class Card(CardBaseValues, CardActions, object):

  # default init method for all cards
  # do not overwrite!
  def __init__(self, hp=1, mp=1, ap=1, dp=1, maap=1, madp=1, n='default_card', l=1):
    self._hitPoints = hp
    self._magicPoints = mp

    # on init set the cards current hp/mp to be full
    self._currentHP = self.hitPoints
    self._currentMP = self.magicPoints
    
    self._meleeAttack = ap
    self._meleeDefence = dp
    
    self._magicAttack = maap
    self._magicDefence = madp



    self._name = n
    self._level = l

    self.Stance = "Neutral"
    
    #When a Card is created set the value of it's Statuses to be clear
    self.status = Status()

    # define the actions that a card can do
    self.actions = ()

  @property
  def hitPoints(self):
    return self._hitPoints
  @hitPoints.setter
  def hitPoints(self, hp):
    self._hitPoints = int(hp)

  @property
  def magicPoints(self):
    return self._magicPoints
  @magicPoints.setter
  def magicPoints(self, value):
    self._magicPoints = int(value)
  
  @property
  def meleeAttack(self):
    return self._meleeAttack
  @meleeAttack.setter
  def meleeAttack(self, value):
    self._meleeAttack = int(value)
  
  @property
  def meleeDefence(self):
    return self._meleeDefence
  @meleeDefence.setter
  def meleeDefence(self, value):
    self._meleeDefence = int(value)
  
  @property
  def level(self):
    return self._level
  @level.setter
  def level(self, value):
    self._level = int(value)

  @property
  def name(self):
    return self._name
  @name.setter
  def name(self, value):
    self._name = str(value)
  
  @property
  def magicAttack(self):
    return self._magicAttack
  @magicAttack.setter
  def magicAttack(self, value):
    self._magicAttack = int(value)

  @property
  def magicDefense(self):
    return self._magicDefense
  @magicDefense.setter
  def magicDefense(self, value):
    self._magicDefense = int(value)

  @property
  def currentHP(self):
    return self._currentHP
  @currentHP.setter
  def currentHP(self, value):
    self._currentHP = value

  @property
  def currentMP(self):
      return self._currentMP
  @currentMP.setter
  def currentMP(self, value):
      self._currentMP = value
  

  
  def executeAction(self, action, target):
    pass

  def attack(self, target):
    self.onAttack(target)

  def isDead(self):
    return not self.status.alive

  def getActions(self):
    pass




  def __str__(self):
    return self.name

  def __repr__(self):
    return 'Level: ' + str(self.level) + ' Name: ' + self.name + ' HP: ' + str(self.currentHP) + '/' + str(self.hitPoints)