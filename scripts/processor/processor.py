import scripts.queries.queries as qr
import scripts.queries.filters as ft
import scripts.processor.connection as cn

class ProductAdder:
    # TODO
    pass


class DishAdder:
    # TODO
    pass


class MenuGenerator:
    @staticmethod
    async def processor(user: int, filters: list[ft.Filter]):
        if not filters:
            await cn.ShellTransmitter.transmit(qr.RequireFilters(user))
            #TODO

    # TODO
    pass


class ShoppingListGetter:
    # TODO
    pass
