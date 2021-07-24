my_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
print('Initial list', my_list)
my_list.sort()
print('Sorted list:', my_list)
print('my_even_list', my_list[1:10:2])
my_list.sort(reverse=True)
print('Sorted list:', my_list)
print('my_odd_list', my_list[1:10:2])
