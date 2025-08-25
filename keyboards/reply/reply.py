from aiogram.types import ReplyKeyboardMarkup, KeyboardButton



reply = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Loyiha haqida ℹ️"),
        ],
        [
            KeyboardButton(text="Maqsadimiz ⚡️"),
            KeyboardButton(text="Imkoniyatlar 🚀")
        ],
        [           
            KeyboardButton(text="Kanallarimiz 📢"),
            KeyboardButton(text="Aloqa 📞"),
        ],
    ],
    resize_keyboard=True
)