import asyncio
import os
import ssl
import dotenv 
import random
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiohttp import TCPConnector

dotenv.load_dotenv()
TOKEN = os.getenv("TOKEN")

# Инициализация бота с кастомным connector
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Настройка SSL контекста (если нужно обойти проверку)
ssl_context = ssl.create_default_context()
ssl_context.set_ciphers('DEFAULT@SECLEVEL=1')

music_db = {
    "поп": [
        {"title": "Поп-песня 1", "file": "pop1.mp3"},
        {"title": "Поп-песня 2", "file": "pop2.mp3"}
    ],
    "реп": [
        {"title": "Конченный", "file": "2r2r0.mp3"},
        {"title": "Кальян Каннибала", "file": "2r2r1.mp3"},
    ],
    "рок": [
        {"title": "Рок-хит 1", "file": "rock1.mp3"},
        {"title": "Рок-хит 2", "file": "rock2.mp3"}
    ],
    "фонк": [
        {"title": "Матушка Земля", "file": "phonk0.mp3"},
        {"title": "Фонк-бит 2", "file": "funk2.mp3"}
    ]
}

# Клавиатура главного меню
main_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🎵 Жанры", callback_data="genres")],
    [InlineKeyboardButton(text="🎲 Рандом", callback_data="random")]
])

@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer("Выберите действие:", reply_markup=main_kb)

@dp.callback_query(F.data == "genres")
async def show_genres(callback: types.CallbackQuery):
    await callback.message.delete()
    builder = InlineKeyboardBuilder()
    for genre in music_db.keys():
        builder.add(InlineKeyboardButton(text=genre, callback_data=f"genre_{genre}"))
    builder.adjust(2)
    await callback.message.answer("Выберите жанр:", reply_markup=builder.as_markup())

@dp.callback_query(F.data.startswith("genre_"))
async def show_songs(callback: types.CallbackQuery):
    genre = callback.data.split("_")[1]
    songs = music_db.get(genre, [])
    await callback.message.delete()
    
    builder = InlineKeyboardBuilder()
    for song in songs:
        builder.add(InlineKeyboardButton(
            text=song["title"],
            callback_data=f"song_{genre}_{song['file']}"
        ))
    builder.adjust(1)
    builder.row(InlineKeyboardButton(text="⬅️ Назад", callback_data="genres"))
    
    await callback.message.answer(
        f"Песни в жанре {genre}:",
        reply_markup=builder.as_markup()
    )

@dp.callback_query(F.data.startswith("song_"))
async def send_song(callback: types.CallbackQuery):
    _, genre, filename = callback.data.split("_")
    song_path = os.path.join("music", genre, filename)
    
    try:
        # Находим песню в базе данных по имени файла
        song = next((s for s in music_db[genre] if s["file"] == filename), None)
        
        if not song:
            await callback.answer("Песня не найдена в базе данных", show_alert=True)
            return
            
        with open(song_path, "rb") as audio_file:
            await bot.send_audio(
                chat_id=callback.message.chat.id,
                audio=types.BufferedInputFile(audio_file.read(), filename=filename),
                caption=f"🎵 {song['title']}\n#️⃣ Жанр: {genre}"
            )
    except FileNotFoundError:
        await callback.answer("Файл не найден", show_alert=True)
    except Exception as e:
        print(f"Ошибка: {e}")
        await callback.answer("Произошла ошибка", show_alert=True)

@dp.callback_query(F.data == "random")
async def send_random(callback: types.CallbackQuery):
    genre = random.choice(list(music_db.keys()))
    song = random.choice(music_db[genre])
    song_path = os.path.join("music", genre, song["file"])
    
    try:
        with open(song_path, "rb") as audio_file:
            await bot.send_audio(
                chat_id=callback.message.chat.id,
                audio=types.BufferedInputFile(audio_file.read(), filename=song["file"]),
                caption=f"🎲 Случайный трек: {song['title']}\n#️⃣ Жанр: {genre}"
            )
    except FileNotFoundError:
        await callback.answer("Файл не найден", show_alert=True)
    except Exception as e:
        print(f"Ошибка: {e}")
        await callback.answer("Произошла ошибка", show_alert=True)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())