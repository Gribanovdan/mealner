class Product:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost
        # TODO
        pass


class DishIngridient:
    def __init__(self, product: Product, frac: float):
        self.product = product
        self.frac = frac
        # TODO


class Dish:
    def __init__(self, name: str, ingridients: list[DishIngridient]):
        self.ingridients = ingridients
        # TODO


class Creator:
    @staticmethod
    def create_dish():
        # TODO
        pass

    @staticmethod
    def create_product():
        # TODO
        pass
