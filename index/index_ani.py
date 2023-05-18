#from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart, StateFilter, Text
from aiogram.filters.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import (CallbackQuery, InlineKeyboardButton,
                           InlineKeyboardMarkup, Message, PhotoSize)
from aiogram import Router
from aiogram.types import (KeyboardButton, Message, ReplyKeyboardMarkup,
                           ReplyKeyboardRemove)

router: Router = Router()

#BOT_TOKEN = '6119057214:AAFfWbstixdSv64T34PMfUIDVcHSmKzEWJs'

# Инициализируем хранилище (создаем экземпляр класса MemoryStorage)
storage: MemoryStorage = MemoryStorage()

# Создаем объекты бота и диспетчера
# bot: Bot = Bot(BOT_TOKEN)
# dp: Dispatcher = Dispatcher(storage=storage)

class Form(StatesGroup):
    sex = State()
    Weight = State()
    Height = State()
    MCV = State()
    ACT = State()
    ALT = State()
    #BMI = State()

# что бы реагировал на нажатие кнопки
@router.message(Text(text='индекс АНИ'))
#@router.message(CommandStart(), StateFilter(default_state))
async def process_start_command(message: Message):
    await message.answer(text='Привет, этот бот рассчитает индекс ANI\n\n'
                              'Чтобы перейти к заполнению анкеты - '
                              'отправьте команду /index_ani')

@router.message(Command(commands='index_ani'), StateFilter(default_state))
async def process_fillform_command(message: Message, state: FSMContext):
    await message.answer(text='Введите пол пациента (m/w)')
    await state.set_state(Form.sex)

@router.message(Form.sex)
async def process_name(message: Message, state: FSMContext) -> None:
    #await message.answer(f'Пол пациента:\r\n{message.text}\r\nВведите MCV')
    await message.answer(f'Введите вес (кг)')
    await state.update_data(sex=message.text)
    await state.set_state(Form.Weight)

@router.message(Form.Weight)
async def process_name(message: Message, state: FSMContext) -> None:
    await message.answer(f'Введите рост (см)')
    await state.update_data(Weight=message.text)

    await state.set_state(Form.Height)

@router.message(Form.Height)
async def process_name(message: Message, state: FSMContext) -> None:
    await message.answer(f'Введите MCV')
    await state.update_data(Height=message.text)
    await state.set_state(Form.MCV)


@router.message(Form.MCV)
async def process_name(message: Message, state: FSMContext) -> None:
    await message.answer(f'Введите ACT')
    await state.update_data(MCV=message.text)
    await state.set_state(Form.ACT)



@router.message(Form.ACT)
async def process_name(message: Message, state: FSMContext) -> None:
    await message.answer(f'Введите ALT')
    await state.update_data(ACT=message.text)
    await state.set_state(Form.ALT)

@router.message(Form.ALT)
async def process_name(message: Message, state: FSMContext) -> None:
    await state.update_data(ALT=message.text)


    context_data = await state.get_data()
    sex = context_data.get('sex')
    Weight = context_data.get('Weight')
    Height = context_data.get('Height')
    MCV = context_data.get('MCV')
    ACT = context_data.get('ACT')
    #ALT = context_data.get('ALT')

    #data_user=f"{sex}, {MCV}, {ACT}, {ALT}, {message.text}"
    #await message.answer(f"{sex}, {MCV}, {ACT}, {ALT}, {message.text}")
    if sex == 'w':
        await message.answer(f'Индекс ANI:\r\n{float(-58.5 + 0.637 * float(MCV) + 3.91 * (float(ACT)/float(message.text)) - 0.406 * (float(Weight) / (float(Height) / 100) ** 2))}')
    elif sex == 'm':
        await message.answer(f"Индекс ANI:\r\n{float(-58.5 + 0.637 * float(MCV) + 3.91 * (float(ACT) / float(message.text)) - 0.406 * (float(Weight) / (float(Height) / 100) ** 2)) + 6.35}")
    else:
        await message.answer('Проверте ввод данных')
# сделать расчет по формуле в зависимости от пола пациента
   # await message.answer(float(MCV)*float(ACT))


    await state.clear()


# Запускаем поллинг
# if __name__ == '__main__':
#     dp.run_polling(bot)






# from aiogram import Bot, Dispatcher, F
# from aiogram.filters import Command, CommandStart, StateFilter, Text
# from aiogram.filters.state import State, StatesGroup
# from aiogram.fsm.context import FSMContext
# from aiogram.fsm.state import default_state
# from aiogram.fsm.storage.memory import MemoryStorage
# from aiogram.types import (CallbackQuery, InlineKeyboardButton,
#                            InlineKeyboardMarkup, Message, PhotoSize)
# from aiogram import Router
# from aiogram.types import (KeyboardButton, Message, ReplyKeyboardMarkup,
#                            ReplyKeyboardRemove)
#
# router: Router = Router()
#
# #BOT_TOKEN = '6119057214:AAFfWbstixdSv64T34PMfUIDVcHSmKzEWJs'
#
# # Инициализируем хранилище (создаем экземпляр класса MemoryStorage)
# storage: MemoryStorage = MemoryStorage()
#
# # Создаем объекты бота и диспетчера
# # bot: Bot = Bot(BOT_TOKEN)
# # dp: Dispatcher = Dispatcher(storage=storage)
#
# class Form(StatesGroup):
#     sex = State()
#     MCV = State()
#     ACT = State()
#     ALT = State()
#     BMI = State()
#
# # что бы реагировал на нажатие кнопки
# @router.message(Text(text='индекс АНИ'))
# #@router.message(CommandStart(), StateFilter(default_state))
# async def process_start_command(message: Message):
#     await message.answer(text='Привет, этот бот рассчитает индекс ANI\n\n'
#                               'Чтобы перейти к заполнению анкеты - '
#                               'отправьте команду /index_ani')
#
# @router.message(Command(commands='index_ani'), StateFilter(default_state))
# async def process_fillform_command(message: Message, state: FSMContext):
#     await message.answer(text='Введите пол пациента (m/w)')
#     await state.set_state(Form.sex)
#
# @router.message(Form.sex)
# async def process_name(message: Message, state: FSMContext) -> None:
#     #await message.answer(f'Пол пациента:\r\n{message.text}\r\nВведите MCV')
#     await message.answer(f'Введите MCV')
#     await state.update_data(sex=message.text)
#     await state.set_state(Form.MCV)
#
# @router.message(Form.MCV)
# async def process_name(message: Message, state: FSMContext) -> None:
#     await message.answer(f'Введите ACT')
#     await state.update_data(MCV=message.text)
#
#     await state.set_state(Form.ACT)
#
# @router.message(Form.ACT)
# async def process_name(message: Message, state: FSMContext) -> None:
#     await message.answer(f'Введите ALT')
#     await state.update_data(ACT=message.text)
#     await state.set_state(Form.ALT)
#
#
# @router.message(Form.ALT)
# async def process_name(message: Message, state: FSMContext) -> None:
#     await message.answer(f'Введите BMI')
#     await state.update_data(ALT=message.text)
#     await state.set_state(Form.BMI)
#
#
#
# @router.message(Form.BMI)
# async def process_name(message: Message, state: FSMContext) -> None:
#     await state.update_data(BMI=message.text)
#
#     context_data = await state.get_data()
#     sex = context_data.get('sex')
#     MCV = context_data.get('MCV')
#     ACT = context_data.get('ACT')
#     ALT = context_data.get('ALT')
#
#     #data_user=f"{sex}, {MCV}, {ACT}, {ALT}, {message.text}"
#     #await message.answer(f"{sex}, {MCV}, {ACT}, {ALT}, {message.text}")
#     if sex == 'w':
#         await message.answer(f'Индекс ANI:\r\n{float(-58.5 + 0.637 * float(MCV) + 3.91 * (float(ACT)/float(ALT)) - 0.406 * float(message.text))}')
#     elif sex == 'm':
#         await message.answer(f"Индекс ANI:\r\n{float(-58.5 + 0.637 * float(MCV) + 3.91 * (float(ACT) / float(ALT)) - 0.406 * float(message.text)) + 6.35}")
#     else:
#         await message.answer('Проверте ввод данных')
# # сделать расчет по формуле в зависимости от пола пациента
#    # await message.answer(float(MCV)*float(ACT))
#
#
#     await state.clear()
#
#
# # Запускаем поллинг
# # if __name__ == '__main__':
# #     dp.run_polling(bot)