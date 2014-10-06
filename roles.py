import logging 

import stance

class PlayerRole(object):
  Stance = stance.Neutral()

class GrandWizard(PlayerRole, object):
  Name = "Grand Wizard"
  Stance = stance.Righteous()

class DarkLord(PlayerRole, object):
  Name = "Dark Lord"
  Stance = stance.Corrupt()