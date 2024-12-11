#Imagine we're writing some code for a video game.
#In this video game, there are six elements, which
#come in three pairs: Fire and Ice; Land and Water;
#Time and Space. Each pair of elements cancels
#themselves out: if an attack does 3 Fire damage and
#3 Ice damage, then it does 0 total damage.
#
#Write a function called calculate_damage.
#calculate_damage should take as input a list of
#2-tuples. The first item of each 2-tuple will be an
#integer; the second will be a string, either "Fire",
#"Ice", "Land", "Water", "Time", or "Space".
#
#Your function should return a list of three 2-tuples:
#the first will represent the total Fire or Ice
#damage, such as (3, "Ice") or (2, "Fire"). The
#second will represent the total Land or Water damage,
#such as (3, "Water") or (2, "Land"). The third
#will represent the total Time or Space damage,
#such as (3, "Time") or (2, "Space").
#
#You may assume that there will always be some net
#damage for each of the three categories (e.g. you
#don't have to handle the case where there is 0 Fire
#or Ice damage).
#
#For example, for the following list of 2-tuples...
#
# attacks = [(3, "Fire"), (2, "Ice"), (5, "Water"),
#            (2, "Land"), (1, "Time"), (2, "Space")]
# calculate_damage(attacks) -> [(1, "Fire"), (3, "Water"), (1, "Space")]
#
#Because:
# - 3 Fire + 2 Ice = 1 Fire
# - 5 Water + 2 Land = 3 Water
# - 1 Time + 2 Space = 1 Space
#
#HINT: For each of the three pairs, try thinking of
#one as positive and the other as negative.


#Write your function here!

def calculate_damage(list_of_tuples):
    fire_ice_dmg = 0
    land_water_dmg = 0
    time_space_dmg = 0

    for dmg, element in list_of_tuples:
        if element == "Fire":
            fire_ice_dmg += dmg
        elif element == "Ice":
            fire_ice_dmg -= dmg
        elif element == "Land":
            land_water_dmg += dmg
        elif element == "Water":
            land_water_dmg -= dmg
        elif element == "Time":
            time_space_dmg += dmg
        elif element == "Space":
            time_space_dmg -= dmg

    return [(abs(fire_ice_dmg), "Fire" if fire_ice_dmg > 0 else "Ice"),
            (abs(land_water_dmg), "Land" if land_water_dmg > 0 else "Water"),
            (abs(time_space_dmg), "Time" if time_space_dmg > 0 else "Space")]


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print:
#[(1, 'Fire'), (3, 'Water'), (1, 'Space')]
attacks = [(3, "Fire"), (2, "Ice"), (5, "Water"), (2, "Land"), (1, "Time"), (2, "Space")]
print(calculate_damage(attacks))


