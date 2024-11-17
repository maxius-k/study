immutable_var = 1, 2, 3, 'urban', True
print(immutable_var)
#immutable_var[0] = 4 #- в кортежах нельзя менять элеметы, потому что он создан для хранения неизменяемых данных
mutable_list = [1, 2, 3, 'urban', True]
print(mutable_list)
mutable_list[0] = 4
print(mutable_list)