# # import turtle
# from turtle import Turtle, Screen
#
# timmy = Turtle()
# # Turtle here is the class
# print(timmy)
# # tell us where the turtle object is located in the memory
#
# timmy.shape('turtle')
# # changes the object shape on the centre of the screen
#
# timmy.color('DarkSlateBlue')
# # changes the color of the turtle.
#
# timmy.fd(100)
# # moves turtle 100 spaces forward we can use fd or forward().
# timmy.forward(100)
# my_screen = Screen()
#
# print(my_screen.canvheight)
# # canvheight is attribute of Screen
#
# my_screen.exitonclick()
# # previously the screen poped up for a brief but now the screen will exit only when we click on it.


from prettytable import PrettyTable

table = PrettyTable()
# prettytable is a module installed.
#print(table)
table.add_column("Pokemon name",['Pikachu','Squirtle','Charmander'])
#print(table)
# add columns adds column to the table one column at a time.
table.add_column("Type", ['Electric','Water',"Fire"])
table.align = 'l'
# align here is an attribute that is changing the alignment from centre to left.
print(table)
