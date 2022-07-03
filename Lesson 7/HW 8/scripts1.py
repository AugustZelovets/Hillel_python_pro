import json
from pprint import pprint
from typing import List, Dict, Any

from human import Human


def create_class_objects(some_list: List[Dict[str, Any]]) -> List[Human]:
    """приймає список діктів та повертає список об`єктів"""
    result = []
    for human in human_list:
        result.append(Human(human['name'], human['sex'], human['age'], ))
    return [Human(**item) for item in some_list]


def read_dict_lists(some_file: str) -> List[dict]:
    """читає файл і повертає список словників"""
    with open(some_file, 'r') as f:
        return json.load(f)


if __name__ == '__main__':
    human_list = [
        {
            'name': 'Danil',
            'sex': 'Male',
            'age': '24',
        },
        {
            'name': 'Sergey',
            'sex': 'Male',
            'age': '40',
        },
        {
            'name': 'Olga',
            'sex': 'Female',
            'age': '30',
        }]

    pprint(read_dict_lists('humans.json'), sort_dicts=False)
    print()
    pprint(create_class_objects(human_list))
