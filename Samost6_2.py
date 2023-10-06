example_1 = ((1, 2, 3), 1)
example_2 = ((1, 2, 3, 1, 2, 3, 4, 5, 2, 3, 4, 2, 4, 2), 3)
example_3 = ((2, 4, 6, 6, 4, 2), 9)

def remove_element_from_tuple(value):
    source_tuple, element = value
    new_list = []
    was_removed = False
    for x in list(source_tuple):
        if x == element and was_removed == False:
            was_removed = True
            continue
        new_list.append(x)
    return tuple(new_list)

print('Результат #1:', remove_element_from_tuple((example_1)))
print('Результат #2:', remove_element_from_tuple((example_2)))
print('Результат #3:', remove_element_from_tuple((example_3)))