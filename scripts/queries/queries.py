class Query:
    def __init__(self, user: int):
        self.user = user

    # TODO
    # user?
    pass


class AddDish(Query):
    # TODO
    pass


class AddProduct(Query):
    # TODO
    pass


class GenerateMenu(Query):
    def __init__(self, user: int, filters: list):
        super().__init__(user)
        self.filters = filters
    # TODO
    pass


class GetShoppingList(Query):
    # TODO
    pass


class RequireFilters(Query):
    # TODO
    pass