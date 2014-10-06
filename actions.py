class actionType(object):
  def __init__(self):
    self.name = self.__class__.__name__

class melee(actionType, object):
  pass

class magic(actionType, object):
  pass

class projectile(actionType, object):
  pass

class splash(actionType, object):
  pass



class action(object):
  def __init__(self):
    self.actiontype = ''

  def run(self):
    pass


class attack(action, object):
  pass

class defend(action, object):
  pass

class item(action, object):
  pass

class skip(action, object):
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