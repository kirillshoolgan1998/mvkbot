from aiogram import Bot, Dispatcher, types, executor

bot = Bot(token="5306815029:AAFjQF71wkC7XnXmOUPEp_k7G6oSp-KeZh8")
dp = Dispatcher(bot)

StendKB = "КОМЕНДАНТСКИЙ БАТАЛЬОН МИНСКОЙ ВОЕННОЙ КОМЕНДАТУРЫ \n \nВ соответствии с директивой Министра обороны Республики Беларусь №Д-5 от 12.02.2009 года в штат военной комендатуры 30.04.2009 года был введен КОМЕНДАНТСКИЙ БАТАЛЬОН, в состав которого вошли рота почетного караула, рота караульной службы, патрульная рота и автомобильный взвод."
StendMVK = "МИНСКАЯ ВОЕННАЯ КОМЕНДАТУРА \n \nМинская военная комендатура была сформирована 30 ноября 1917 года приказом №1 главнокомандующим армиями Западного фронта А.Ф. Мясниковым в целях наведения порядка в городе. Размещалась тогда комендатура на площади Свободы, 4.\nВ период оккупации немцами города Минска, военная комендатура Минского гарнизона прекратила свою деятельность. После освобождения Минска 3 июля 1944 года было сформировано управление военного коменданта города Минска.\nВ 1984 году управление военного коменданта города Минска было переведено на штат военной комендатуры 1-го разряда и было переименовано в военную комендатуру Минского гарнизона.\nВ августе 1995 года комендатура была переформирована в Главную военную комендатуру Вооруженных Сил. Тогда в ее состав вошли рота почетного караула и патрульная рота (бывшая комендантская рота).\nВ 2014 году Главная военная комендатура Вооруженных Сил была переименована в Военную комендатуру Вооруженных Сил.\nВ 2018 году Военная комендатура Вооруженных Сил была переименована в Минскую военную комендатуру."
StendRPK = "РОТА ПОЧЕТНОГО КАРАУЛА КОМЕНДАНТСКОГО БАТАЛЬОНА МИНСКОЙ ВОЕННОЙ КОМЕНДАТУРЫ \n \nНа основании приказа Министра обороны Республики Беларусь №5/349 от 17 февраля 1995 года была образована РОТА ПОЧЕТНОГО КАРАУЛА. До ее создания функцию почетного караула выполняли курсанты Минского военного инженерного зенитно-ракетного училища и Минского высшего военно-командного училища, на базе которых позднее была создана Военная академия Республики Беларусь. В сферу задач роты входило встреча глав государств и правительственных делегаций, участия в общегосударственных мероприятиях, торжествах возле мемориалов, возложении венков к памятникам и обелискам, отдания воинских почестей при погребении известных государственных деятелей. Первое боевое крещение РОТА ПОЧЕТНОГО КАРАУЛА прошла на праздновании Дня Независимости 27 июля 1995 года. Следующие мероприятия роты касались встречи и проводов министров обороны ведомств разных государств.\nВ 2004 году Указом Президента Республики Беларусь №407 от 26 августа 2004 года была образована СВОДНАЯ РОТА ПОЧЕТНОГО КАРАУЛА, состоящая из военнослужащих Вооруженных Сил, Государственного пограничного комитета и Министерства внутренних дел. В соответствии с докладной запиской Министра обороны Республики Беларусь от 05.03.2018 года №23/423 была создана ВТОРАЯ РОТА ПОЧЕТНОГО КАРАУЛА."
StendRKS = "РОТА КАРАУЛЬНОЙ СЛУЖБЫ КОМЕНДАНТСКОГО БАТАЛЬОНА МИНСКОЙ ВОЕННОЙ КОМЕНДАТУРЫ \n \nВ соответствии с директивой №17 Министерства обороны Республики Беларусь от 11 марта 2002 года и перечнем изменений к штату главной военной комендатуры Вооруженных Сил №34/013 от 16 апреля 2002 года приказом ВС №77 от 5 июля 2002 года на базе патрульной роты и роты почетного караула, а также подразделений комендатур гарнизонов Вооруженных Сил была сформирована РОТА КАРАУЛЬНОЙ СЛУЖБЫ Главной военной комендатуры Вооруженных Сил. Первое заступление, для несения службы в карауле состоялось 15 сентября 2002 года."
StendPR = "ПАТРУЛЬНАЯ РОТА КОМЕНДАНТСКОГО БАТАЛЬОНА МИНСКОЙ ВОЕННОЙ КОМЕНДАТУРЫ \n \n12 декабря 1994 года, приказом Министра обороны Республики Беларусь №555 на базе роты особого назначения 1-го мотострелкового батальона 339-го гвардейского полка 120-й гваржейской механизированной дивизии была сформирована комендантская рота военной комендатуры Минского гарнизона. В этот же месяц рота приступила к выполнению поставленных ей задач.\nВ августе 1995 года комендатура была переформирована в Главную военную комендатуру ВС РБ, в комендантская рота военной комендатуры Минского гарнизона переименована в ПАТРУЛЬНУЮ РОТУ Главной военной комендатуры."
StendOPK = "ОРКЕСТР ПОЧЕТНОГО КАРАУЛА МИНСКОЙ ВОЕННОЙ КОМЕНДАТУРЫ\n \n1 июля 1995 года приказом Министра обороны был создан оркестр Минской военной комендатуры, тогда он назывался оркестром Главной военной комендатуры Вооружённых Сил Республики Беларусь. С момента формирования оркестра и на протяжении почти одиннадцати лет его начальником являлся подполковник Костюченко Сергей Николаевич.\nНеотъемлемым для этого коллектива является выполнение множества сложных и ответственных задач совместно с ротой почётного караула:  встреча глав государств и правительственных делегаций, участие в общегосударственных мероприятиях и торжествах возле мемориалов. Также в сферу задач оркестра входит: участие в возложении венков от высокопоставленных государственных особ к памятникам и обелискам, отдании воинских почестей при погребении известных государственных деятелей, в том числе обеспечение проведения на высоком идейном уровне важных событий государственного и военного значения.\nЯвляясь профессионально-творческим коллективом, по средствам музыкального искусства оркестр минской военной комендатуры содействует воспитанию и повышению культурного и эстетического уровня военнослужащих Вооруженных Сил и населения города Минска.\nВ основу репертуара оркестра входят высокохудожественные произведения на героическую и военно-патриотическую темы, лучшие образцы белорусской, русской и зарубежной музыки."
StendVAI = "ВОЕННАЯ АВТОМОБИЛЬНАЯ ИНСПЕКЦИЯ МИНСКОЙ ВОЕННОЙ КОМЕНДАТУРЫ"
StendODIR = "ОТДЕЛ ДОЗНАНИЯ И РОЗЫСКА МИНСКОЙ ВОЕННОЙ КОМЕНДАТУРЫ"
StendTSO = "ОТДЕЛ ОСНАЩЕНИЯ И РЕГЛАМЕНТА ТЕХНИЧЕСКИХ СИСТЕМ И СРЕДСТВ ОХРАНЫ МИНСКОЙ ВОЕННОЙ КОМЕНДАТУРЫ"


InfoKB = "КОМЕНДАНТСКИЙ БАТАЛЬОН МИНСКОЙ ВОЕННОЙ КОМЕНДАТУРЫ\n \nКомандир комендантского батальона\nмайор Гордынец С.И.\n \nНачальник штаба - первый заместитель командира батальона\nкапитан Вишневецкий Д.В.\n \nЗаместитель командира батальона по идеологической работе\nкапитан Сахарчук Ю.А.\n \nКомандир первой роты почетного караула\nкапитан Корчинский К.И.\n \nКомандир второй роты почетного караула\nкапитан Фицнер Р.Д.\n \nКомандир роты караульной службы\nкапитан Тарасевич А.А.\n \nКомандир патрульной роты\nстарший лейтенант Шеменев Д.Ю.\n \nКомандир автомобильного взвода\nстарший прапорщик Мандрик В.А."
InfoOPK = "ОРКЕСТР ПОЧЕТНОГО КАРАУЛА МИНСКОЙ ВОЕННОЙ КОМЕНДАТУРЫ\n \nНачальник оркестра почетного караула\nстарший лейтенант Купреев И.С.\n \nЗаместитель начальника оркестра - военный дирижер\nлейтенант Муравьев А.А."
InfoVAI = "ВОЕННАЯ АВТОМОБИЛЬНАЯ ИНСПЕКЦИЯ МИНСКОЙ ВОЕННОЙ КОМЕНДАТУРЫ\n \nНачальник инспекции\nмайор Чикида А.М.\n \nЗаместитель начальника инспекции - начальник группы дорожно-патрульной службы\nкапитан Кондратьев А.А.\n \nНачальник группы государственного технического осмотра\nмайор Гуринович В.А.\n \nНачальник группы регистрации транспортных средств\nмайор Бильман Д.А."
InfoODIR = "ОТДЕЛ ДОЗНАНИЯ И РОЗЫСКА МИНСКОЙ ВОЕННОЙ КОМЕНДАТУРЫ\n \nНачальник отдела\nмайор юстиции Марук А.Н.\n \nЗаместитель начальника отдела\nкапитан юстиции Глушковский Е.О."
InfoTSO = "ОТДЕЛ ОСНАЩЕНИЯ И РЕГЛАМЕНТА ТЕХНИЧЕСКИХ СИСТЕМ И СРЕДСТВ ОХРАНЫ МИНСКОЙ ВОЕННОЙ КОМЕНДАТУРЫ\n \nНачальник отдела\nмайор Адаменко А.А.\n \nСтарший офицер группы\nкапитан Красовский А.С."

Podrazdeleniya = ""
CommandSet = "Командование Минской военной комендатуры: \n \nВоенный комендант\nподполковник Жуковский Д.В. \n \nНачальник штаба - первый заместитель военного коменданта\nподполковник Гудожников С.Н.\n \nЗаместитель военного коменданта\nподполковник Хохлов А.С.\n \nЗаместитель военного коменданта по идеологической работе\nкапитан Божичко С.И.\n \nЗаместитель военного коменданта по материально-техническому обеспечению\nкапитан Последний Д.В."

#==========================(СООБЩЕНИЯ ПОЛЬЗОВАТЕЛЯ)==============================#
@dp.message_handler(commands="start")
async def cmd1(message: types.Message): #первое сообщение бота
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="История", callback_data="History"), types.InlineKeyboardButton(text="Командование", callback_data="CommandSet"))
    keyboard.add(types.InlineKeyboardButton(text="Наши новости", callback_data="News"))
    await message.answer("Здравствуйте, чем я могу помочь?", reply_markup=keyboard)
#==========================(СООБЩЕНИЯ ПОЛЬЗОВАТЕЛЯ)==============================#


#==========================(КАЛЛБЭК КНОПОК)==============================#
@dp.callback_query_handler(text="Start")
async def cmd1(call: types.CallbackQuery): #Начало
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="История", callback_data="History"), types.InlineKeyboardButton(text="Командование", callback_data="CommandSet"))
    keyboard.add(types.InlineKeyboardButton(text="Наши новости", callback_data="News"))
    await call.message.edit_text("Здравствуйте, чем я могу помочь?", reply_markup=keyboard)
    await call.answer()

@dp.callback_query_handler(text="News")
async def cmd1(call: types.CallbackQuery): #Новости
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Телеграм-канал Минской военной комендатуры", url="t.me/VK_Minsk"))
    keyboard.add(types.InlineKeyboardButton(text="Сайт МО РБ", url="https://www.mil.by/ru/"), types.InlineKeyboardButton(text="Instagram МО РБ", url="https://www.instagram.com/army__by/"), types.InlineKeyboardButton(text="Twitter МО РБ", url="https://twitter.com/MOD_BY"))
    keyboard.add(types.InlineKeyboardButton(text='<< Назад <<', callback_data="Start"))
    await call.message.edit_text("Больше информации:", reply_markup=keyboard)
    await call.answer()

@dp.callback_query_handler(text="History")
async def next(call: types.CallbackQuery): #История
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text='Минская ВК', callback_data="MVK"))
    keyboard.add(types.InlineKeyboardButton(text='Рота почетного караула', callback_data="RPK"))
    keyboard.add(types.InlineKeyboardButton(text='Рота караульной службы', callback_data="RKS"))
    keyboard.add(types.InlineKeyboardButton(text='Патрульная рота', callback_data="PR"))
    keyboard.add(types.InlineKeyboardButton(text='Оркестр почетного караула', callback_data="OPK"))
    keyboard.add(types.InlineKeyboardButton(text='Военная автомобильная инспекция', callback_data="VAI"))
    keyboard.add(types.InlineKeyboardButton(text='Отдел дознания и розыска', callback_data="ODIR"))
    keyboard.add(types.InlineKeyboardButton(text='Отдел оснащения и регламента технических систем и средств охраны', callback_data="TSO"))
    keyboard.add(types.InlineKeyboardButton(text='<< Назад <<', callback_data="Start"))
    await call.message.edit_text("Выберите, о чем хотите узнать:", reply_markup=keyboard)
    await call.answer()

@dp.callback_query_handler(text="CommandSet")
async def next(call: types.CallbackQuery): #История
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text='Подразделения МВК', callback_data="Podrazdeleniya"))
    keyboard.add(types.InlineKeyboardButton(text='<< Назад <<', callback_data="Start"))
    await call.message.edit_text(CommandSet, reply_markup=keyboard)
    await call.answer()

#--------------------(КОМАНДОВАНИЕ)-------------------------#
@dp.callback_query_handler(text="Podrazdeleniya")
async def next(call: types.CallbackQuery): #История
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text='Комендантский батальон', callback_data="InfoKB"))
    keyboard.add(types.InlineKeyboardButton(text='Оркестр почетного караула', callback_data="InfoOPK"))
    keyboard.add(types.InlineKeyboardButton(text='Военная автомобильная инспекция', callback_data="InfoVAI"))
    keyboard.add(types.InlineKeyboardButton(text='Отдел дознания и розыска', callback_data="InfoODIR"))
    keyboard.add(types.InlineKeyboardButton(text='Отдел оснащения и регламента технических систем и средств охраны', callback_data="InfoTSO"))
    keyboard.add(types.InlineKeyboardButton(text='<< Назад <<', callback_data="CommandSet"))
    await call.message.edit_text("О каком подразделении Вам хотелось бы узнать?", reply_markup=keyboard)
    await call.answer()
#--------------------(КОМАНДОВАНИЕ)-------------------------#

#--------------------(ИСТОРИЯ)-------------------------#
@dp.callback_query_handler(text="MVK")
async def next(call: types.CallbackQuery): #Минская ВК
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text='<< Назад <<', callback_data="History"), types.InlineKeyboardButton(text='НА ГЛАВНУЮ', callback_data="Start"))
    await call.message.edit_text( f'{StendMVK}[.]({"https://sun9-83.userapi.com/s/v1/ig2/gx8eTh-M2uwIRE7X8X5_23jDaevCEHqgcm9nc7wyp-ka5tLzJjf3CPgKmz62XAkhZcq7-a7arorCD7qYRMSIskTz.jpg?size=1280x853&quality=95&type=album"})', reply_markup=keyboard, parse_mode='markdown')
    await call.answer()

@dp.callback_query_handler(text="RPK")
async def next(call: types.CallbackQuery): #РПК
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text='<< Назад <<', callback_data="History"), types.InlineKeyboardButton(text='НА ГЛАВНУЮ', callback_data="Start"))
    await call.message.edit_text( f'{StendRPK}[.]({"https://sun9-38.userapi.com/s/v1/ig2/VqT9cvwgpODmrydYnHN28tXa5c0-DT4cJKctGVv5jCsfLzh6Hm8awlLmVQ3Ro-YWXHG8qHwxkffRbn1FtXRiKj0I.jpg?size=1920x1080&quality=95&type=album"})', reply_markup=keyboard, parse_mode='markdown')
    await call.answer()

@dp.callback_query_handler(text="RKS")
async def next(call: types.CallbackQuery): #Минская ВК
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text='<< Назад <<', callback_data="History"), types.InlineKeyboardButton(text='НА ГЛАВНУЮ', callback_data="Start"))
    await call.message.edit_text( f'{StendRKS}[.]({"https://sun9-79.userapi.com/s/v1/ig2/RGkpgwBNxkNdGtLWFujF04q_GDKiYYWF2tqNIWd-ZcPtaks0mkMKDSxoQ0F_Hco6ttae2reVi8CjJw7GqQ6l1dFU.jpg?size=2560x1707&quality=95&type=album"})', reply_markup=keyboard, parse_mode='markdown')
    await call.answer()

@dp.callback_query_handler(text="PR")
async def next(call: types.CallbackQuery): #Минская ВК
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text='<< Назад <<', callback_data="History"), types.InlineKeyboardButton(text='НА ГЛАВНУЮ', callback_data="Start"))
    await call.message.edit_text( f'{StendPR}[.]({"https://sun9-25.userapi.com/s/v1/ig2/PVUJjKPc_DIEYdp_MHLUmzVB3ToQibp3H9DyuY-JjBEE9ucyEyMbt2b4N6nfj5dNlGiViu9HZCwV0Yq_R85VtzoN.jpg?size=2560x1920&quality=95&type=album"})', reply_markup=keyboard, parse_mode='markdown')
    await call.answer()

@dp.callback_query_handler(text="OPK")
async def next(call: types.CallbackQuery): #Минская ВК
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text='<< Назад <<', callback_data="History"), types.InlineKeyboardButton(text='НА ГЛАВНУЮ', callback_data="Start"))
    await call.message.edit_text( f'{StendOPK}[.]({"https://sun9-72.userapi.com/s/v1/ig2/tdLF_6hV_T6DjS2iuUgFXcveFJiU6ddlB9f53evXcrZQhZ6c33cDLopWCj7xZyfkAUfi1mogHBqbG9OWDiViL04M.jpg?size=900x600&quality=95&type=album"})', reply_markup=keyboard, parse_mode='markdown')
    await call.answer()

@dp.callback_query_handler(text="VAI")
async def next(call: types.CallbackQuery): #Минская ВК
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text='<< Назад <<', callback_data="History"), types.InlineKeyboardButton(text='НА ГЛАВНУЮ', callback_data="Start"))
    await call.message.edit_text( f'{StendVAI}[.]({"https://sun9-34.userapi.com/s/v1/ig2/zXZLRCrRS_0OTQeiC2kSrS6qOyj21Gl5qpgs5mcrSpQEFcbHtMlCSzumvTQLKAIF2jrJ2u70yESaJNN-2E2JbR5J.jpg?size=2560x1402&quality=95&type=album"})', reply_markup=keyboard, parse_mode='markdown')
    await call.answer()

@dp.callback_query_handler(text="ODIR")
async def next(call: types.CallbackQuery): #Минская ВК
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text='<< Назад <<', callback_data="History"), types.InlineKeyboardButton(text='НА ГЛАВНУЮ', callback_data="Start"))
    await call.message.edit_text( f'{StendODIR}[.]({"https://sun9-11.userapi.com/s/v1/ig2/9rsEwQeZgfJ9fwa9OpilHOTYykIbRIbTrhn-y3crTqQ9-E7RM6Jr0IOhKnU9D5oxKk4aThXP-t7oroCIn0YHE00Z.jpg?size=2474x1604&quality=95&type=album"})', reply_markup=keyboard, parse_mode='markdown')
    await call.answer()

@dp.callback_query_handler(text="TSO")
async def next(call: types.CallbackQuery): #Минская ВК
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text='<< Назад <<', callback_data="History"), types.InlineKeyboardButton(text='НА ГЛАВНУЮ', callback_data="Start"))
    await call.message.edit_text( f'{StendTSO}[.]({"https://sun9-82.userapi.com/s/v1/ig2/hNGC4He04TicbbYpNUaix0qr9B11B0fMaNXXety8exG-aUewoVl7FAZGxD5VLuQDSonP1LrWowX06ngqXJsGM5a0.jpg?size=1024x663&quality=95&type=album"})', reply_markup=keyboard, parse_mode='markdown')
    await call.answer()


#--------------------(ИСТОРИЯ)-------------------------#

#--------------------(Информация)-------------------------#
@dp.callback_query_handler(text="InfoKB")
async def next(call: types.CallbackQuery): #Минская ВК
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text='<< Назад <<', callback_data="Podrazdeleniya"), types.InlineKeyboardButton(text='НА ГЛАВНУЮ', callback_data="Start"))
    await call.message.edit_text(InfoKB, reply_markup=keyboard, parse_mode='markdown')
    await call.answer()

@dp.callback_query_handler(text="InfoOPK")
async def next(call: types.CallbackQuery): #Минская ВК
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text='<< Назад <<', callback_data="Podrazdeleniya"), types.InlineKeyboardButton(text='НА ГЛАВНУЮ', callback_data="Start"))
    await call.message.edit_text(InfoOPK, reply_markup=keyboard, parse_mode='markdown')
    await call.answer()

@dp.callback_query_handler(text="InfoVAI")
async def next(call: types.CallbackQuery): #Минская ВК
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text='<< Назад <<', callback_data="Podrazdeleniya"), types.InlineKeyboardButton(text='НА ГЛАВНУЮ', callback_data="Start"))
    await call.message.edit_text(InfoVAI, reply_markup=keyboard, parse_mode='markdown')
    await call.answer()

@dp.callback_query_handler(text="InfoODIR")
async def next(call: types.CallbackQuery): #Минская ВК
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text='<< Назад <<', callback_data="Podrazdeleniya"), types.InlineKeyboardButton(text='НА ГЛАВНУЮ', callback_data="Start"))
    await call.message.edit_text(InfoODIR, reply_markup=keyboard, parse_mode='markdown')
    await call.answer()

@dp.callback_query_handler(text="InfoTSO")
async def next(call: types.CallbackQuery): #Минская ВК
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text='<< Назад <<', callback_data="Podrazdeleniya"), types.InlineKeyboardButton(text='НА ГЛАВНУЮ', callback_data="Start"))
    await call.message.edit_text(InfoTSO, reply_markup=keyboard, parse_mode='markdown')
    await call.answer()
#--------------------(Информация)-------------------------#

#==========================(КАЛЛБЭК КНОПОК)==============================#


#==========================(ФУНКЦИИ)==============================#
def getText(str):
    with open(str + ".txt", "r", encoding="utf-8") as file:
        txt = file.read()
        return txt
#==========================(ФУНКЦИИ)==============================#


#==========================(ЗАПУСК БОТА)==============================#
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
#==========================(ЗАПУСК БОТА)==============================#