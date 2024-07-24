def descending_order(num):
    numbers_str = str(num)
    numbers_list = list(numbers_str)
    numbers_list.sort(reverse=True)
    sorted_numbers_str = ''.join(numbers_list)
    return int(sorted_numbers_str)







print(descending_order(132485))