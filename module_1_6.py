my_dict = {"Gleb":1991,"Masha":1994}
print(my_dict)
print(my_dict["Gleb"])
my_dict["Bes"] = 2021
print(my_dict["Bes"])
my_dict.update({"Ksyusha": 2012, "Bag": 2023})
a = my_dict.pop("Bag")
print(a)
print(my_dict)

my_set = {1, 9, 9, 1, 'Noyabr', False, (1, 2, 3)}
print(my_set)
my_set.add("O/")
my_set.add((1, 3, 2))
my_set.discard((1, 2, 3))
print(my_set)