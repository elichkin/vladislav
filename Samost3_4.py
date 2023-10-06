value = input('Пожалуйста, введите Ваше предложение: ')
print('Длина Вашего предложения:', len(value))
print('Ваше предложение переведено в нижний регистр:', value.lower())

words = 0
for i in range(len(value)):
    if value[i] in  ['a', 'e', 'i', 'o', 'u']:
        words += 1
print('Количество гласных (a,e,i,o,u) в Вашем предложении:', words)
print('Произведена замена слова "ugly" на "beauty":', value.replace('ugly', 'beauty'))
print('Ваше предложение начинается на The:', 'да' if value.find('The') == 0 else 'нет')
print('Ваше предложение заканчивается на End:', 'да' if value.find('End') == len(value) - len('End') else 'нет')
