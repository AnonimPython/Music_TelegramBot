# 🎵 Music Bot - Telegram музыкальный бот 🎧

## 🌟 О проекте / About The Project

**Music Bot** - это интеллектуальный Telegram-бот для любителей музыки, предлагающий удобный способ поиска и прослушивания треков по жанрам.

**Music Bot** is an intelligent Telegram bot for music lovers, offering a convenient way to search and listen to tracks by genre.

### 🔥 Особенности / Key Features

* 🎵 **По жанрам** /  **By Genre** : Поп, Рэп, Рок, Фонк
* 🎲 **Случайный трек** /  **Random Track** : Кнопка для случайного выбора
* 🔍 **Удобная навигация** /  **Easy Navigation** : Интуитивное меню с кнопками
* 🚀 **Быстрая загрузка** /  **Fast Loading** : Мгновенная отправка аудиофайлов
* 📱 **Адаптивный интерфейс** /  **Responsive Interface** : Работает на любых устройствах

## 🛠 Технологии / Technologies

* **Python 3.10+** с асинхронной работой
* **Aiogram 3.x** - современный фреймворк для Telegram ботов

## 🚀 Установка / Installation

### 📦 Требования / Prerequisites

* Python 3.10 или новее
* Telegram bot token от [@BotFather](https://t.me/BotFather)

### ⚙️ Настройка / Setup

1. Клонируйте репозиторий:

Copy

```
git clone https://github.com/AnonimPython/Music_TelegramBot.git
cd music
```

4. Создайте структуру папок:

Copy

```
/music
  /поп
  /реп
  /рок
  /фонк
```

5. Добавьте MP3 файлы в соответствующие папки
6. Запустите бота:

Copy

```
python main.py
```

## 🎨 Использование / Usage

### Основные команды / Main Commands:

* `/start` - Запустить бота
* `🎵 Жанры` - Выбрать музыкальный жанр
* `🎲 Рандом` - Случайный трек

### Пример работы / Example Flow:

1. Пользователь нажимает "🎵 Жанры"
2. Выбирает жанр (например, "Фонк")
3. Видит список доступных треков
4. Выбирает трек и получает аудиофайл с описанием

## 📂 Структура проекта / Project Structure

Copy

```
music-bot/
├── music/           # Папка с аудиофайлами
│   ├── поп/         # Поп-музыка
│   ├── реп/         # Рэп-треки
│   ├── рок/         # Рок-композиции
│   └── фонк/        # Фонк-биты
├── .env             # Конфигурация
├── main.py          # Основной код бота
└── README.md        # Документация
```
