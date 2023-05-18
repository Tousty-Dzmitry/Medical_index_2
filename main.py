import asyncio

from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand

from config import BOT_TOKEN, ADMIN_CHAT_ID, CHAT_ID
from lexicon import LEXICON_COMMANDS
from aiogram.filters import CommandStart, Text
from aiogram.types import (KeyboardButton, Message, ReplyKeyboardMarkup,
                           ReplyKeyboardRemove)
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.types import ReplyKeyboardRemove
from index import index_ani
from index import index_bmi
import other_text
from keyboard import keyboard
#import contact_with_admin
#>>>>>>>>>>>>>
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters.state import State, StatesGroup
#>>>>>>>>>>>


storage: MemoryStorage = MemoryStorage()


# Создаем объекты бота и диспетчера
bot: Bot = Bot(token=BOT_TOKEN)
dp: Dispatcher = Dispatcher()

# создание кнопки меню
# Создаем асинхронную функцию
async def set_main_menu(bot: Bot):
    main_menu_commands = [BotCommand(
        command=command,
        description=description
    ) for command,
          description in LEXICON_COMMANDS.items()]
    await bot.set_my_commands(main_menu_commands)

@dp.message(Command(commands='choose_an_index'))
async def process_start_command(message: Message):
    await message.answer(text='выбирайте индекс',
                         reply_markup=keyboard)
#>>>>>>>>>>>>>>>>> ВОПРОС АДМИНУ
class Form(StatesGroup):
    question = State()

@dp.message(Command(commands='contact_with_admin'))
async def process_question(message: Message, state: FSMContext):
    await message.answer(f'задайте вопрос админу')
    await state.set_state(Form.question)

@dp.message(Form.question)
async def process_question(message: Message, state: FSMContext) -> None:
    #await state.update_data(question=message.text)
    # context_data = await state.get_data()
    # question = context_data.get('question')


    # await message.answer (f'Вопрос админу:\r\n{message.text}]',
    #                       chat_id=5489411423,
                         # )
    await bot.send_message(chat_id=ADMIN_CHAT_ID, text='Вопрос админу: ' + message.text)

    await state.clear()
#>>>>>>>>>>>>>>>>
#ADMIN_CHAT_ID = 5489411423
@dp.message(Command(commands='contact'))
async def send_to_admin(message: Message):
    await bot.send_message(chat_id=ADMIN_CHAT_ID, text='Сообщение для админа')
#<<<<<<<<<<>>>>>>>>>>

#<<<<<<<<<<>>>>>>>>>>





#dp.include_router(contact_with_admin.router)
dp.include_router(index_ani.router)
dp.include_router(index_bmi.router)
dp.include_router(other_text.router)





if __name__ == '__main__':
    # Регистрируем асинхронную функцию в диспетчере,
    # которая будет выполняться на старте бота,
    dp.startup.register(set_main_menu)
    # Запускаем поллинг
    dp.run_polling(bot)