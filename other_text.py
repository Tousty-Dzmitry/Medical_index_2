
from aiogram import Router
from aiogram.filters import Command
from config import ADMIN_CHAT_ID, CHAT_ID
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.state import default_state
from aiogram.filters.state import State, StatesGroup
from aiogram.types import Message
from config import BOT_TOKEN
from aiogram import Bot

bot: Bot = Bot(token=BOT_TOKEN)


router: Router = Router()



# как администратору написать сообщение
storage: MemoryStorage = MemoryStorage()

class Form(StatesGroup):
     admin_text = State()

@router.message(Command(commands='admin_text'))
async def process_admin(message: Message, state: FSMContext):
    await message.answer(text='Чем хотите поделиться?')
    await state.set_state(Form.admin_text)

@router.message(Form.admin_text)
async def process_admin(message: Message, state: FSMContext) -> None:
    await message.answer(message.text)



@router.message()
async def other_text(message:Message):
    await message.answer('1) выбери команду /choose_an_index\n\n'
                         '2) выбери индекс\n\n'
                         '3) следуй инструкции')



