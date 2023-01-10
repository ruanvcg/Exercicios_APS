
class Player:

  def __init__(self, name):
    self.__name = name
    self.__value = None

  @property
  def name(self):
    return self.__name

  @name.setter
  def name(self, name):
    self.__name = name

  @property
  def value(self):
    return self.__value

  @value.setter
  def value(self, value):
    self.__value = value