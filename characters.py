import logging 

import cards
import stance

class Man(cards.Card, object):
  Stance = stance.Righteous()

class Paladin(Man, object):
  HitPoints = 50
  Name = "Paladin"
class Elf(Man, object):
  Name = "Elf"
class Dwarf(Man, object):
  Name = "Dwarf"
class Archer(Man, object):
  Name = "Archer"
class Priest(Man, object):
  Name = "Priest"




class Monster(cards.Card, object):
  Stance = stance.Corrupt()

class Undead(Monster, object):
  HitPoints = 10
  Name = "Undead"

class Goblin(Monster, object):
  HitPoints = 50
  MagicPoints = 10
  Attack = 10
  Defence = 10
  Name = "Goblin"

class Dragon(Monster, object):
  HitPoints = 1000
  MagicPoints = 1000
  Attack = 10
  Defence = 10
  Name = "Dragon"

class Succubus(Monster, object):
  Name = "Succubus"