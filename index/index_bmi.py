

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart, StateFilter, Text
from aiogram.filters.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import (CallbackQuery, InlineKeyboardButton,
                           InlineKeyboardMarkup, Message, PhotoSize)
from aiogram import Router
# Вместо BOT TOKEN HERE нужно вставить токен вашего бота,
# полученный у @BotFather
#BOT_TOKEN = '6119057214:AAFfWbstixdSv64T34PMfUIDVcHSmKzEWJs'
router:Router = Router()
# Инициализируем хранилище (создаем экземпляр класса MemoryStorage)
storage: MemoryStorage = MemoryStorage()

# Создаем объекты бота и диспетчера
# bot: Bot = Bot(BOT_TOKEN)
# dp: Dispatcher = Dispatcher(storage=storage)

class Form(StatesGroup):
    weight = State()
    height = State()


@router.message(Text(text='индекс массы тела'))
#@router.message(CommandStart(), StateFilter(default_state))
async def process_start_command(message: Message):
    await message.answer(text='Привет, этот бот рассчитает твой ИМТ\n\n'
                              'Чтобы перейти к заполнению анкеты - '
                              'отправьте команду /index_bmi')

@router.message(Command(commands='index_bmi'), StateFilter(default_state))
async def process_fillform_command(message: Message, state: FSMContext):
    await message.answer(text='Пожалуйста, введите ваше вес (кг)')
    await state.set_state(Form.weight)




@router.message(Form.weight)
async def process_name(message: Message, state: FSMContext) -> None:
    await message.answer(f'Теперь введите рост (см)')
    await state.update_data(weight=message.text)
    await state.set_state(Form.height)

@router.message(Form.height)
async def process_name(message: Message, state: FSMContext) -> None:
    context_data = await state.get_data()
    weight = context_data.get('weight')
    data_user = f"ИМТ  {float(weight) / (float(message.text)/100) ** 2}"
    await message.answer(data_user)
    bmi = (float(weight) / (float(message.text)/100) ** 2)
    if bmi < 16:
        await message.answer('Выраженный дефицит массы тела')
    elif 16 <= bmi < 18.5:
        await message.answer('Недостаточная (дефицит) масса тела')
    elif 18.5 <= bmi < 25:
        await message.answer('Норма')
    elif 25 <= bmi < 30:
        await message.answer('Избыточная масса тела (предожирение)')
    elif 30 <= bmi < 35:
        await message.answer('Ожирение 1 степени')
    elif 35 <= bmi < 40:
        await message.answer('Ожирение 2 степени')
    elif 40 <= bmi:
        await message.answer('Ожирение 3 степени')

    await state.clear()

# # Запускаем поллинг
# if __name__ == '__main__':
#     dp.run_polling(bot)
