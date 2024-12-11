#Write a function called count_duplicates. The function
#should have one parameter, a list of integers. The
#function should return the number of integers in the
#list that are duplicates of earlier integers in the
#list.
#
#For example:
#
# count_duplicates([1, 2, 2, 3, 3, 3]) -> 3
#
#There are three duplicates in that list; the second 2,
#the second 3, and the third 3.
#
#Here are other examples:
#
# count_duplicates([1, 2, 3, 4, 5, 6, 7]) -> 0
# count_duplicates([5, 5, 5, 5, 5, 5, 5, 5, 5]) -> 8
# count_duplicates([7, 3, 7, 3, 7, 3, 7, 3]) -> 6


#Write your function here!

def count_duplicates(list_of_ints):
    sort_list =  sorted(list_of_ints)
    duplicate_count = 0
    for number in range(0, len(sort_list)-1):
        if sort_list[number] == sort_list[number+1]:
            duplicate_count += 1
        else:
            continue
    return duplicate_count


#The lines below will test your code. Feel free to modify
#them. If your code is working properly, these will print:
#3, 0, 8, 6, each on its own line.
print(count_duplicates([1, 2, 2, 3, 3, 3]))
print(count_duplicates([1, 2, 3, 4, 5, 6, 7]))
print(count_duplicates([5, 5, 5, 5, 5, 5, 5, 5, 5]))
print(count_duplicates([7, 3, 7, 3, 7, 3, 7, 3]))


