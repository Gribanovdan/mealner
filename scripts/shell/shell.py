class Shell:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Shell, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        from scripts.shell.aiobot import Aiobot
        from scripts.shell.connection import Transmitter, Receiver
        self.shell = Aiobot()
        self.transmitter = Transmitter(self)
        self.receiver = Receiver(self)

    def launch_shell(self):
        self.shell.launch()

    def send_message(self):
        # TODO
        pass

    def send_xlsx(self):
        # TODO
        pass

    def ask_user(self):
        # TODO
        pass

def launch():
    shell = Shell()
    shell.launch_shell()


