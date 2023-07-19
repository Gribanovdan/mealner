from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


class GeneratingStates(StatesGroup):
    choosing_filter = State()
    tuning_budget = State()
    tuning_snack = State()
    tuning_kkalories = State()
    confirming_filters = State()