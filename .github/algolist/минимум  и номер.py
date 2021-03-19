my_list = [4, 7, -3, 1, -7, 11, 6]
val, idx = min((val, idx) for (idx, val) in enumerate(my_list))
print('Минимальный {}-й элемент массива = {}'.format(idx + 1, val))
