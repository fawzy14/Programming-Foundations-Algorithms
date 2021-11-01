names = []    #stack 

names.append('Mahmoud')   # in stack last in, first out
names.append('Omer')      # in stack first in, last out 
names.append('Fawzy')
names.append('Mostafa')

print(names)  

remove_name = names.pop()  #Mostafa will out 
print(remove_name)
print(names)