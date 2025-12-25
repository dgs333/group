import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.types import FSInputFile
from utils.gemini import *
from utils.funcs import *
from utils import data
import os
from dotenv import load_dotenv

load_dotenv()
TG_TOKEN=os.environ.get("TG_TOKEN")
logging.basicConfig(level=logging.INFO)
bot = Bot(TG_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello!")

#Длинный ответ
@dp.message(Command("gen2"))
async def gen2_(message: types.Message):
    prompt = message.text.split(' ', maxsplit=1)[1]
    ans = gen_ai(prompt, genai.types.GenerateContentConfig(temperature=0.7, system_instruction=data.def_config))
    fname = '(не сохранен)'
    if len(ans) < 4096: 
        await message.answer(ans)
    else:
        fname = text_in_file(ans)
        await message.answer_document(FSInputFile(fname), caption='Текст слишком длинный, он был отправлен файлом')
    save_ai_log(prompt, message.from_user.username, fname)

#Короткий ответ 
@dp.message(Command("gen"))
async def gen_(message: types.Message):
    prompt = message.text.split(' ', maxsplit=1)[1]
    config = genai.types.GenerateContentConfig(temperature=0.7, system_instruction=data.def_config_short+data.def_config)
    ans = gen_ai(prompt, config)
    fname = '(не сохранен)'
    if len(ans) < 4096: 
        await message.answer(ans)
    else:
        fname = text_in_file(ans)
        await message.answer_document(FSInputFile(fname), caption='Текст слишком длинный, он был отправлен файлом')
    save_ai_log(prompt, message.from_user.username, fname)

# @dp.message(Command("edit_cfg"))
# async def edit_cfg_(message: types.Message):
#     config = message.text.split(' ', )

"""@dp.message(Command("test"))
async def test_(message: types.Message):
    text = message.text.split(' ', maxsplit=1)[1]
    ans = ''
    for i in range(int(text)):
        ans += '1'
    print(ans)
    await message.answer(ans)"""


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
    