# from turtle import Turtle, Screen
# timmy = Turtle()
# timmy.color('coral')
# timmy.shape('turtle')
# my_screen = Screen()
# print(my_screen.canvheight)
#
# timmy.forward(1000)
# my_screen.exitonclick()
from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon",
                 ["Pikachu", "Charmander", "Squirtle", "Bulbasaur"])
table.add_column("Type",
                 ["Electric", "Fire", "Water", "Grass"])
table.align = "l"
print(table)
