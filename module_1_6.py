my_dict = {'Kirill': 2001, 'Varya': 2002, 'Anna': 2004}
print(my_dict)
print(my_dict['Varya'])
my_dict['Darya'] = 1998
print(my_dict['Darya'])
my_dict.update({'Grigory': 2003, 'Sasha': 1999})
print(my_dict)
del my_dict['Darya']
print(my_dict.get('Darya', 'Такого ключа не существует'))
print(my_dict)

my_set = {1, 2, 3,'Kirill', 2, 4, 1, 'Kirill', 'Anna', (1,2,3)}
print(my_set)
my_set.add(5)
my_set.add(0)
print(my_set)
my_set.remove((1,2,3))
print(my_set)

