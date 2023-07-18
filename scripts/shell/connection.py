from scripts.shell.shell import Shell
import scripts.queries.queries as qr
import scripts.queries.filters as ft
import scripts.processor.connection as cn


class Transmitter:
    shell: Shell = None

    @staticmethod
    async def transmit(query: qr.Query, filters: list[ft.Filter] = None):
        if filters is None:
            filters = []
        await cn.ShellReceiver.receive(query, filters)
        # TODO

    # TODO


class Receiver:
    shell: Shell = None

    @staticmethod
    async def receive(query: qr.Query):
        user = query.user_id
        if isinstance(query, qr.RequireFilters):
            await Receiver.shell.send_message(user, 'Fuck you:)')
            pass
            # TODO
    # TODO
