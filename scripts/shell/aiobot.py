import os
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import scripts.logs.log_manager as lg
import scripts.shell.handlers


class Aiobot:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Aiobot, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        from scripts.shell.shell_config import AiobotConfig
        self.token = AiobotConfig.get_token()

        self.storage = MemoryStorage()
        self.bot = Bot(token=self.token)
        self.dp = Dispatcher(self.bot, storage=self.storage)

    @staticmethod
    def register_handlers(dp: Dispatcher):
        scripts.shell.handlers.register_all(dp)
        lg.log('handlers registered', 20)

    @staticmethod
    async def on_startup(dp):
        lg.log('Bot launched!', 20)

    def launch(self):
        self.register_handlers(self.dp)
        executor.start_polling(self.dp, skip_updates=True, on_startup=self.on_startup)

    async def send_message(self, user: int, text: str, parse_mode: str = 'HTML'):
        await self.bot.send_message(user, text=text, parse_mode=parse_mode)
        # TODO

    async def show_choice_menu(self, user: int, inline_kb: types.InlineKeyboardMarkup, text: str = 'Выберите фильтры:',
                               *args):
        await self.bot.send_message(user, text=text, reply_markup=inline_kb)

    def send_xlsx(self):
        # TODO
        pass

    def ask_user(self):
        # TODO
        pass
