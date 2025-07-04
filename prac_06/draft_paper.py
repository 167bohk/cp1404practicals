# monsters = [["Mike", 340, "blue"], ["James", 14, "green"], ["Randall", 24, "purple"]]
# toothy_monsters = [monster for monster in monsters if monster[1] > 16]
# print(toothy_monsters)

# class Monster:
#     """"""
#     def __init__(self, name = "Mike", number_of_teeth = 0, colour = "blue"):
#         """Initialize a Monster. """
#         self.name = name
#         self.number_of_teeth = number_of_teeth
#         self.colour = colour
#     def __str__(self):
#         return f"{self.name} {self.number_of_teeth} {self.colour}"
#
#     def is_scary(self):
#         """Determine whether the Monster is scary. """
#         return self.colour == "red" or self.number_of_teeth > 16
#
#
# monster1 = Monster(name="Mike", number_of_teeth=340, colour="blue")
# monster2 = Monster(name="James", number_of_teeth=14, colour="green")
# monster3 = Monster(name="Randall", number_of_teeth=24, colour="purple")
# monsters = [monster1, monster2, monster3]
# scary_monsters = [monster.__str__() for monster in monsters if monster.is_scary()]
# print(scary_monsters)

#
# class User:
#     def __init__(self, name = "", number_of_tacos = 5, score = 0):
#         """Initialize User."""
#         self.name = name
#         self.number_of_tacos = number_of_tacos
#         self.score = score
#
#     def __str__(self):
#         """Return a User in string format."""
#         return f"{self.name}, {self.score} points, {self.number_of_tacos} tacos left"
#
#     def give_taco(self, other_user):
#         """Give a taco"""
#         if self.number_of_tacos > 0:
#             self.number_of_tacos -= 1
#             other_user.number_of_tacos += 1
#         else:
#             print(f"{self.name} has no taco to give.")
#
# user1 = User(name="Ben", number_of_tacos= 4, score= 2)
# user2 = User("Mike")
# print(user1)
# print(user2)
# user1.give_taco(user2)
# print(user1)
# print(user2)





