import asyncio

from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand

from config import BOT_TOKEN
from lexicon import LEXICON_COMMANDS
from aiogram.filters import CommandStart, Text
from aiogram.types import (KeyboardButton, Message, ReplyKeyboardMarkup,
                           ReplyKeyboardRemove)
from aiogram.filters.state import State, StatesGroup
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.types import ReplyKeyboardRemove
from index import index_ani
from index import index_bmi
import other_text
from keyboard import keyboard
#import contact_with_admin
from aiogram import Router
from aiogram.fsm.storage.memory import MemoryStorage
from config import BOT_TOKEN
from config import ADMIN_CHAT_ID

router: Router = Router()

storage: MemoryStorage = MemoryStorage()
bot: Bot = Bot(token=BOT_TOKEN)
class Form(StatesGroup):
    question = State()

@router.message(Command(commands='contact_with_admin'))
async def process_question(message: Message, state: FSMContext):
    await message.answer(f'задайте вопрос админу')
    await state.set_state(Form.question)

@router.message(Form.question)
async def process_question(message: Message, state: FSMContext) -> None:
    #await state.update_data(question=message.text)
    # context_data = await state.get_data()
    # question = context_data.get('question')


    # await message.answer (f'Вопрос админу:\r\n{message.text}]',
    #                       chat_id=5489411423,
                         # )
    await bot.send_message( text='message.text', chat_id=5489411423)

    await state.clear()



#
#
# @router.message(Command(command='contact_with_admin'))
# async def send_to_admin(message: types.Message):
#     await bot.send_message(chat_id=ADMIN_CHAT_ID, text='Сообщение для админа')