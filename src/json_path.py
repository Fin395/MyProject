import os

dir_path = os.path.dirname(os.path.realpath(__file__))
logs_path = os.path.join(dir_path, "..", "data", "operations.json")
#print(logs_path)

my_list = [1,2,3,4,5]
if 3 < 2:
    my_list = my_list
else:
    my_list.append(6)
print(my_list)


