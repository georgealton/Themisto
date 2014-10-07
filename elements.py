
class element(object):
  def getType(self):
      return self.name

class fire(element):
  def __init__(self):
    self.name = "fire"
    
class ice(element):
  def __init__(self):
    self.name = "ice"
    
class shock(element):
  def __init__(self):
    self.name = "shock"
    
class wind(element):
  def __init__(self):
    self.name = "wind"
    
    