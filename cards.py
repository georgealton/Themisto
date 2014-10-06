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


class Card(CardActions, object):

  def __init__(self):
    self.HitPoints = 0
    self.MagicPoints = 0
    self.Attack = 0
    self.Defence = 0
    self.Name = "DefaultCharacter"
    self.Stance = "Neutral"
    self.Level = "1"

    #When a Card is created set the value of it's Statuses 
    self.status = Status()

  def speak(self):
    logging.info(self.Name)

  def attack(self, target):
    self.onAttack(target)

  def isDead(self):
    return self.status.Alive

  def __str__(self):
    return self.Name

  def __repr__(self):
    return 'Level: ' + self.Level + ' Name: ' + self.Name + ' HP: ' + str(self.HitPoints)