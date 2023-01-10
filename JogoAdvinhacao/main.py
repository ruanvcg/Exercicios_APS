from player import Player
from system import System

name = str(input("Type the name of player: "))
system = System()

system.player = Player(name)

system.sort_number()