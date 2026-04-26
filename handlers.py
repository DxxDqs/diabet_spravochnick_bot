from aiogram import Router, F
from aiogram.types import Message,CallbackQuery
from aiogram.filters.command import CommandStart
from aiogram.exceptions import TelegramBadRequest
import keyboard as kb

user = Router()
@user.message(CommandStart())
async def cmd_start (message: Message):
    await message.answer ("Добро пожаловать в бот, выберите тип диабета, который вас интересует",
                          reply_markup = kb.menu)
@user.callback_query (lambda call: call.data == "tip_1")
async def cmd_1_tip (callback: CallbackQuery):
    try:
        await callback.message.edit_text(
            text = "Первый тип диабета - это болезнь, передающаяся по наследству. На данный момент она никак "
            "не лечится,больные поддерживают свое здоровье с помощью инъекций инсулина. Выберите, о чем бы "
            "хотели узнать подробнее",
            reply_markup = kb.tip_1)
    except TelegramBadRequest:
        pass
    await callback.answer()
@user.callback_query(lambda call: call.data == "insulin")
async def cmd_insulin (callback: CallbackQuery):
    try:
        await callback.message.edit_text (
            text = "Инсулин - гормон, который проводит глюкозу из крови в клетки организма. "
            "О каком инсулине вы бы хотели узнать?",
            reply_markup = kb.insulin)
    except TelegramBadRequest:
        pass
    await callback.answer()
@user.callback_query (lambda call: call.data == "menu")
async def cmd_menu (callback: CallbackQuery):
    try:
        await callback.message.edit_text (
            text ="Добро пожаловать в бот, выберите тип диабета, который вас интересует",
            reply_markup = kb.menu)
    except TelegramBadRequest:
        pass
    await callback.answer()
@user.callback_query (lambda call: call.data == "tip_2")
async def cmd_2_tip (callback: CallbackQuery):
    try:
        await callback.message.edit_text(
            text = "Второй тип диабета - болезнь, вызванная неправильным образом жизни, плохим питанием и возрастом."
            "Из-за этих факторов организм перестает воспринимать инсулин (понижается чувствительность к инсулину),"
            "из-за чего сахар в крови повышается.Второй тип лечится, достаточно соблюдать диету и пить таблетки,"
            "которые вам назначит врач. Если не соблюдать рекомендации врача, ситуация усугубится, и возмодно придется"
            "делать инъекции инсулина для понижения сахара",
            reply_markup = kb.tip_2)
    except TelegramBadRequest:
        pass
    await callback.answer()
@user.callback_query (lambda call: call.data == "poyavlenye")
async def cmd_poyavlenye (callback: CallbackQuery):
    try:
        await callback.message.edit_text(
            text = "У некоторых людей с рождения есть определенный ген, который вызывает диабет. Этот ген включается"
            "в рандомный момент жизни и уничтожает клетки, вырабатывающие инсулин, из-за чего глюкоза не "
            "уходит из крови в клетки",
            reply_markup = kb.poyavlenye)
    except TelegramBadRequest:
        pass
    await callback.answer()
@user.callback_query (lambda call: call.data == "glukoza")
async def cmd_glukoza (callback: CallbackQuery):
    try:
        await callback.message.edit_text(
            text = "Глюкоза - углевод, который является основным источником питания для клеток. Глюкоза есть практически"
            "во всех продуктах, поэтому сахар в крови растет после любой еды",
            reply_markup = kb.glukoza)
    except TelegramBadRequest:
        pass
    await callback.answer()
@user.callback_query (lambda call: call.data == "gl_index")
async def cmd_glick_index (callback: CallbackQuery):
    try:
        await callback.message.edit_text(
            text = "Гликемический индекс - показатель того, насколько быстро усваиваются продукты. Есть низкий, средний"
            "и высокий гликемический индекс",
            reply_markup = kb.gl_index)
    except TelegramBadRequest:
        pass
    await callback.answer()
@user.callback_query (lambda call: call.data == "dieta")
async def cmd_dieta (callback: CallbackQuery):
    try:
        await callback.message.edit_text(
            text = "При диабете вы можете есть абсолютно любой продукт, главное учитывать количество углеводов "
            "этого продукта и его гликемический индекс, и исходя из этих данных вводить нужную дозу инсулина"
            "(доза инсулина обговаривается с врачом)",
            reply_markup = kb.dieta)
    except TelegramBadRequest:
        pass
    await callback.answer()
@user.callback_query (lambda call: call.data == "fiz_nagruzka")
async def cmd_fiz_nagruzka (callback: CallbackQuery):
    try:
        await callback.message.edit_text(
            text = "Да, влияет на сахар в крови. Есть некоторые противопоказания, а также влияние зависит от "
            "интенсивности нагрузки",
            reply_markup = kb.fiz_nagruzka)
    except TelegramBadRequest:
        pass
    await callback.answer()
@user.callback_query (lambda call: call.data == "fast_ins")
async def cmd_fast_insulin (callback: CallbackQuery):
    try:
        await callback.message.edit_text(
            text = "Инсулин, который начинает действовать в течении 15-30 минут после введения. Используется "
            "перед приемами пищи или для понижения уровня глюкозы",
            reply_markup = kb.fast_ins)
    except TelegramBadRequest:
        pass
    await callback.answer()
@user.callback_query (lambda call: call.data == "slow_ins")
async def cmd_slow_insulin (callback: CallbackQuery):
    try:
        await callback.message.edit_text(
            text = "Инсулин, действующий на протяжении 12 часов или более, используется для поддержания уровня глюкозы",
            reply_markup = kb.slow_ins)
    except TelegramBadRequest:
        pass
    await callback.answer()
@user.callback_query (lambda call: call.data == "hight_gli")
async def cmd_hight_glick_index (callback: CallbackQuery):
    try:
        await callback.message.edit_text(
            text = "Высокий гликемический индекс обозначает, что продукт усваивается в течении часа и вызывает"
            "резкий подъем сахара. На такие продукты инсулин нужно вводить заранее (паузу нужно обсудить "
            "с лечащим врачом). Примеры таких продуктов: картофель, выпечка из пшеницы, любая сладость, в "
            "которой есть сахар в прямом виде",
            reply_markup = kb.hight_gli)
    except TelegramBadRequest:
        pass
    await callback.answer()
@user.callback_query (lambda call: call.data == "avarage_gli")
async def cmd_avarage_glick_index (callback: CallbackQuery):
    try:
        await callback.message.edit_text(
            text = "Средний гликемический индекс обозначает, что продукт усваивается в течении 2 часов, умеренно"
            "поднимает сахар, так что нет нужды вводить перед ними инсулин заранее. Примеры таких продуктов:"
            "цельнозерновой хлеб, различные крупы, каши",
            reply_markup = kb.avarage_gli)
    except TelegramBadRequest:
        pass
    await callback.answer()
@user.callback_query (lambda call: call.data == "low_gli")
async def cmd_low_glick_index (callback: CallbackQuery):
    try:
        await callback.message.edit_text(
            text = "Низкий гликемический индекс обозначает, что продукт усваивается за 3 или более часов, медленно"
            "поднимает сахар, так что перед ними вообще ненужно вводить инсулин. Примеры таких продуктов:"
            "любые овощи, кроме картофеля и кукурузы, творог, многие орехи (миндаль, грецкий орех и др.)",
            reply_markup = kb.low_gli)
    except TelegramBadRequest:
        pass
    await callback.answer()
@user.callback_query (lambda call: call.data == "hight_fiz")
async def cmd_hight_intens (callback: CallbackQuery):
    try:
        await callback.message.edit_text(
            text = "Если вы проведете тренировку с тяжелой нагрузкой, сахар в вашей крови может подняться. Это нормально,"
            "через какое-то время он сам спадет. Это происходит из-за выброса запасов глюкозы из печени",
            reply_markup = kb.hight_fiz)
    except TelegramBadRequest:
        pass
    await callback.answer()
@user.callback_query (lambda call: call.data == "low_fiz")
async def cmd_avarage_low_intens (callback: CallbackQuery):
    try:
        await callback.message.edit_text(
            text = "Если вы проведете тренировку с легкой нагрузкой, либо же просто пройдете какое-то расстояние"
            "пешком, сахар в вашей крови может опуститься. Нужно следить за его уровнем и в случае чего поднять."
            "Это происходит, потому что при долгой легкой активности увеличивается чувствительность к инсулину",
            reply_markup = kb.low_fiz)
    except TelegramBadRequest:
        pass
    await callback.answer()
@user.callback_query (lambda call: call.data == "protivopokaz")
async def cmd_protivopokazaniya (callback: CallbackQuery):
    try:
        await callback.message.edit_text(
            text = "Нельзя заниматься тяжелой физ. нагрузкой при сахаре выше 15, потому что сахар может подняться"
            "слишком высоко, он навредит вашему самочувствию и повредит сосуды",
            reply_markup = kb.protivopokaz)
    except TelegramBadRequest:
        pass
    await callback.answer()
@user.callback_query (lambda call: call.data == "tabletki")
async def cmd_tabletki (callback: CallbackQuery):
    try:
        await callback.message.edit_text(
            text = "Как правило, врач прописывает таблетки, которые повышают чувствительность к инсулину и повышают "
            "его выработку. Одни таблетки не помогут вам вылечить диабет, также нужно соблюдать диету",
            reply_markup = kb.tabletki)
    except TelegramBadRequest:
        pass
    await callback.answer()
@user.callback_query (lambda call: call.data == "dieta_2")
async def cmd_dieta_2 (callback: CallbackQuery):
    try:
        await callback.message.edit_text(
            text = "Обычно в таких диетах из рациона исключаются жирные продукты, выпечка и сладкое",
            reply_markup = kb.dieta_2)
    except TelegramBadRequest:
        pass
    await callback.answer()
@user.callback_query (lambda call: call.data == "sposoby_vvoda")
async def cmd_sposoby_vvoda (callback: CallbackQuery):
    try:
        await callback.message.edit_text(
            text = "Инсулин можно вводить двумя способами: с помощью шприца, либо же с помощью помпы. Помпа - устройство,"
            "которое может вводить инсулин без помощи шприцов.которое с помощью постоянного ввода маленьких "
            "доз быстрого инсулина симулирует длинный инсулин, благодаря чему вам не придется его вводить.",
            reply_markup = kb.sposoby_vvoda)
    except TelegramBadRequest:
        pass
    await callback.answer()
@user.callback_query(lambda call: call.data == "level_gl")
async def cmd_level_glukoza (callback: CallbackQuery):
    try:
        await callback.message.edit_text(
            text = "Глюкоза в крови может быть повышенной (гипергликемия), ее нужно понизить инсулином, в норме и "
            "пониженной (гипогликемия), ее нужно повысить с помощью углеводов с быстрым гликемическим индексом",
            reply_markup = kb.level_gl)
    except TelegramBadRequest:
        pass
    await callback.answer()
@user.message()
async def cmd_unknow_message (message: Message):
    await message.answer(
        text = "Используй кнопки, встроенные в бота",
        reply_markup = kb.menu
    )