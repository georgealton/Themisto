class Spell(object):
  Name = "Spell"
  ManaCost = 99999

class Heal(Spell, object):
  Name = "Heal"
  ManaCost = 1000

class Cataclysm(Spell, object):
  Name = "Heal"
  ManaCost = 1000