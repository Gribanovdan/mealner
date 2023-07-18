def start():
    text = 'Привет! Этот *mealner* - бот, который поможет с составлением меню!'
    parse_mode = 'Markdown'
    return [text, parse_mode]


def help():
    return start

# TODO