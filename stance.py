class Stance(object):
  Spectrum = range(200)

class Righteous(Stance, object):
  Value = 200

class Corrupt(Stance, object):
  Value = 0

class Neutral(Stance, object):
  Value = 100