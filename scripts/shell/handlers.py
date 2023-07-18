from aiogram import Dispatcher, types
import scripts.shell.reply_patterns as rp
from scripts.shell.connection import Transmitter as tr
import scripts.queries.queries as qr
import scripts.queries.filters as ft


class HandlerSet:
    # TODO
    pass


class TextHandlers(HandlerSet):
    @staticmethod
    async def start(msg: types.Message):
        await msg.answer(*rp.start())

    @staticmethod
    async def help(msg: types.Message):
        await msg.answer(*rp.help())

    @staticmethod
    async def generate(msg: types.Message):
        await tr.transmit(query=qr.GenerateMenu(msg.from_user.id))


class InlineHandlers(HandlerSet):
    # TODO
    pass


class Stages:
    # TODO
    pass


def register_all(dp: Dispatcher):
    dp.register_message_handler(TextHandlers.start, commands=['start'])
    dp.register_message_handler(TextHandlers.help, commands=['help'])
    dp.register_message_handler(TextHandlers.generate, commands=['generate'])
    # TODO
