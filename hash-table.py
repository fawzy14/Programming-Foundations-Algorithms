# demonstrate hashtable usage


# TODO: create a hashtable all at once

item1 = dict({'key1': 1, 'key2': 2, 'key3':'three'})

print(item1)

# TODO: create a hashtable progressively

item2 = {}
item2['key1'] = 1
item2['key2'] = 2
item2['key3'] = 3

print(item2)


# TODO: try to access a nonexistent key

# print(item2['key6'])


# TODO: replace an item

item2['key2'] = 'two'

print(item2)

# TODO: iterate the keys and values in the dictionary

for key, value in item2.items():
     print('key:', key, 'value', value)