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
    self.Alive = False
    logging.info(self.Name + ' Is Banished!')


  def onDefend(self):
    raise NotImplementedError()


class Card(CardActions, object):

  HitPoints = 0
  MagicPoints = 0
  Attack = 0
  Defence = 0
  Name = "DefaultCharacter"
  Stance = "Neutral"
  Level = "1"

  Alive = True

  Sleep = False
  Poison = False
  Blind = False
  Frozen = False

  def speak(self):
    logging.info(self.Name)

  def attack(self, target):
    self.onAttack(target)

  def isDead(self):
    return self.Alive

  def __str__(self):
    return self.Name

  def __repr__(self):
    return 'Level: ' + self.Level + ' Name: ' + self.Name + ' HP: ' + str(self.HitPoints)