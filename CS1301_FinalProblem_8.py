#-----------------------------------------------------------
#The United States Social Security Administration publishes
#a list of all documented baby names each year, along with
#how often each name was used for boys and for girls. The
#list is used to see what names are most common in a given
#year.
#
#We've grabbed that data for any name used more than 25
#times, and provided it to you in a file called
#babynames.csv. The line below will open the file:

# def read_data():
#     gender = {}
#
#     def name_details(line_item):
#         name_of_child = line_item[0] # actual name
#         count_name_used = line_item[1] # number of times the name is given out
#         gender_of_name = line_item[2] # boy or girl
#         return name_of_child, count_name_used, gender_of_name
#
#     with open('../resource/lib/public/babynames.csv', 'r') as file:
#         for line in file:
#             clean_line = line.strip()
#             line_data = clean_line.split(',')
#             name, times_given, name_gender = name_details(line_data)
#
#             if name_gender not in gender:
#                 gender[name_gender] = {}
#                 gender[name_gender][name] = {
#                     "Number of times name used" : times_given,
#                 }
#             else:
#                 gender[name_gender][name] = {
#                     "Number of times name used" : times_given,
#                 }



    # How many total names are listed in the database?
    # name_gender = []
    # for gender, name in gender.items():
    #     for name_ in name:
    #         if name_ in name_gender:
    #             continue
    #         else:
    #             name_gender.append(name)
    # return len(name_gender)
    # return gender

    # How many total births are covered by the names in the database?
    # birth_count = 0
    # for gender, name in gender.items():
    #     for name_ in name:
    #         birth_count += int(name[name_]['Number of times name used'])
    # return birth_count
    # return gender

    # How many different boys' names are there that begin with the letter Z? (Count the names, not the people.)

    # q_names = {}
    # for gender, name in gender.items():
    #     if gender == 'Boy':
    #         continue
    #     else:
    #         for name_ in name:
    #             if name_[0] == 'Q':
    #                 if name_ in q_names:
    #                     q_names[name_] += int(name[name_]['Number of times name used'])
    #                 else:
    #                     q_names[name_] = 0
    #                     q_names[name_] += int(name[name_]['Number of times name used'])
    #             else:
    #                 continue
    # max_name_count = 0
    # max_name = ''
    #
    # for name, count in q_names.items():
    #     if count > max_name_count:
    #         max_name_count =  count
    #         max_name = name
    #
    # return max_name

    #How many total babies were given names that both start and end with vowels (A, E, I, O, or U)?
    #
    # vowel_names = {}
    # vowels = ['a', 'e', 'i', 'o', 'u']
    # for gender, name in gender.items():
    #     for name_ in name:
    #         name_lower = name_.lower()
    #         if name_lower[0] in vowels and name_lower[-1] in vowels:
    #             if name_ in vowel_names:
    #                 vowel_names[name_] += int(name[name_]['Number of times name used'])
    #             else:
    #                 vowel_names[name_] = 0
    #                 vowel_names[name_] += int(name[name_]['Number of times name used'])
    # name_vowel_count = 0
    # for name, count in vowel_names.items():
    #     name_vowel_count += count
    #
    # return name_vowel_count


    # What letter is the least common first letter of a baby's name
    # (in terms of number of babies with names starting with that letter, not number of names)?

    # names_count = {}
    # for gender, name in gender.items():
    #     for name_ in name:
    #         if name_[0] in names_count:
    #             names_count[name_[0]] += int(name[name_]['Number of times name used'])
    #         else:
    #             names_count[name_[0]] = 0
    #             names_count[name_[0]] += int(name[name_]['Number of times name used'])
    #
    # low_name_count = 100000000
    # low_name = None
    #
    # for name, count in names_count.items():
    #     if count < low_name_count:
    #         low_name_count = count
    #         low_name = name
    #
    # return low_name_count

#     What letter is the most common first letter of a baby's name
#     (in terms of number of babies with names starting with that letter, not number of names)?

    # names_count = {}
    # for gender, name in gender.items():
    #     for name_ in name:
    #         if name_[0] in names_count:
    #             names_count[name_[0]] += int(name[name_]['Number of times name used'])
    #         else:
    #             names_count[name_[0]] = 0
    #             names_count[name_[0]] += int(name[name_]['Number of times name used'])
    #
    # high_name_count =0
    # high_name = None
    #
    # for name, count in names_count.items():
    #     if count > high_name_count:
    #         high_name_count = count
    #         high_name = name
    #
    # return high_name_count

# How many babies were born with names starting with that most-common letter?

    #
    # names_count = {}
    # for gender, name in gender.items():
    #     for name_ in name:
    #         if name_[0] in names_count:
    #             names_count[name_[0]] += int(name[name_]['Number of times name used'])
    #         else:
    #             names_count[name_[0]] = 0
    #             names_count[name_[0]] += int(name[name_]['Number of times name used'])
    #
    # high_name_count =0
    # high_name = None
    #
    # for name, count in names_count.items():
    #     if count > high_name_count:
    #         high_name_count = count
    #         high_name = name
    #
    # return high_name_count


    #By default, the Social Security Administration's data separates out names by gender.
    # For example, Jamie is listed separately for girls and for boys.
    # If you were to remove this separation, what would be the most common name in the 2010s regardless of gender?


# def read_data():
#     child_name = {}
#
#     def name_details(line_item):
#         name_of_child = line_item[0] # actual name
#         count_name_used = line_item[1] # number of times the name is given out
#         gender_of_name = line_item[2] # boy or girl
#         return name_of_child, count_name_used, gender_of_name
#
#     with open('../resource/lib/public/babynames.csv', 'r') as file:
#         for line in file:
#             clean_line = line.strip()
#             line_data = clean_line.split(',')
#             name, times_given, name_gender = name_details(line_data)
#
#             if name not in child_name:
#                 child_name[name] = {}
#                 child_name[name] = {
#                     "Number of times name used" : int(times_given),
#                 }
#             else:
#                 child_name[name]['Number of times name used'] += int(times_given)
#
#     highest_count = 0
#     popular_name = None
#     for name in child_name:
#         count_of_name = int(child_name[name]['Number of times name used'])
#         if count_of_name > highest_count:
#             highest_count =  count_of_name
#             popular_name = name
#
#     return popular_name


# How many people would have that name?

# def read_data():
#     child_name = {}
#
#     def name_details(line_item):
#         name_of_child = line_item[0] # actual name
#         count_name_used = line_item[1] # number of times the name is given out
#         gender_of_name = line_item[2] # boy or girl
#         return name_of_child, count_name_used, gender_of_name
#
#     with open('../resource/lib/public/babynames.csv', 'r') as file:
#         for line in file:
#             clean_line = line.strip()
#             line_data = clean_line.split(',')
#             name, times_given, name_gender = name_details(line_data)
#
#             if name not in child_name:
#                 child_name[name] = {}
#                 child_name[name] = {
#                     "Number of times name used" : int(times_given),
#                 }
#             else:
#                 child_name[name]['Number of times name used'] += int(times_given)
#
#     highest_count = 0
#     popular_name = None
#     for name in child_name:
#         count_of_name = int(child_name[name]['Number of times name used'])
#         if count_of_name > highest_count:
#             highest_count =  count_of_name
#             popular_name = name
#
#     return highest_count

# What name that is used for both genders has the smallest difference in which gender holds the name most frequently?
# In case of a tie, enter any one of the correct answers.

# def read_data():
#
#     same_name = {
#         "Boy" : {},
#         'Girl' :{}
#     }
#     gender = {}
#     delta = {}
#
#     def name_details(line_item):
#         name_of_child = line_item[0] # actual name
#         count_name_used = line_item[1] # number of times the name is given out
#         gender_of_name = line_item[2] # boy or girl
#         return name_of_child, count_name_used, gender_of_name
#
#     with open('../resource/lib/public/babynames.csv', 'r') as file:
#         for line in file:
#             clean_line = line.strip()
#             line_data = clean_line.split(',')
#             name, times_given, name_gender = name_details(line_data)
#
#             if name_gender not in gender:
#                 gender[name_gender] = {}
#                 gender[name_gender][name] = {
#                     "Number of times name used" : times_given,
#                 }
#             else:
#                 gender[name_gender][name] = {
#                     "Number of times name used" : times_given,
#                 }
#
#     for name in gender['Boy']:
#         if name in gender['Girl']:
#             if name in same_name['Boy']:
#                 same_name['Boy'][name] += int(gender['Boy'][name]['Number of times name used'])
#                 same_name['Girl'][name] += int(gender['Girl'][name]['Number of times name used'])
#             else:
#                 same_name['Boy'][name] = 0
#                 same_name['Girl'][name] = 0
#                 same_name['Boy'][name] += int(gender['Boy'][name]['Number of times name used'])
#                 same_name['Girl'][name] += int(gender['Girl'][name]['Number of times name used'])
#
#     for name in same_name['Boy']:
#         delta[name] = abs(same_name['Boy'][name] - same_name['Girl'][name])
#
#     smallest_delta_number = 10000000
#     smallest_delta = None
#
#     for name in delta:
#         if delta[name] < smallest_delta_number:
#             smallest_delta_number = delta[name]
#             smallest_delta = name
#
#     return smallest_delta




#We've also provided a sample subset of the data in
#sample.csv.
#
#Each line of the file has three values, separated by
#commas. The first value is the name; the second value is
#the number of times the name was given in the 2010s (so
#far); and the third value is whether that count
#corresponds to girls or boys. Note that if a name is
#given to both girls and boys, it is listed twice: for
#example, so far in the 2010s, the name Jamie has been
#given to 611 boys and 1545 girls.
#
#Use this dataset to answer the questions below.


#Here, add any code you want to allow you to answer the
#questions asked below over on edX. This is just a sandbox
#for you to explore the dataset: nothing is required for
#submission here.





