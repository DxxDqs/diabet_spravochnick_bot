from aiogram import Router
from aiogram.types import Message
from aiogram.filters.command import CommandStart, Command
import keyboard as kb
user = Router()
@user.message (CommandStart())
async def cmd_start (message: Message):
    await message.answer ("Добро пожаловать в бот, выберите тип диабета, который вас интересует",
                          reply_markup = kb.menu)
@user.message (lambda message: message.text == "Первый тип" )
async def cmd_1_tip (message: Message):
    await message.answer("Первый тип диабета - это болезнь, передающаяся по наследству. На данный момент она никак "
                         "не лечится,больные поддерживают свое здоровье с помощью инъекций инсулина. Выберите, о чем бы "
                         "хотели узнать подробнее",
                         reply_markup = kb.tip_1)
@user.message (lambda message: message.text == "Что такое инсулин?")
async def cmd_insulin (message: Message):
    await message.answer ("Инсулин - гормон, который проводит глюкозу из крови в клетки организма. "
                          "О каком инсулине вы бы хотели узнать?",
                          reply_markup = kb.insulin)
@user.message (lambda message: message.text == "В меню")
async def cmd_menu (message: Message):
    await message.answer ("Добро пожаловать в бот, выберите тип диабета, который вас интересует",
                          reply_markup = kb.menu)
@user.message (lambda message: message.text == "Назад" )
async def cmd_menu_1_tip (message: Message):
    await message.answer("Выберите, что вас интересует",
                         reply_markup = kb.tip_1)
@user.message (lambda message: message.text == "Второй тип")
async def cmd_2_tip (message: Message):
    await message.answer("Второй тип диабета - болезнь, вызванная неправильным образом жизни, плохим питанием и возрастом."
                         "Из-за этих факторов организм перестает воспринимать инсулин (понижается чувствительность к инсулину),"
                         "из-за чего сахар в крови повышается.Второй тип лечится, достаточно соблюдать диету и пить таблетки,"
                         "которые вам назначит врач. Если не соблюдать рекомендации врача, ситуация усугубится, и возмодно придется"
                         "делать инъекции инсулина для понижения сахара",
                         reply_markup = kb.tip_2)
@user.message (lambda message: message.text == "Как он появляется?")
async def cmd_poyavlenye (message: Message):
    await message.answer("У некоторых людей с рождения есть определенный ген, который вызывает диабет. Этот ген включается"
                         "в рандомный момент жизни и уничтожает клетки, вырабатывающие инсулин, из-за чего глюкоза не "
                         "уходит из крови в клетки",
                         reply_markup = kb.poyavlenye)
@user.message (lambda message: message.text == "Что такое глюкоза?")
async def cmd_glukoza (message: Message):
    await message.answer("Глюкоза - углевод, который является основным источником питания для клеток. Глюкоза есть практически"
                         "во всех продуктах, поэтому сахар в крови растет после любой еды",
                         reply_markup = kb.glukoza)
@user.message (lambda message: message.text == "Что такое гликемический индекс и как он связан с глюкозой?")
async def cmd_glick_index (message: Message):
    await message.answer("Гликемический индекс - показатель того, насколько быстро усваиваются продукты. Есть низкий, средний"
                         "и высокий гликемический индекс",
                         reply_markup = kb.gl_index)
@user.message (lambda message: message.text == "Насколько строгая диета при диабете?")
async def cmd_dieta (message: Message):
    await message.answer("При диабете вы можете есть абсолютно любой продукт, главное учитывать количество углеводов "
                         "этого продукта и его гликемический индекс, и исходя из этих данных вводить нужную дозу инсулина"
                         "(доза инсулина обговаривается с врачом)",
                         reply_markup = kb.dieta)
@user.message (lambda message: message.text == "Влияет-ли диабет на физ.нагрузку?")
async def cmd_fiz_nagruzka (message: Message):
    await message.answer("Да, влияет на сахар в крови. Есть некоторые противопоказания, а также влияние зависит от "
                         "интенсивности нагрузки",
                         reply_markup = kb.fiz_nagruzka)
@user.message (lambda message: message.text == "Быстрый инсулин")
async def cmd_fast_insulin (message: Message):
    await message.answer("Инсулин, который начинает действовать в течении 15-30 минут после введения. Используется "
                         "перед приемами пищи или для понижения уровня глюкозы",
                         reply_markup = kb.back)
@user.message (lambda message: message.text == "Медленный инсулин")
async def cmd_slow_insulin (message: Message):
    await message.answer("Инсулин, действующий на протяжении 12 часов или более, используется для поддержания уровня"
                         "глюкозы",
                         reply_markup = kb.back)
@user.message (lambda message: message.text == "Высокий гликемический индекс")
async def cmd_hight_glick_index (message: Message):
    await message.answer("Высокий гликемический индекс обозначает, что продукт усваивается в течении часа и вызывает"
                         "резкий подъем сахара. На такие продукты инсулин нужно вводить заранее (паузу нужно обсудить "
                         "с лечащим врачом). Примеры таких продуктов: картофель, выпечка из пшеницы, любая сладость, в "
                         "которой есть сахар в прямом виде",
                         reply_markup = kb.back)
@user.message (lambda message: message.text == "Средний гликемический индекс")
async def cmd_avarage_glick_index (message: Message):
    await message.answer("Средний гликемический индекс обозначает, что продукт усваивается в течении 2 часов, умеренно"
                         "поднимает сахар, так что нет нужды вводить перед ними инсулин заранее. Примеры таких продуктов:"
                         "цельнозерновой хлеб, различные крупы, каши",
                         reply_markup = kb.back)
@user.message (lambda message: message.text == "Низкий гликемический индекс")
async def cmd_low_glick_index (message: Message):
    await message.answer("Низкий гликемический индекс обозначает, что продукт усваивается за 3 или более часов, медленно"
                         "поднимает сахар, так что перед ними вообще ненужно вводить инсулин. Примеры таких продуктов:"
                         "любые овощи, кроме картофеля и кукурузы, творог, многие орехи (миндаль, грецкий орех и др.)",
                         reply_markup = kb.back)
@user.message (lambda message: message.text == "Влияние на сахар при высокой интенсивности")
async def hight_intens (message: Message):
    await message.answer("Если вы проведете тренировку с тяжелой нагрузкой, сахар в вашей крови может подняться. Это нормально,"
                         "через какое-то время он сам спадет. Это происходит из-за выброса запасов глюкозы из печени",
                         reply_markup = kb.back)
@user.message (lambda message: message.text == "Влияние на сахар при средней/низкой интенсивности")
async def avarage_low_intens (message: Message):
    await message.answer("Если вы проведете тренировку с легкой нагрузкой, либо же просто пройдете какое-то расстояние"
                         "пешком, сахар в вашей крови может опуститься. Нужно следить за его уровнем и в случае чего поднять."
                         "Это происходит, потому что при долгой легкой активности увеличивается чувствительность к инсулину",
                         reply_markup = kb.back)
@user.message (lambda message: message.text == "Какие есть противопоказания?")
async def protivopokazaniya (message: Message):
    await message.answer("Нельзя заниматься тяжелой физ. нагрузкой при сахаре выше 15, потому что сахар может подняться"
                         "слишком высоко, он навредит вашему самочувствию и повредит сосуды",
                         reply_markup = kb.back)
@user.message (lambda message: message.text == "Какие таблетки прописывают врачи?")
async def tabletki (message: Message):
    await message.answer("Как правило, врач прописывает таблетки, которые повышают чувствительность к инсулину и повышают "
                         "его выработку. Одни таблетки не помогут вам вылечить диабет, также нужно соблюдать диету",
                         reply_markup = kb.tabletki)
@user.message (lambda message: message.text == "Какая диета ставится?")
async def tabletki (message: Message):
    await message.answer("Обычно в таких диетах из рациона исключаются жирные продукты, выпечка и сладкое",
                         reply_markup = kb.dieta_2)
@user.message (lambda message: message.text == "Какие есть способы ввода инсулина?")
async def sposoby_vvoda (message: Message):
    await message.answer("Инсулин можно вводить двумя способами: с помощью шприца, либо же с помощью помпы. Помпа - устройство,"
                         "которое может вводить инсулин без помощи шприцов.которое с помощью постоянного ввода маленьких "
                         "доз быстрого инсулина симулирует длинный инсулин, благодаря чему вам не придется его вводить.",
                         reply_markup = kb.sposoby_vvoda)
@user.message (lambda message: message.text == "Какие бывают уровни глюкозы в крови?")
async def cmd_level_glukoza (message: Message):
    await message.answer("Глюкоза в крови может быть повышенной (гипергликемия), ее нужно понизить инсулином, в норме и "
                         "пониженной (гипогликемия), ее нужно повысить с помощью углеводов с быстрым гликемическим индексом",
                         reply_markup = kb.level_gl)
@user.message ()
async def unknow_message (message: Message):
    await message.answer("Такого запроса нету в боте, используйте встроенную клавиатуру,чтобы не возникло ошибок",
                         reply_markup = kb.menu)
