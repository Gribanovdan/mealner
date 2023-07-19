import scripts.queries.queries as qr
import scripts.queries.filters as ft
import scripts.shell.connection as shell_cn
import scripts.processor.processor as pr

class ShellReceiver:
    @staticmethod
    async def receive(query: qr.Query):
        if isinstance(query, qr.GenerateMenu):
            await pr.MenuGenerator.processor(query.user, query.filters)

    # TODO
    pass


class ShellTransmitter:
    @staticmethod
    async def transmit(query: qr.Query):
        await shell_cn.Receiver.receive(query)
        # TODO

    # TODO
    pass


class DBReceiver:
    # TODO
    pass


class DBTransmitter:
    # TODO
    pass
