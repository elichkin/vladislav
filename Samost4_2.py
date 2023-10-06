from random import randint
def roll():
    result = randint(1, 6)
    print('Значение кубика: ', result)
    if result == 3 or result == 4:
        return roll()
    return result;
def main():
    value = roll()
    if value == 5 or value == 6:
        print('Вы победили')
    elif value == 1 or value == 2:
        print('Вы проиграли')
if __name__ == '__main__':
    main()