import requests


class DoingModel:
    def __init__(self, id, title, category_id, details, date):
        self.id = id
        self.title = title
        self.category_id = category_id
        self.details = details
        self.date = date


class CategoryModel:
    def __init__(self, id, name):
        self.id = id
        self.name = name

