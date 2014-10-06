import logging 

import cards
import stance
import actions

class Man(cards.Card, object):
  Stance = stance.Righteous()
  
  #Base modifiers (0 = immune, 1 = normal damage, 2 = double damage)
  #subclasses overwrite
  fireModifier = 1
  iceModifier = 1
  lightingModifier = 1
  bladeWeapons = 1
  bluntWeapons = 1
  projectileWeapons = 1

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
  #Base modifiers (0 = immune, 1 = normal damage, 2 = double damage)
  #subclasses overwrite
  fireModifier = 1
  iceModifier = 1
  lightingModifier = 1
  bladeWeapons = 1
  bluntWeapons = 1
  projectileWeapons = 1

class smallMonster(Monster, object):
    Size = 50
    Strength = 50

class humanoidMonster(Monster, object):
    Size = 100
    Strenght = 50
  
class beastMonster(Monster, object):
    Size = 150
    Strenth = 150
    
class Dragon(Monster, object):
    Size = 300
    Strength = 400
    fireModifier = 0

class Undead(humanoidMonster, object):
  HitPoints = 10
  Name = "Undead"

class Goblin(smallMonster, object):
  HitPoints = 50
  MagicPoints = 10
  Attack = 10
  Defence = 10
  Name = "Goblin"

class commonDragon(Dragon, object):
  HitPoints = 1000
  MagicPoints = 1000
  Attack = 10
  Defence = 10
  Name = "Dragon"

class Succubus(Monster, object):
  Name = "Succubus"