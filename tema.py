my_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
print('Initial list', my_list)
new_list = sorted(my_list)
print('Sorted list', new_list)
print('my_even_list', new_list[1::2])
print('Reverse list', new_list[::-1])
print('my_odd_list', new_list[::2])
my_sliced_list = new_list[2::3]
print('Multiple of 3', my_sliced_list)
print('Initial list', my_list)
