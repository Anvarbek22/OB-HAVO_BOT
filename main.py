import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher, types,F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.context import FSMContext
from aiogram.filters import CommandStart
from button import*



TOKEN = '6581228259:AAFrhFVBh1-eJSC2-YpRKhAAB9jTHWDpJCs'

dp = Dispatcher()

@dp.message(CommandStart())
async def start_command(message: types.Message,state:FSMContext):
    await message.answer(text="VILOYATNI TANLANG🔔",reply_markup=viloyat())
    await state.set_state(logs.start1)
    
@dp.message(logs.start1)
async def start_command(message: types.Message,state:FSMContext):
    a=message.text
    if a=="Youtube":
        await message.answer(text="YOUTUBE KANAL",reply_markup=yyy)
    else:
        await state.update_data({'VILOYAT':a})
        await message.answer(text="TANLANG",reply_markup=tur)
        await state.set_state(logs.start2)
    
@dp.message(logs.start2)
async def start_command(message: types.Message,state:FSMContext):
    text=message.text
    if text=="ORTGA":
        await message.answer(text="VILOYATNI TANLANG🔔",reply_markup=viloyat())
        await state.set_state(logs.start1)
    else:
        data=await state.get_data()
        vil=data.get('VILOYAT')
        dat=obhavo(text,vil)
        await message.answer(text=dat)
            

async def main() -> None:
   
    bot = Bot(token=TOKEN)
   
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        logging.basicConfig(level=logging.INFO, stream=sys.stdout)
        asyncio.run(main())
    except:
        print("bot o'chdi")