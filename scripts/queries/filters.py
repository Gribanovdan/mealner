class Filter:
    # TODO
    pass


class EmptyFilter(Filter):
    # TODO
    pass


class BudgetFilter(Filter):
    def __init__(self, budget: int):
        self.budget = budget

    def __str__(self):
        return f'Бюджет: {self.budget}р.'

    # TODO


class SnackFilter(Filter):
    def __init__(self, exists: bool = False):
        self.exists = exists

    def __str__(self):
        res = 'да' if self.exists else 'нет'
        return f'Добавить перекусы? {res}.'


class KkaloriesFilter(Filter):
    def __init__(self, kkalories: int):
        self.kkalories = kkalories

    def __str__(self):
        return f'{self.kkalories} ккалорий в день.'

# TODO добавить фильтры
