my_list = []

my_list.append (10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

my_list.insert(1, 15)

my_list.extend([50, 60, 70])

my_list.pop()

my_list.sort()

value_to_find = 50
index_of_value = my_list.index(value_to_find)
print("Index of", value_to_find, "is", index_of_value)

print("Final list:", my_list)