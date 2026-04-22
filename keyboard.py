from aiogram.types import ReplyKeyboardMarkup, KeyboardButton



menu = ReplyKeyboardMarkup(
    keyboard = [
        [KeyboardButton(text = "Первый тип"),
         KeyboardButton (text = "Второй тип")]
    ],
    resize_keyboard = True
)
tip_1 = ReplyKeyboardMarkup(
    keyboard = [
        [KeyboardButton(text = "Как он появляется?"),
         KeyboardButton(text = "Что такое инсулин?")],
         [KeyboardButton (text = "Что такое глюкоза?"),
         KeyboardButton (text = "Влияет-ли диабет на физ.нагрузку?")],
        [KeyboardButton(text = "В меню")]
    ],
    resize_keyboard = True
)
insulin = ReplyKeyboardMarkup(
    keyboard = [
    [KeyboardButton(text = "Быстрый инсулин"),
     KeyboardButton(text = "Медленный инсулин")],
    [KeyboardButton(text = "Какие есть способы ввода инсулина?"),
     KeyboardButton(text = "Назад")]
     ],
    resize_keyboard=True
)
tip_2 = ReplyKeyboardMarkup(
    keyboard = [
    [KeyboardButton(text = "Какие таблетки прописывают врачи?"),
     KeyboardButton(text = "Какая диета ставится?")],
    [KeyboardButton(text = "В меню")]
    ],
    resize_keyboard = True
)
poyavlenye = ReplyKeyboardMarkup(
    keyboard = [
        [KeyboardButton(text = "Что такое инсулин?")],
        [KeyboardButton(text ="Назад")]
    ],
    resize_keyboard = True
)
back = ReplyKeyboardMarkup(
    keyboard = [
        [KeyboardButton(text = "Назад")]
    ],
    resize_keyboard = True
)
glukoza = ReplyKeyboardMarkup(
    keyboard = [
        [KeyboardButton(text = "Что такое гликемический индекс и как он связан с глюкозой?"),
        KeyboardButton(text = "Насколько строгая диета при диабете?")],
        [KeyboardButton(text = "Назад")]
    ],
    resize_keyboard = True
)
gl_index = ReplyKeyboardMarkup(
    keyboard = [
        [KeyboardButton(text = "Высокий гликемический индекс"),
         KeyboardButton(text = "Средний гликемический индекс"),
         KeyboardButton(text = "Низкий гликемический индекс")],
        [KeyboardButton(text = "Назад")]
    ],
    resize_keyboard = True
)
dieta = ReplyKeyboardMarkup(
    keyboard = [
        [KeyboardButton(text = "Что такое гликемический индекс и как он связан с глюкозой?"),
         KeyboardButton(text = "Назад")]
    ],
    resize_keyboard = True
)
fiz_nagruzka = ReplyKeyboardMarkup(
    keyboard = [
        [KeyboardButton(text = "Влияние на сахар при высокой интенсивности"),
         KeyboardButton(text = "Влияние на сахар при средней/низкой интенсивности")],
        [KeyboardButton(text = "Какие есть противопоказания?"),
         KeyboardButton(text = "Назад")]
    ],
    resize_keyboard = True
)
tabletki = ReplyKeyboardMarkup(
    keyboard = [
    [KeyboardButton(text = "Какая диета ставится?")],
    [KeyboardButton(text = "В меню")]
    ],
    resize_keyboard = True
)
dieta_2 = ReplyKeyboardMarkup(
    keyboard = [
    [KeyboardButton(text = "Какие таблетки прописывают врачи?")],
    [KeyboardButton(text = "В меню")]
    ],
    resize_keyboard = True
)
sposoby_vvoda = ReplyKeyboardMarkup(
    keyboard = [
        [KeyboardButton(text = "Быстрый инсулин")],
        [KeyboardButton(text = "Медленный инсулин")],
        [KeyboardButton(text = "Назад")]
    ],
    resize_keyboard = True
)
level_gl = ReplyKeyboardMarkup(
    keyboard = [
        [KeyboardButton(text = "Высокий гликемический индекс"),
         KeyboardButton(text = "Назад")]
    ],
    resize_keyboard = True
)
