from scripts.shell.shell import Shell
import scripts.queries.queries as qr
import scripts.queries.filters as ft
import scripts.processor.connection as cn
import scripts.shell.inline_keyboards as kb

class Transmitter:
    shell: Shell = None

    @staticmethod
    async def transmit(query: qr.Query):

        await cn.ShellReceiver.receive(query)
        # TODO

    # TODO


class Receiver:
    shell: Shell = None

    @staticmethod
    async def receive(query: qr.Query):
        user = query.user_id
        if isinstance(query, qr.RequireFilters):
            await Receiver.shell.show_choice_menu(user, kb.generating_filters_choice())
            pass
            # TODO
    # TODO
