immutable_var = 1, 2, 3, 'a', 'b', 'c', True
print(immutable_var)
#immutable_var[1] = 5
#print(immutable_var) # кортеж не поддерживает обращение по элементам, с кортежем мы можем выполнить только конкатенацию и умножение
mutable_list = [1, 2, 3, 'a','b','c',True]
print(mutable_list)
mutable_list[6] = 7
print(mutable_list)