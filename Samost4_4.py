def calc(*numbers):
    countNumbers = len((numbers))
    result = 0;
    for i in range(countNumbers):
        result += numbers[i]

    return result / countNumbers
def main():
    print('Для чисел 8, 7, 6 среднее арифметическое будет равно:', calc(8, 7, 6))
if __name__ == '__main__':
    main()