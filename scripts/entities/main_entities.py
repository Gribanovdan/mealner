from enum import Enum
import scripts.logs.log_manager as lg


class MeasureType(Enum):
    gram = 1
    liter = 2
    piece = 3

    def __str__(self):
        if self.value == 1:
            return '100 грамм'
        if self.value == 2:
            return '1 литр'
        if self.value == 3:
            return '1 шт'
        lg.log('Bad measure type', 40)
        return None

    @staticmethod
    def get_measure_type(s: str):
        if 'грам' in s.lower():
            return MeasureType.gram
        if 'литр' in s.lower():
            return MeasureType.liter
        if 'шт' in s.lower():
            return MeasureType.piece
        lg.log('Bad measure type', 40)
        return None


class Product:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost
        # TODO
        pass

    def set_extra_stats(self, kkalories: int, protein: float, fats: float, carbohydrates: float,
                        measure: MeasureType):
        self.kkalories = kkalories
        self.protein = protein
        self.fats = fats
        self.carbohydrates = carbohydrates
        self.measure = measure


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
    def create_product(name: str, price: int, kkalories: int, protein: float, fats: float, carbohydrates: float,
                       measure: MeasureType):
        product = Product(name, price)
        product.set_extra_stats(kkalories, protein, fats, carbohydrates, measure)
        return product
