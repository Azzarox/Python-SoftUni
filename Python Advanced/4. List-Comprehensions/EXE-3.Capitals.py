# test_input:
# countries = "Bulgaria, Romania, Germany, England".split(", ")
# capitals = "Sofia, Bucharest, Berlin, London".split(", ")

# the long
# countries = input().split(", ")
# capitals = input().split(", ")
#
# country_cap_tuple = zip(countries, capitals)  # -> returns tuple
#
# dict_from_tuple = {x[0]: x[1] for x in country_cap_tuple}  # accessing tuple values 0 and 1
#
# printing_list_comprehension = [f"{el} -> {dict_from_tuple[el]}" for el in dict_from_tuple]
#
# [print(el) for el in printing_list_comprehension]

# the short
countries = input().split(", ")
capitals = input().split(", ")

country_cap_tuple = zip(countries, capitals)  # returns tuple with 2 lists

dict_from_tuple = {x[0]: x[1] for x in country_cap_tuple}  # makes a dictionary from the above tuples // accessing tuple values 0 and 1

[print(f'{el} -> {dict_from_tuple[el]}') for el in dict_from_tuple]  # prints on new line
