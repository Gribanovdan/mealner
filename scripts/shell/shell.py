


class Shell:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Shell, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        from scripts.shell.aiobot import Aiobot
        from scripts.shell.connection import Transmitter, Receiver
        self.shell = Aiobot()
        Transmitter.shell = self
        Receiver.shell = self

    def launch_shell(self):
        # TODO может поумнее что-нибудь?
        import scripts.shell.handlers as handlers
        handlers.shell = self
        self.shell.launch()

    async def send_message(self, user: int, text: str, parse_mode: str = 'HTML'):
        # TODO не уверен насчет parse_mode, здесь ли это нужно делать?
        await self.shell.send_message(user, text, parse_mode)

    async def show_choice_menu(self, user: int, *args):
        await self.shell.show_choice_menu(user, *args)

    def send_xlsx(self):
        # TODO
        pass

    def ask_user(self):
        # TODO
        pass

def launch():
    shell = Shell()
    shell.launch_shell()


