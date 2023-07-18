def start():
    text = 'Привет! Это *mealner* - бот, который поможет с составлением меню!\nНапиши /help, чтобы получить список комманд!'
    parse_mode = 'Markdown'
    return [text, parse_mode]


def help():
    text = '*Список комманд:*\n' \
           '💥 /generate - сгенерировать меню по вашим запросам\n' \
           '💥 /list - получить список покупок для текущего меню\n' \
           '💥 /adddish - добавить свое блюдо в базу данных\n' \
           '💥 /addproduct - добавить свой продукт в базу данных\n' \
           '💥 /profile - ваш профиль'
    parse_mode = 'Markdown'
    return [text, parse_mode]

# TODO