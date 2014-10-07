class actionType(object):
  def __init__(self):
    self.name = self.__class__.__name__

class melee(actionType):
  pass

class magic(actionType):
  pass

class projectile(actionType):
  pass

class splash(actionType):
  pass



class action(object):
  def __init__(self):
    self.actiontype = ''

  def run(self):
    pass


class attack(action):
  pass

class defend(action):
  pass

class item(action):
  pass

class skip(action):
  pass

class cast(action):
  pass



class block(defend):
  def __init__(self):
    self.actiontype = melee()

class shield(defend):
  def __init__(self):
    self.actiontype = melee()

class barrier(defend):
  def __init__(self):
    self.actiontype = magic()

class wall(defend):
  def __init__(self):
    self.actiontype = magic()