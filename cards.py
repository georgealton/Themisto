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
    self.Cards[:] = [c for c in self.Cards if c.Alive]

  def __len__(self):
    return len(self.Cards)
  def __str__(self):
    return 'Deck: ' + str(self.Cards)

class Status(object):
  def __init__(self):
    self.Alive = True
    self.Sleep = False
    self.Poison = False
    self.Blind = False
    self.Frozen = False

class CardActions(object):

  def onAttack(self, target):
    target.onAttacked(self, target)

  def onAttacked(self, source, target):
    hit = -random.randint(0,9)

    if(hit == 0 ):
      logging.info(source.Name + ' Misses ' + target.Name + '!!')
      return

    logging.info(source.Name + ' Hits ' + target.Name + ' For ' + str(hit) + ' HP')
    if target.HitPoints + hit <= 0 :
      target.onDeath(source)
    else : 
      target.HitPoints += hit

  def onDeath(self, source):
    self.HitPoints = 0
    self.status.Alive = False
    logging.info(self.Name + ' Is Banished!')


  def onDefend(self):
    raise NotImplementedError()

  def speak(self):
    logging.info(self.name)


class Card(CardActions, object):

  def __init__(self, hp=1, mp=1, map=1, mdp=1, mgap=1, mgdp=1, name='default_card', level=1):
    self.hitPoints = hp
    self.currentHP = self.hitPoints
    self.magicPoints = mp
    self.currentMP = self.magicPoints
    self.meleeAttack = ap
    self.meleeDefence = dp
    self.magicAttack = mgap
    self.magicDefence = mgdp
    self.name = name
    self.level = level

    self.Stance = "Neutral"
    
    #When a Card is created set the value of it's Statuses 
    self.status = Status()
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
    return self.level
  @level.setter
  def level(self, level):
    self._level = int(i)

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

  


  def attack(self, target):
    self.onAttack(target)

  def isDead(self):
    return not self.status.Alive

  def getActions(self):
    pass




  def __str__(self):
    return self.name

  def __repr__(self):
    return 'Level: ' + self.level + ' Name: ' + self.name + ' HP: ' + str(self.hitPoints)