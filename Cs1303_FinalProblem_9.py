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
        self.legendary = self.bool_test(legendary)
        self.mega = self.bool_test(mega)

    def bool_test(self, var):
        if var == 'TRUE':
            return True
        else:
            return False
    def total_power(self):
        total_power = sum([self.hp, self.attack, self.defense, self.spcattack, self.spcdefense, self.speed])
        return total_power



def read_data():

    pokemon = {}
    pokemon_id = 0
    with open('../resource/lib/public/pokedex.csv', 'r') as file:
        next(file)
        for line in file:
            clean_line = line.strip()
            line_data = clean_line.split(',')
            pokemon_id += 1
            pokemon[pokemon_id] = Pokemon(line_data[0], line_data[1], line_data[2], line_data[3], line_data[4],
                                       line_data[5],line_data[6], line_data[7], line_data[8], line_data[9], line_data[10],
                                       line_data[11],line_data[12])


    # Rounded to the nearest integer,
    # how much higher is the average sum of all six stats
    # among Mega Pokemon than their non-Mega versions?
    # Note that Mega Pokemon share the same Number (the first column) as their non-Mega versions,
    # which will allow you to find all Pokemon that have a Mega version.


    mega_numbers = []

    for pokemon_id in pokemon:
        pokemon_num = pokemon[pokemon_id].number
        if pokemon[pokemon_id].mega:
            mega_numbers.append(pokemon_num)

    pokemon_numbers_with_mega = list(set(mega_numbers))

    pokemon_megatype_loop = {
    }

    for pokemon_id in pokemon:
        poke_number = pokemon[pokemon_id].number
        poke_mega = pokemon[pokemon_id].mega
        poke_total_power = pokemon[pokemon_id].total_power()
        if poke_number in pokemon_numbers_with_mega:
            if poke_number in pokemon_megatype_loop:
                if poke_mega:
                    pokemon_megatype_loop[poke_number]['Mega']['Total Power'] += poke_total_power
                    pokemon_megatype_loop[poke_number]['Mega']['Count'] += 1
                else:
                    pokemon_megatype_loop[poke_number]['Non-Mega']['Total Power'] += poke_total_power
                    pokemon_megatype_loop[poke_number]['Non-Mega']['Count'] += 1
            else:
                pokemon_megatype_loop[poke_number] = {
                    'Mega': {'Total Power':0, 'Count':0},
                    'Non-Mega': {'Total Power':0, 'Count':0},
                }
                if poke_mega:
                    pokemon_megatype_loop[poke_number]['Mega']['Total Power'] += poke_total_power
                    pokemon_megatype_loop[poke_number]['Mega']['Count'] += 1
                else:
                    pokemon_megatype_loop[poke_number]['Non-Mega']['Total Power'] += poke_total_power
                    pokemon_megatype_loop[poke_number]['Non-Mega']['Count'] += 1
        else:
            continue

    pokemon_comparison_nonmega_mega = {

    }
    print(pokemon_megatype_loop)
    for poke_num in pokemon_megatype_loop:
        pokemon_comparison_nonmega_mega[poke_num] = {}
        pokemon_comparison_nonmega_mega[poke_num] = {
            'Mega': pokemon_megatype_loop[poke_num]['Mega']['Total Power']/pokemon_megatype_loop[poke_num]['Mega']['Count'],
            'Non-Mega': pokemon_megatype_loop[poke_num]['Non-Mega']['Total Power']/pokemon_megatype_loop[poke_num]['Non-Mega']['Count']
        }

    delta = {
        'Delta': 0,
        'Count': 0
    }

    for poke_n in pokemon_comparison_nonmega_mega:
        delta['Delta'] += pokemon_comparison_nonmega_mega[poke_n]['Mega'] - pokemon_comparison_nonmega_mega[poke_n]['Non-Mega']
        delta['Count'] += 1

    return int(delta['Delta']/delta['Count'])









    # # Rounded to the nearest integer,
    # # how much higher is the average sum of all six stats among Mega Pokemon than their
    # # non-Mega versions? Note that Mega Pokemon share the same Number
    # # (the first column) as their non-Mega versions, which will allow you to find all Pokemon
    # # that have a Mega version.
    #
    #
    # # Rounded to the nearest integer, how much higher was that statistic than the next-closest generation's
    # # average sum of all six stats (HP, Attack, Defense, Special Attack, Special Defense, and Speed)?
    #
    # pokemon_power = {}
    # pokemon_power_2 = {}
    #
    # for pokemon_id in pokemon:
    #     if pokemon[pokemon_id].generation in pokemon_power:
    #         pokemon_power[pokemon[pokemon_id].generation]["Total Power"] += pokemon[pokemon_id].total_power()
    #         pokemon_power[pokemon[pokemon_id].generation]["Total count"] += 1
    #     else:
    #         pokemon_power[pokemon[pokemon_id].generation]= {
    #             'Total Power': 0,
    #             'Total count': 0
    #         }
    #         pokemon_power[pokemon[pokemon_id].generation]["Total Power"] += pokemon[pokemon_id].total_power()
    #         pokemon_power[pokemon[pokemon_id].generation]["Total count"] += 1
    # for pokemon_id in pokemon_power:
    #     pokemon_power_2[pokemon_id] = int(pokemon_power[pokemon_id]['Total Power']/pokemon_power[pokemon_id]['Total count'])
    #
    # print(pokemon_power_2)

    # highest_power_gen = None
    # six_gen_power = 0
    # highest_power = 0
    # second_highest_power = 0
    # delta = highest_power - six_gen_power
    #
    # for gen in pokemon_power:
    #     avg_power = pokemon_power[gen]['Total Power'] / pokemon_power[gen]['Total count']
    #     if avg_power > highest_power:
    #         highest_power = avg_power
    #         highest_power_gen = gen
    #     if gen == 6:
    #         six_gen_power = pokemon_power[gen]['Total Power'] / pokemon_power[gen]['Total count']
    # delta = highest_power - six_gen_power
    # return int(delta)

    # Among all 7 Pokemon generations, which generation had the highest average sum of all six stats
    # (HP, Attack, Defense, Special Attack, Special Defense, and Speed)?

    # pokemon_power = {}
    #
    # for pokemon_id in pokemon:
    #     if pokemon[pokemon_id].generation in pokemon_power:
    #         pokemon_power[pokemon[pokemon_id].generation]["Total Power"] += pokemon[pokemon_id].total_power()
    #         pokemon_power[pokemon[pokemon_id].generation]["Total count"] += 1
    #     else:
    #         pokemon_power[pokemon[pokemon_id].generation]= {
    #             'Total Power': 0,
    #             'Total count': 0
    #         }
    #         pokemon_power[pokemon[pokemon_id].generation]["Total Power"] += pokemon[pokemon_id].total_power()
    #         pokemon_power[pokemon[pokemon_id].generation]["Total count"] += 1
    #
    # highest_power_gen = None
    # highest_power = 0
    #
    # for gen in pokemon_power:
    #     avg_power = pokemon_power[gen]['Total Power'] / pokemon_power[gen]['Total count']
    #     if avg_power > highest_power:
    #         highest_power_gen = gen
    #         highest_power = avg_power
    #
    # return highest_power_gen

    #Rounded to the nearest integer, what is that highest average Speed statistic? Include both Type1 and Type2 in your calculation.


    # pokemon_speed = {}
    #
    # for pokemon_id in pokemon:
    #     if pokemon[pokemon_id].type1 in pokemon_speed:
    #         pokemon_speed[pokemon[pokemon_id].type1]["Total Speed"] += pokemon[pokemon_id].speed
    #         pokemon_speed[pokemon[pokemon_id].type1]["Total count"] += 1
    #     else:
    #         pokemon_speed[pokemon[pokemon_id].type1]={}
    #         pokemon_speed[pokemon[pokemon_id].type1]["Total Speed"] = 0
    #         pokemon_speed[pokemon[pokemon_id].type1]["Total count"] = 0
    #         pokemon_speed[pokemon[pokemon_id].type1]["Total Speed"] += pokemon[pokemon_id].speed
    #         pokemon_speed[pokemon[pokemon_id].type1]["Total count"] += 1
    #     if pokemon[pokemon_id].type2 in pokemon_speed:
    #         pokemon_speed[pokemon[pokemon_id].type2]["Total Speed"] += pokemon[pokemon_id].speed
    #         pokemon_speed[pokemon[pokemon_id].type2]["Total count"] += 1
    #     else:
    #         pokemon_speed[pokemon[pokemon_id].type2]={}
    #         pokemon_speed[pokemon[pokemon_id].type2]["Total Speed"] = 0
    #         pokemon_speed[pokemon[pokemon_id].type2]["Total count"] = 0
    #         pokemon_speed[pokemon[pokemon_id].type2]["Total Speed"] += pokemon[pokemon_id].speed
    #         pokemon_speed[pokemon[pokemon_id].type2]["Total count"] += 1
    #
    # highest_avg_speed_type = None
    # highest_avg_speed = 0
    #
    # for type in pokemon_speed:
    #     avg_speed = pokemon_speed[type]['Total Speed'] / pokemon_speed[type]['Total count']
    #     if avg_speed > highest_avg_speed:
    #         highest_avg_speed_type = type
    #         highest_avg_speed = avg_speed
    #
    # return int(highest_avg_speed)
    # What type has the highest average Speed statistic? Include both Type1 and Type2 in your calculation.

    # pokemon_speed = {}
    #
    # for pokemon_id in pokemon:
    #     if pokemon[pokemon_id].type1 in pokemon_speed:
    #         pokemon_speed[pokemon[pokemon_id].type1]["Total Speed"] += pokemon[pokemon_id].speed
    #         pokemon_speed[pokemon[pokemon_id].type1]["Total count"] += 1
    #     else:
    #         pokemon_speed[pokemon[pokemon_id].type1]={}
    #         pokemon_speed[pokemon[pokemon_id].type1]["Total Speed"] = 0
    #         pokemon_speed[pokemon[pokemon_id].type1]["Total count"] = 0
    #         pokemon_speed[pokemon[pokemon_id].type1]["Total Speed"] += pokemon[pokemon_id].speed
    #         pokemon_speed[pokemon[pokemon_id].type1]["Total count"] += 1
    #     if pokemon[pokemon_id].type2 in pokemon_speed:
    #         pokemon_speed[pokemon[pokemon_id].type2]["Total Speed"] += pokemon[pokemon_id].speed
    #         pokemon_speed[pokemon[pokemon_id].type2]["Total count"] += 1
    #     else:
    #         pokemon_speed[pokemon[pokemon_id].type2]={}
    #         pokemon_speed[pokemon[pokemon_id].type2]["Total Speed"] = 0
    #         pokemon_speed[pokemon[pokemon_id].type2]["Total count"] = 0
    #         pokemon_speed[pokemon[pokemon_id].type2]["Total Speed"] += pokemon[pokemon_id].speed
    #         pokemon_speed[pokemon[pokemon_id].type2]["Total count"] += 1
    #
    # highest_avg_speed_type = None
    # highest_avg_speed = 0
    #
    # for type in pokemon_speed:
    #     avg_speed = pokemon_speed[type]['Total Speed'] / pokemon_speed[type]['Total count']
    #     if avg_speed > highest_avg_speed:
    #         highest_avg_speed_type = type
    #         highest_avg_speed = avg_speed
    #
    # return highest_avg_speed_type
    # In terms of the sum of all six stats (HP, Attack, Defense, Special Attack, Special Defense, and Speed),
    # what is the strongest non-Legendary, non-Mega Pokemon?
    # If there is a tie, list any of the tying Pokemon.
    # strongest_mon_num = 0
    # strongest_mon = None
    #
    # for pokemon_id in pokemon:
    #     if not pokemon[pokemon_id].legendary and not pokemon[pokemon_id].mega:
    #         if pokemon[pokemon_id].total_power() > strongest_mon_num :
    #             strongest_mon_num  = pokemon[pokemon_id].total_power()
    #             strongest_mon = pokemon[pokemon_id].name
    # return strongest_mon
    # In terms of the sum of all six stats
    # (HP, Attack, Defense, Special Attack, Special Defense, and Speed),
    # what is the weakest Legendary Pokemon? If there is a tie, list any of the tying Pokemon.

    # weakest_legend_num = 100000
    # weakest_legend = None
    #
    # for pokemon_id in pokemon:
    #     if pokemon[pokemon_id].legendary is True:
    #         if pokemon[pokemon_id].total_power() < weakest_legend_num:
    #             weakest_legend_num = pokemon[pokemon_id].total_power()
    #             weakest_legend = pokemon[pokemon_id].name
    # return weakest_legend
# Among Legendary Pokemon, what is the most common type? Include both Type1 and Type2 in your count.

    # for pokemon_id in pokemon:
    #     if pokemon[pokemon_id].legendary is True:
    #         if pokemon[pokemon_id].type1 in pokemon_type:
    #             pokemon_type[pokemon[pokemon_id].type1] += 1
    #         else:
    #             pokemon_type[pokemon[pokemon_id].type1] = 0
    #             pokemon_type[pokemon[pokemon_id].type1] += 1
    #         if pokemon[pokemon_id].type2 in pokemon_type:
    #             pokemon_type[pokemon[pokemon_id].type2] += 1
    #         else:
    #             pokemon_type[pokemon[pokemon_id].type2] = 0
    #             pokemon_type[pokemon[pokemon_id].type2] += 1

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