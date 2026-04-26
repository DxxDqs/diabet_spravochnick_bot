from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Первый тип", callback_data="tip_1"),
         InlineKeyboardButton(text="Второй тип", callback_data="tip_2")]
    ]
)

tip_1 = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Как он появляется?", callback_data="poyavlenye"),
         InlineKeyboardButton(text="Что такое инсулин?", callback_data="insulin")],
        [InlineKeyboardButton(text="Что такое глюкоза?", callback_data="glukoza"),
         InlineKeyboardButton(text="Влияет-ли диабет на физ.нагрузку?", callback_data="fiz_nagruzka")],
        [InlineKeyboardButton(text="В меню", callback_data="menu")]
    ]
)

insulin = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Быстрый инсулин", callback_data="fast_ins"),
         InlineKeyboardButton(text="Медленный инсулин", callback_data="slow_ins")],
        [InlineKeyboardButton(text="Какие есть способы ввода инсулина?", callback_data="sposoby_vvoda"),
         InlineKeyboardButton(text="Назад", callback_data="tip_1")]
    ]
)

tip_2 = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Какие таблетки прописывают врачи?", callback_data="tabletki"),
         InlineKeyboardButton(text="Какая диета ставится?", callback_data="dieta_2")],
        [InlineKeyboardButton(text="В меню", callback_data="menu")]
    ]
)

poyavlenye = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Что такое инсулин?", callback_data="insulin")],
        [InlineKeyboardButton(text="Назад", callback_data="tip_1")]
    ]
)

glukoza = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Что такое гликемический индекс и как он связан с глюкозой?", callback_data="gl_index")],
        [InlineKeyboardButton(text="Насколько строгая диета?", callback_data="dieta")],
        [InlineKeyboardButton(text="Какие бывают уровни глюкозы?", callback_data="level_gl")],
        [InlineKeyboardButton(text="Назад", callback_data="tip_1")]
    ]
)

gl_index = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Высокий гликемический индекс", callback_data="hight_gli"),
         InlineKeyboardButton(text="Средний гликемический индекс", callback_data="avarage_gli"),
         InlineKeyboardButton(text="Низкий гликемический индекс", callback_data="low_gli")],
        [InlineKeyboardButton(text="Назад", callback_data="glukoza")]
    ]
)

dieta = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Что такое гликемический индекс и как он связан с глюкозой?", callback_data="gl_index")],
        [InlineKeyboardButton(text="Назад", callback_data="glukoza")]
    ]
)

fiz_nagruzka = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Высокая интенсивность", callback_data="hight_fiz")],
        [InlineKeyboardButton(text="Средняя/низкая интенсивность", callback_data="low_fiz")],
        [InlineKeyboardButton(text="Противопоказания", callback_data="protivopokaz")],
        [InlineKeyboardButton(text="Назад", callback_data="tip_1")]
    ]
)

tabletki = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Какая диета ставится?", callback_data="dieta_2")],
        [InlineKeyboardButton(text="Назад", callback_data="tip_2")]
    ]
)

dieta_2 = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Какие таблетки прописывают врачи?", callback_data="tabletki")],
        [InlineKeyboardButton(text="Назад", callback_data="tip_2")]
    ]
)

sposoby_vvoda = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Быстрый инсулин", callback_data="fast_ins")],
        [InlineKeyboardButton(text="Медленный инсулин", callback_data="slow_ins")],
        [InlineKeyboardButton(text="Назад", callback_data="insulin")]
    ]
)

level_gl = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Высокий гликемический индекс", callback_data="hight_gli")],
        [InlineKeyboardButton(text="Назад", callback_data="glukoza")]
    ]
)
fast_ins = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Назад", callback_data="insulin")]
    ]
)
slow_ins = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text = "Назад", callback_data="insulin")]
    ]
)
hight_gli = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text = "Назад", callback_data="gl_index")]
    ]
)
avarage_gli = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text = "Назад", callback_data="gl_index")]
    ]
)
low_gli = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text = "Назад", callback_data="gl_index")]
    ]
)
hight_fiz = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text = "Назад", callback_data="fiz_nagruzka")]
    ]
)
low_fiz = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text = "Назад", callback_data="fiz_nagruzka")]
    ]
)
protivopokaz = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text = "Назад", callback_data="fiz_nagruzka")]
    ]
)