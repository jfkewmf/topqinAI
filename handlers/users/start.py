from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.reply.reply import reply
from loader import dp, bot 
ADMIN_ID = 6038831784
import re
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

class UserState(StatesGroup):
    waiting_for_message = State()

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    text = [
        f"<b>😊 Salom, {message.from_user.full_name}!\n</b>",
        f"<b>🥇 Bizning loyihamizga xush kelibsiz!\n</b>",
        f"<b>📚 Bu yerda siz <a href='https://t.me/topqin'>Topqin AI</a> nima nima maqsada asos solinga va ilovamiz kelajagi haqida bilib olishingiz mumkin!\n</b>",
        f"<b>🍃 Sizga manfaatli bo'lishidan hursandiz doimo mamnunmiz!\n\n</b>",
        f"<b>✍️ Agar talab va takliflaringiz bo'lsa, bizga murojaat qiling!\n</b>",
        f"<b>👇 Batafsil ma'lumot uchun kerakli tugmalardan birini bosing!</b>"
    ]
    await message.answer(text="\n".join(text), reply_markup=reply, parse_mode=types.ParseMode.HTML)

@dp.message_handler(text="Loyiha haqida ℹ️")
async def loyiha_haqida(message: types.Message):
    text = """<b>✨ ToqinAI nima?  

ToqinAI — bu sizning ingliz tilini o'rganishingizga yordam beradigan aqlli ilova. 🇬🇧📚  

🔹 Ilova orqali turli xil qiziqarli o'yinlar o'ynab, so'z boyligingizni oshirishingiz mumkin.  
🔹 Ingliz tilini o'rganish yanada qulay va samarali bo'ladi.  
🔹 Hatto do'stlaringiz bilan birgalikda mashq qilib, til o'rganishni yanada maroqli qilishingiz mumkin! 🤝🎮  

🚀 ToqinAI bilan ingliz tilini o'rganish — oson, qiziqarli va samarali!</b>"""
    await message.answer(text=text, reply_markup=reply, parse_mode=types.ParseMode.HTML)

@dp.message_handler(text="Maqsadimiz ⚡️")
async def maqsadimiz(message: types.Message):
    text = """<b>✨ ToqinAI nima?  

ToqinAI — bu ingliz tilini o'rganishda yordam beradigan aqlli ilova. 🇬🇧📚  

Bugun hali ishlab chiqilayotgan bo'lsa-da, kelajakda ToqinAI yanada ko'plab foydali funksiyalar bilan boyitiladi. 🔮  

🔹 Qiziqarli o'yinlar orqali ingliz tilini o'rganish.  
🔹 Do'stlar bilan birga mashq qilish va musobaqalashish.  
🔹 So'z boyligini kengaytirish va tez eslab qolish usullari.  
🔹 Yangi texnologiyalar asosida yanada samarali ta'lim olish imkoniyati.  

🚀 ToqinAI kelajakda o'quvchilar, talabalar va til o'rganishni istagan har bir inson uchun ishonchli yordamchi bo'ladi.</b>"""
    await message.answer(text=text, reply_markup=reply, parse_mode=types.ParseMode.HTML)

@dp.message_handler(text="Imkoniyatlar 🚀")
async def imkoniyatlar(message: types.Message):
    text = """<b>🚀 Topqin AI – Sizning aqlli yordamchingiz! 🤖✨  

📌 Topqin AI – bu sizga ingliz tilini 🇬🇧 o'rganishni 📚 yanada qiziqarli 🎉 va samarali 💡 qiladigan platforma.  

🔹 Topqin AIda mavjud imkoniyatlar:  
🎮 Mini-o'yinlar orqali o'rganish (Word Battle ⚔️, 4 Pics 1 Word 🖼️➕🔤, Flashcards 🃏 va boshqalar)  
🧠 AI yordamida so'z va gaplarni tushunish  
📅 Har kuni yangi topshiriqlar va testlar  
🗣️ Ingliz tilidagi nutqni rivojlantirish imkoniyati  
🏆 Do'stlar bilan bellashish va natijalarni solishtirish  

🔥 Topqin AI – bu nafaqat til o'rganish 📖, balki uni amalda qo'llash ✨ ham o'rgatadigan aqlli ilova! 🚀</b>"""
    await message.answer(text=text, reply_markup=reply, parse_mode=types.ParseMode.HTML)

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

@dp.message_handler(text="Kanallarimiz 📢")
async def kanallarimiz(message: types.Message):
    text = """📢 Bizning rasmiy kanallarimiz:

1️⃣ Topqin AI - Asosiy kanalimiz!
2️⃣ Abdurokhman Life - Shaxsiy blog!"""
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(
        InlineKeyboardButton("🔗 Topqin AI", url="https://t.me/topqin"),
        InlineKeyboardButton("🔗 Shahsiy kanal", url="https://t.me/abdurokhman_life")
    )
    await message.answer(text, reply_markup=keyboard)

@dp.message_handler(text="Aloqa 📞")
async def aloqa_start(message: types.Message):
    await message.answer("<b>✍️ Iltimos, murojaatingizni yozing.\nTez orada javob beramiz: @mortistubea</b>", reply_markup=reply)