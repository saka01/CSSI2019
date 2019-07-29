class Pokemon(object):
    #Constructor
    def __init__(self, name, type, sex):
        self.name = name
        self.type = type
        self.sex = sex

    def attack(self, move):
        print("my name is " + self.name + " and my move is " + move + " and i am a " + self.sex)

my_pokemon = Pokemon("Pikachu", "electric", "Male")
my_pokemon.attack("judo chop")
print(my_pokemon.sex)

class Pikachu(object):
    def __init__(self, name, type, sex, current, voltage):
        super(Pikachu, self).__init__()
        self.arg = arg


class Charrrrrrizardddd(Pokemon):
    def __init__(self, name, type, sex, tail_flame_size):
        Pokemon.__init__(self, name, type, sex)
        self.tail_flame_size = tail_flame_size

    def burntheguy(self):
        print("$$$$$")

Charizard = Charrrrrrizardddd("Charry", "flame-fly", "F", "Large" )
print(Charizard.tail_flame_size)

Charizard.attack("burn")
Charizard.burntheguy()
