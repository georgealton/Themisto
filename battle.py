import logging 

class Battle(object):
  def __init__(self, sourcePlayer, targetPlayer):
    self.players = [sourcePlayer, targetPlayer]

    self.turns = Turns(self.players)
    self.requestBattle()
    

  def requestBattle(self):
    logging.info('%s Wants to Battle %s', self.players[1].title(), self.players[0].title())
    self.start()


  def start(self):
    while(self.players[0].holdsCards() and self.players[1].holdsCards()):
      self.turns.runTurns()

    self.end()
    
  def end(self):
    logging.info("Battled Ended")



class Turns(object):
  def __init__(self, players):
    self.turnIndex = 0
    self.unturnIndex = 1

    self.players = players

    self.turnedPlayer = self.players[self.turnIndex]
    self.unturnedPlayer = self.players[not self.turnIndex]

  def requestAction(self):
    action = ''
    while not hasattr(self.turnedPlayer, action): 
      action = input('Input Action : ')
      
      if action == '' :
        action = 'skip'
        return action
        
      if not hasattr(self.turnedPlayer, action):
        logging.info(action + ' Not Permitted')

    return action 

  def runTurns(self):

    for p in self.players:
      logging.debug(p.getTitleAndDeck())
    
    action = self.requestAction()

    if action != 'skip':
      if hasattr(self.turnedPlayer, action):
        getattr(self.turnedPlayer, action)(0, self.unturnedPlayer, 0)
    else :
      logging.info('Skipping Turn')
    if not self.unturnedPlayer.holdsCards():
      logging.info(self.unturnedPlayer.title() + ' Holds No Cards!')
    else :
      self.switchTurn()

  def switchTurn(self):
    logging.debug("Switching Turns")
    self.turnIndex = int(not self.turnIndex)
    self.unturnIndex = int(not self.unturnIndex)

    self.turnedPlayer = self.players[self.turnIndex]
    self.unturnedPlayer = self.players[self.unturnIndex]