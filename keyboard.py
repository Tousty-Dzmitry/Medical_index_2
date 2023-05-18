from aiogram.types import (KeyboardButton, Message, ReplyKeyboardMarkup,
                           ReplyKeyboardRemove)




#клавиатуру нужно сделать отдельным модулем

button_1: KeyboardButton = KeyboardButton(text='индекс АНИ')
button_2: KeyboardButton = KeyboardButton(text='индекс массы тела')
# button_3: KeyboardButton = KeyboardButton(text='привет')
# button_4: KeyboardButton = KeyboardButton(text='Кнопка 4')
# button_5: KeyboardButton = KeyboardButton(text='Кнопка 5')
# button_6: KeyboardButton = KeyboardButton(text='Кнопка 6')
# button_7: KeyboardButton = KeyboardButton(text='Кнопка 7')
# button_8: KeyboardButton = KeyboardButton(text='Кнопка 8')
# button_9: KeyboardButton = KeyboardButton(text='Кнопка 9')

# Создаем объект клавиатуры, добавляя в него кнопки
keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
                        keyboard=[[button_1], [button_2]])#, [button_3],
                                  # [button_4, button_5, button_6],
                                  # [button_7, button_8, button_9]])


