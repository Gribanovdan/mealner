from aiogram import Dispatcher, types
import scripts.shell.reply_patterns as rp
from scripts.shell.connection import Transmitter as tr
import scripts.queries.queries as qr
import scripts.queries.filters as ft
from aiogram.dispatcher import FSMContext
from scripts.shell.states import GeneratingStates
import scripts.shell.inline_keyboards as kb

shell = tr.shell


class HandlerSet:
    # TODO
    pass


class TextHandlers(HandlerSet):
    @staticmethod
    async def start(msg: types.Message, state: FSMContext):
        await msg.answer(*rp.start())
        await state.finish()

    @staticmethod
    async def help(msg: types.Message, state: FSMContext):
        await msg.answer(*rp.help())
        await state.finish()

    @staticmethod
    async def generate(msg: types.Message, state: FSMContext):
        await state.set_state(GeneratingStates.choosing_filter)
        filters = [ft.SnackFilter()]
        await state.update_data(filters=filters)
        await shell.show_choice_menu(msg.from_user.id, kb.generating_filters_choice())

    class GeneratingFiltersChoice(HandlerSet):
        @staticmethod
        async def tuning_budget(message: types.Message, state: FSMContext):
            if not message.text.isdigit():
                await message.answer('Неправильный формат ввода. Повторите попытку')
                return
            data = await state.get_data()
            filters: list = data['filters']
            budget = int(message.text)
            for i in range(len(filters)):
                if isinstance(filters[i], ft.BudgetFilter):
                    filters[i].budget = budget
                    break
            else:
                filters.append(ft.BudgetFilter(budget))
            await state.update_data(filters=filters)
            await state.set_state(GeneratingStates.choosing_filter)
            await message.answer(text=f'Вы ввели бюджет: *{budget}р*.', parse_mode='Markdown')
            # TODO отслеживание очередного нажатия по кнопке
            await shell.show_choice_menu(message.from_user.id, kb.generating_filters_choice())

        @staticmethod
        async def tuning_kkalories(message: types.Message, state: FSMContext):
            if not message.text.isdigit():
                await message.answer('Неправильный формат ввода. Повторите попытку')
                return
            data = await state.get_data()
            filters: list = data['filters']
            kkalories = int(message.text)
            for i in range(len(filters)):
                if isinstance(filters[i], ft.KkaloriesFilter):
                    filters[i].kkalories = kkalories
                    break
            else:
                filters.append(ft.KkaloriesFilter(kkalories))
            await state.update_data(filters=filters)
            await state.set_state(GeneratingStates.choosing_filter)
            await message.answer(text=f'Вы ввели бюджет: *{kkalories}* ккалорий в день.', parse_mode='Markdown')
            # TODO отслеживание очередного нажатия по кнопке
            await shell.show_choice_menu(message.from_user.id, kb.generating_filters_choice())


# inline_keyboards.py
class InlineHandlers(HandlerSet):
    class GeneratingFiltersChoice(HandlerSet):
        @staticmethod
        async def budget(callback: types.CallbackQuery, state: FSMContext):
            await callback.answer()
            await state.set_state(GeneratingStates.tuning_budget)
            await callback.bot.send_message(callback.from_user.id, text='Введите желаемый *недельный* бюджет в рублях:',
                                            parse_mode='Markdown')
            await callback.bot.delete_message(callback.message.chat.id, callback.message.message_id)
            # TODO
            pass

        @staticmethod
        async def snack(callback: types.CallbackQuery, state: FSMContext):
            await callback.answer()
            await callback.bot.delete_message(callback.message.chat.id, callback.message.message_id)

            await shell.show_choice_menu(callback.from_user.id, kb.snack_choice(), 'Хотите добавить перекусы в рацион?')
            await state.set_state(GeneratingStates.tuning_snack)

            # TODO
            pass

        @staticmethod
        async def tuning_snack(callback: types.CallbackQuery, state: FSMContext):
            data = await state.get_data()
            filters = data['filters']
            for i in range(len(filters)):
                if isinstance(filters[i], ft.SnackFilter):
                    f = filters[i]
                    break
            else:
                f = ft.SnackFilter()
                filters.append(f)
            if 'yes' in callback.data:
                f.exists = True
            elif 'no' in callback.data:
                f.exists = False
            else:
                await callback.bot.send_message(callback.from_user.id, text='Произошла ошибка ввода. Повторите попытку')

            await state.update_data(filters=filters)
            await callback.answer()
            await callback.bot.delete_message(callback.message.chat.id, callback.message.message_id)
            res = 'да' if f.exists else 'нет'
            await callback.bot.send_message(callback.from_user.id, text=f'Вы выбрали: *{res}*', parse_mode='Markdown')

            await shell.show_choice_menu(callback.from_user.id, kb.generating_filters_choice())
            await state.set_state(GeneratingStates.choosing_filter)

        @staticmethod
        async def kkalories(callback: types.CallbackQuery, state: FSMContext):
            await callback.bot.send_message(callback.from_user.id,
                                            text='Введите *дневное* кол-во ккалорий (примерное):',
                                            parse_mode='Markdown')
            await state.set_state(GeneratingStates.tuning_kkalories)

            await callback.answer()
            await callback.bot.delete_message(callback.message.chat.id, callback.message.message_id)
            # TODO
            pass

        @staticmethod
        async def ready(callback: types.CallbackQuery, state: FSMContext):
            # TODO
            data = await state.get_data()
            filters = data['filters']
            info = 'Вы выбрали следующие фильры:\n'
            for f in filters:
                info += '👉 ' + str(f) + '\n'
            info += 'Подтвердите информацию или измените ее'

            await callback.answer()
            await callback.bot.delete_message(callback.message.chat.id, callback.message.message_id)

            await state.set_state(GeneratingStates.confirming_filters)
            await shell.show_choice_menu(callback.from_user.id, kb.confirm_filters(), info)

            # TODO
            pass

        @staticmethod
        async def confirm(callback: types.CallbackQuery, state: FSMContext):
            await callback.answer()
            await callback.bot.delete_message(callback.message.chat.id, callback.message.message_id)
            if 'edit' in callback.data:
                await state.set_state(GeneratingStates.choosing_filter)
                await shell.show_choice_menu(callback.from_user.id, kb.generating_filters_choice())
            elif 'yes' in callback.data:
                data = await state.get_data()
                filters = data['filters']
                query = qr.GenerateMenu(callback.from_user.id, filters)
                await tr.transmit(query)
                await callback.bot.send_message(callback.from_user.id,
                                                text='Запрос отправлен, пожалуйста, подождите...')
            else:
                await callback.bot.send_message(callback.from_user.id, text='Произошла ошибка ввода. Повторите попытку')

    # TODO
    pass


class Stages:
    # TODO
    pass


def register_all(dp: Dispatcher):
    dp.register_message_handler(TextHandlers.start, commands=['start'], state='*')
    dp.register_message_handler(TextHandlers.help, commands=['help'], state='*')
    dp.register_message_handler(TextHandlers.generate, commands=['generate'], state='*')
    dp.register_message_handler(TextHandlers.GeneratingFiltersChoice.tuning_budget,
                                state=GeneratingStates.tuning_budget)
    dp.register_message_handler(TextHandlers.GeneratingFiltersChoice.tuning_kkalories,
                                state=GeneratingStates.tuning_kkalories)

    dp.register_callback_query_handler(InlineHandlers.GeneratingFiltersChoice.budget, lambda x: x.data == 'budget_btn',
                                       state=GeneratingStates.choosing_filter)
    dp.register_callback_query_handler(InlineHandlers.GeneratingFiltersChoice.snack, lambda x: x.data == 'snack_btn',
                                       state=GeneratingStates.choosing_filter)
    dp.register_callback_query_handler(InlineHandlers.GeneratingFiltersChoice.kkalories,
                                       lambda x: x.data == 'kkalories_btn', state=GeneratingStates.choosing_filter)
    dp.register_callback_query_handler(InlineHandlers.GeneratingFiltersChoice.tuning_snack,
                                       state=GeneratingStates.tuning_snack)
    dp.register_callback_query_handler(InlineHandlers.GeneratingFiltersChoice.ready,
                                       lambda x: x.data == 'ready_btn', state=GeneratingStates.choosing_filter)
    dp.register_callback_query_handler(InlineHandlers.GeneratingFiltersChoice.confirm,
                                       state=GeneratingStates.confirming_filters)

    # TODO
