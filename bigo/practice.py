a = [3, 1, 2]
a.sort()

print(a)

b = sorted("bac")
print(b)

"""
list
tuple
set
dict
"""
my_dict = {'name': 'Python', 'version': 3.11, 'year': 1991}
my_dict["manh"]=12
print(my_dict)
# last_item = my_dict.popitem()
# print(last_item) # ('name', 'Python')
# print(my_dict) # {}
del my_dict['year']
print(my_dict)