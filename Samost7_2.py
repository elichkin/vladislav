with open('./txtfiles/Samost7_2.txt', 'a') as file:
    date = input('Пожалуйста, введите дату покупки: ')
    category = input('Пожалуйста, введите категорию товаров: ')
    sum = int(input('Пожалуйста, введите сумму покупки: '))

    file.write(f'{date}\t\t\t{category}\t\t\t{sum}\n')

with open('./txtfiles/Samost7_2.txt', 'r') as file:
    print('Учёт ваших расходов:\n', file.read())