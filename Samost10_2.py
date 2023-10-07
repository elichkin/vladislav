class EmptyFileError(Exception):
    def __init__(self, message):
        self.message = message
def open_file(path, mode):
    try:
        with open(path, mode) as file:
            content = file.read()
            if content == '':
                raise EmptyFileError('Ваш файл пустой!')
            else:
                print('Содержимое вашего файла:', content)
    except EmptyFileError as err:
        print('Внимание! Обнаружена ошибка:', err)

open_file('./txtfiles/Samost10_2_txtfiles_no.txt', 'r')
open_file('./txtfiles/Samost10_2_txtfiles_yes.txt', 'r')