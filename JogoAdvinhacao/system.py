import random

class System:

  def __init__(self):
    self.__value_sort_system = random.randint(1, 20)
    self.__player = None

  def sort_number(self):
    print(
      f'\n {self.player.name}, Choose between 1 and 20')

    for c in range(1, 4):
      print(f"\n Number attempt {c}")
      sort = int(input("Type number: "))

      while sort > 20 or sort < 1:
        print(f"\n Bad idea, this number is not valid.")
        sort = int(input("Type number: "))
      self.player.value = sort

      if self.player.value < self.value_sort_system:
        print("\n Is cold...")

      if self.player.value > self.value_sort_system:
        print("\n Too hot, guess so hight...")

      if self.player.value == self.value_sort_system:
        break

    self.show_value(c)

  def show_value(self, guess):
    if self.player.value == self.value_sort_system:
      print(
        f"\n Congratulations! you win in {guess} Attempts"
      )

    else:
      print(
        f"\n Tou Lose. The number was: {self.value_sort_system}"
      )

  @property
  def value_sort_system(self):
    return self.__value_sort_system

  @property
  def player(self):
    return self.__player

  @player.setter
  def player(self, player):
    self.__player = player
