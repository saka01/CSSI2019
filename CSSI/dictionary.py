# pet = {
#     "name" : "Skeemer",
#     "animal" : "Dog",
#     "breed" : "Bichon Frise",
#     "age" : 16,
# }
#
# print(pet["name"] + " has dissasociated himself from the Saka family yo.")
#
# pet["name"] = "Simba"
#
# print("and shall now be called " + pet["name"])
#
# pet["favourite"] = "milkbone"
#
# print(pet)
# pet.pop("age")
#
# print(pet)









# sakas_life = {
#     "name"  : "Saka",
#     "age" : 17,
#     "movies" : {
#         "name" : "Avengers End Game",
#         "rating" : "PG-13",
#
#     }
# }
#
# for i in sakas_life:
#     print("mested key is " + i)
#     print("nested value is " + str(sakas_life["movies"]["name"]


class Pet(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("Ruff ruff ruff")

my_pet = Pet("Finn", 14)
my_pet.bark()

print("My new pet is " + my_pet.name + " and he/she is " + str(my_pet.age))
