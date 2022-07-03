import json
from pprint import pprint
from typing import List

from human import Human


def objects_list_to_dict_list(objects_list: List[Human]) -> List[dict]:
    '''Написати функцію яка буде переводити переданий список
    обєктів класу в список словників та повертати результат'''
    return [person.__dict__ for person in objects_list]
    result = []
    for i in objects_list:
        print(i)
        temp_dict = {'name': i.name, 'sex': i.sex, 'age': i.age}
        result.append(temp_dict)
    return result


def create_json(some_list: List[dict]) -> json:
    """Напиcати функцію яка буде зберігати список словників в
    файл json"""
    with open('human.json', 'w') as f:
        json.dump(some_list, f, indent=2)


'''Написати код в кінці файлу який буде створювати 
обєкти класу, викликати функції що конвертують їх 
в список словників та функцію що зберегіє їх в файл'''

if __name__ == '__main__':
    l = [Human("Danil", "Male", "24"),
         Human("Sergey", "Male", "40"),
         Human("Olga", "Female", "30")]

    print(objects_list_to_dict_list(l))
    create_json(objects_list_to_dict_list(l))
