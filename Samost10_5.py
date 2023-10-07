class NameLengthError(Exception):
    def __init__(self, message):
        self.message = message
def lower_case_username(value):
    if len(value) < 3:
        raise NameLengthError('Пожалуйста проверьте, длина указанного Вами имени, должна быть больше 2ух символов!')
class Student:
    def __init__(self, name, age):
        self.name = lower_case_username(name)
        self.age = age
try:
    lower_case_username('Ян')
except NameLengthError as err:
    print('Внимание! Обнаружена ошибка!:', err)
try:
    Student('Ян', 28)
except NameLengthError as err:
    print('Внимание! Обнаружена ошибка!:', err)
try:
    Student('Яна', 28)
except NameLengthError as err:
    print('Внимание! Обнаружена ошибка!:', err)
finally:
    print('Учётная запись студента создана успешно')