class Pokemon:
    def __init__(self, number, name, type1, type2, hp, attack, defense, spcattack, spcdefense, speed, generation, legendary, mega):
        self.number = int(number)
        self.name = str(name)
        self.type1 = str(type1)
        self.type2 = str(type2)
        self.hp = int(hp)
        self.attack = int(attack)
        self.defense = int(defense)
        self.spcattack = int(spcattack)
        self.spcdefense = int(spcdefense)
        self.speed = int(speed)
        self.generation = int(generation)
        self.legendary = bool(legendary.lower())
        self.mega = bool(mega.lower())

        def total_power(self):
            total_power = sum([self.hp, self.attack, self.defense, self.spcattack, self.spcdefense, self.speed])
            return total_power

def read_data():

    pokemon = {}

    with open('../resource/lib/public/pokedex.csv', 'r') as file:
        next(file)
        for line in file:
            clean_line = line.strip()
            line_data = clean_line.split(',')
            pokemon_id = int(line_data[0])
            if pokemon_id in pokemon:
                id_ = max(list(pokemon.keys()))+1
                pokemon[id_] = Pokemon(id_,line_data[1],line_data[2],line_data[3],line_data[4], line_data[5]
                                          ,line_data[6],line_data[7],line_data[8],line_data[9],line_data[10],line_data[11],
                                          line_data[12])
            else:
                pokemon[pokemon_id] = Pokemon(line_data[0], line_data[1], line_data[2], line_data[3], line_data[4],
                                       line_data[5],line_data[6], line_data[7], line_data[8], line_data[9], line_data[10],
                                       line_data[11],line_data[12])
    pokemon_type = {}

    for pokemon_id in pokemon:
        if pokemon[pokemon_id].legendary is True:
            if pokemon[pokemon_id].type1 in pokemon_type:
                pokemon_type[pokemon[pokemon_id].type1] += 1
            else:
                pokemon_type[pokemon[pokemon_id].type1] = 0
                pokemon_type[pokemon[pokemon_id].type1] += 1
            if pokemon[pokemon_id].type2 in pokemon_type:
                pokemon_type[pokemon[pokemon_id].type2] += 1
            else:
                pokemon_type[pokemon[pokemon_id].type2] = 0
                pokemon_type[pokemon[pokemon_id].type2] += 1

    print(poke)
# Among Legendary Pokemon, what is the most common type? Include both Type1 and Type2 in your count.



# Excluding Pokemon that are either Mega or Legendary, what Pokemon has the highest Defense statistic?
#     pokemon_name = None
#     pokemon_def = 0
#
#     for pokemon_id in pokemon:
#         if pokemon[pokemon_id].legendary is not True:
#             continue
#         elif pokemon[pokemon_id].mega is not True:
#             continue
#         else:
#             if pokemon[pokemon_id].defense > pokemon_def:
#                 pokemon_def = pokemon[pokemon_id].defense
#                 pokemon_name = pokemon[pokemon_id].name
#     return pokemon_name



    # What Pokemon has the highest HP statistic?

    # pokemon_name = None
    # pokemon_hp = 0
    #
    # for pokemon_id in pokemon:
    #     if pokemon[pokemon_id].hp > pokemon_hp:
    #         pokemon_hp = int(pokemon[pokemon_id].hp)
    #         pokemon_name = pokemon[pokemon_id].name
    #
    # return pokemon_name

    # What is the most common type? Include both Type1 and Type2 in your count.

    # pokemon_type_count ={}
    #
    # for pokemon_id in pokemon:
    #     if pokemon[pokemon_id].type1 not in pokemon_type_count:
    #         pokemon_type_count[pokemon[pokemon_id].type1] = 0
    #         pokemon_type_count[pokemon[pokemon_id].type1] += 1
    #     else:
    #         pokemon_type_count[pokemon[pokemon_id].type1] += 1
    #     if pokemon[pokemon_id].type2 not in pokemon_type_count:
    #         pokemon_type_count[pokemon[pokemon_id].type2] = 0
    #         pokemon_type_count[pokemon[pokemon_id].type2] += 1
    #     else:
    #         pokemon_type_count[pokemon[pokemon_id].type2] += 1

    # most_common = 0
    # most_common_type = None
    #
    # for type in pokemon_type_count:
    #     if len(type) > 1: # Filter out blank type
    #         if pokemon_type_count[type] > most_common:
    #             most_common = pokemon_type_count[type]
    #             most_common_type = type
    #
    # return most_common_type




    # How many Pokemon have only one type? In other words, for how many Pokemon is Type2 blank?
    # one_type = 0
    # for pokemon_id in pokemon:
    #     if len(pokemon[pokemon_id].type2) == 0:
    #         one_type += 1
    # return one_type




print(type(bool('TRUE')))