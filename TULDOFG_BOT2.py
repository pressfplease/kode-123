import logging
import aiogram
import random

from aiogram import Bot, Dispatcher, executor, types
a=random.randint(0.0 , 100.0)
b=random.randint(0.0 , 100.0)
c=random.randint(0.0 , 100.0)
d=random.randint(0.0 , 100.0)
e=random.randint(0.0 , 100.0)
f=("столкновение  с обьектом")
g=("закончилось топливо")
h=("закончилась вода")
i=("закончилось удобрение")
j=("заполнен зерновой бункер")
k=random.randint(0 , 24)
l=random.randint(0 , 24)
m=random.randint(0 , 24)
n=random.randint(0 , 24)
o=random.randint(0 , 24)

p=random.randint(0 , 59)
q=random.randint(0 , 59)
r=random.randint(0 , 59)
s=random.randint(0 , 59)
t=random.randint(0 , 59)
u=("https://www.donationalerts.com/r/ddr6")

API_TOKEN = '5468034618:AAGz_79qGnci3moaIsQ53m9oq3Tucrw0R88'


logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

'''@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)'''

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    kb_markup = types.ReplyKeyboardMarkup(row_width=3)

    buttons_text = ('полив', 'удобрение' , "поддержать меня")
    kb_markup.row(*(types.KeyboardButton(text) for text in buttons_text))

    more_buttons_text = ("комбайн", "трактор", "грузовик")
    kb_markup.row(*(types.KeyboardButton(text) for text in more_buttons_text))

    await message.reply("Hello, I'm the INNOCAMP bot!", reply_markup=kb_markup)
@dp.message_handler(content_types=['text'])
async def get_text_messages(msg: types.Message):
   if msg.text.lower() == 'полив':
       
       await msg.answer('состояние ')
       await msg.answer(a)
       await msg.answer("из 100")
       await msg.answer(":событие:")
       await msg.answer(h)
       await msg.answer(k)
       await msg.answer(":")
       await msg.answer(p)

       
   elif msg.text.lower() == 'удобрение':
      
       await msg.answer('состояние ')
       await msg.answer(b)
       await msg.answer("из 100")
       await msg.answer(":событие:")
       await msg.answer(i)
       await msg.answer(l)
       await msg.answer(":")
       await msg.answer(q)
       

       
   elif msg.text.lower() == 'комбайн':
       
       await msg.answer('состояние ')
       await msg.answer(c)
       await msg.answer("из 100")
       await msg.answer(":событие:")
       await msg.answer(j)
       await msg.answer(m)
       await msg.answer(":")
       await msg.answer(r)

       
   elif msg.text.lower() == 'трактор':
      
       await msg.answer('состояние ')
       await msg.answer(d)
       await msg.answer("из 100")
       await msg.answer(":событие:")
       await msg.answer(f)
       await msg.answer(n)
       await msg.answer(":")
       await msg.answer(s)

       
   elif msg.text.lower() == 'грузовик':
       
       await msg.answer('состояние ')
       await msg.answer(e)
       await msg.answer("из 100")
       await msg.answer(":событие:")
       await msg.answer(g)
       await msg.answer(o)
       await msg.answer(":")
       await msg.answer(t)
   elif msg.text.lower() == "поддержать меня":
       await msg.answer(u)
      

       
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
