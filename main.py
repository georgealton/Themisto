if __name__ == '__main__':
  
  import logging
  logging.basicConfig(level=logging.INFO)
  logger = logging.getLogger(__name__)

  import player
  import characters
  import roles


  # p1Name = input('Player 1 Name : ')
  # p1Role = None
  # while not p1Role in ('G','D') :
  #   p1Role = input('Player 1 Role [G] or [D] : ')

  # p2Name = input('Player 2 Name : ')
  # p2Role = None
  # while not p2Role in ('G','D') :
  #   p2Role = input('Player 2 Role [G] or [D] : ')

  p1Name = "G"
  p2Name = "D"

  p1 = player.Player(p1Name, roles.GrandWizard)
  p2 = player.Player(p2Name, roles.DarkLord)

  p1.addCardToDeck(characters.Paladin())
  p2.addCardToDeck(characters.Goblin())

  battle = p1.startBattle(p2)