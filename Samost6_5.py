example_1 = (15, 26, 30, 32, 41, 44, 47, 53, 57, 61)
example_2 = (588, 107, 620, 39, 404, 886, 1345, 812, 875, 401)
example_3 = (1682, 2971, 6913, 8713, 10289, 8841, 1594, 10534, 1972, 7426)

def get_even_numbers(values):
    new_list = []
    for x in list(values):
        if x % 2 == 1: new_list.append(x)
    return tuple(new_list)

print('Результат #1:', get_even_numbers(example_1))
print('Результат #2:', get_even_numbers(example_2))
print('Результат #3:', get_even_numbers(example_3))