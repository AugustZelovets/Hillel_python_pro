class Human:
    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age

    def __str__(self):
        return f'Human with name: {self.name}, sex: {self.sex}, age: {self.age}'

    def __repr__(self):
        return f'Human("{self.name}", "{self.sex}", "{self.age}")'


if __name__ == '__main__':
    danil = Human(sex='male', age=24, name='Danil')
    print(danil)
