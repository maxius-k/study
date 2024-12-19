def print_params(a=1, b='строка', c=True):
    print(a, b, c)
print_params(b=25)
print_params(c=[1, 2, 3])

value_list = (1, True, [1, 2, 3])
value_dict = {'a': 98, 'b': False, 'c': [4, 5, 6]}
print_params(*value_list)
print_params(**value_dict)

value_list_2 = (10.1, 'Kirill')
print_params(*value_list_2, 42)