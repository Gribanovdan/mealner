import os
from aiogram import Bot, Dispatcher, executor, types

import scripts.shell.handlers


class Aiobot:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Aiobot, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        from scripts.shell.shell_config import AiobotConfig
        self.token = AiobotConfig.get_token()

        self.bot = Bot(token=self.token)
        self.dp = Dispatcher(self.bot)

    def register_handlers(self, dp: Dispatcher):
        scripts.shell.handlers.register_all(dp)

    def launch(self):
        self.register_handlers(self.dp)
        executor.start_polling(self.dp, skip_updates=True)

    def send_message(self):
        # TODO
        pass

    def send_xlsx(self):
        # TODO
        pass

    def ask_user(self):
        # TODO
        pass
