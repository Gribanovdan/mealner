from aiogram import Dispatcher, types
import scripts.shell.reply_patterns as rp

class HandlerSet:
    # TODO
    pass


class TextHandlers(HandlerSet):
    @staticmethod
    async def start(msg: types.Message):
        await msg.answer(*rp.start())

    @staticmethod
    def help(msg: types.Message):
        pass
        # TODO

class InlineHandlers(HandlerSet):
    # TODO
    pass


class Stages:
    # TODO
    pass


def register_all(dp: Dispatcher):
    dp.register_message_handler(TextHandlers.start, commands=['start'])
    # TODO