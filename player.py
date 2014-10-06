import logging 

import battle
import characters
import cards

class Player(object):

  def __init__(self, name, role):
    logging.info('New Player ' + role.Name +  " " + name)
    self.Name = name
    self.Deck = cards.Deck()
    self.Coins = []
    self.ManaPool = []
    self.Role = role


  def startBattle(self, target_player):
    return battle.Battle(self, target_player)

  def summon(self, character):
    logging.info('You Want to Summon a ' + character)

  def cast(self, spell, target):
    logging.info(self.Name + ' Casting ' + spell + ' at ' + str(target))

  def attack(self, cardid, target_player, target_cardid):
    self.Deck.passActionToCard('attack', self.getDeck().getCardById(cardid), target_player, target_cardid)


  def getDeck(self):
    return self.Deck

  def __str__(self):
    return self.Name

  def title(self):
    return self.Role.Name + ' ' + self.Name

  def holdsCards(self):
    return bool(len(self.getDeck()))

  def getTitleAndDeck(self):
    return self.title() + ' ' + str(self.getDeck())

  def addCardToDeck(self, card):
    if isinstance(card, cards.Card):
      self.getDeck().addCard(card)

class Purse(object):
  def __init__(self):
    self.Coins = []