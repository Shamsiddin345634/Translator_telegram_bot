from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

#tilni tanlash
til = InlineKeyboardMarkup(
    inline_keyboard = [
        [
        InlineKeyboardButton(text="🇺🇿 Uzbek", callback_data="uz"),
        InlineKeyboardButton(text="🇷🇺 Russia ", callback_data="ru")
        ],
        [
        InlineKeyboardButton(text="🏴󠁧󠁢󠁥󠁮󠁧󠁿 English", callback_data="en"),
        InlineKeyboardButton(text="🇨🇳 Chinese", callback_data="zh-cn")
        ],
        [
        InlineKeyboardButton(text="🇫🇷 French", callback_data="fr"),
        InlineKeyboardButton(text="🇦🇪 Arabic", callback_data="ar")
        ],
        [
        InlineKeyboardButton(text="🇪🇸 Spanish", callback_data="es"),
        InlineKeyboardButton(text="🇩🇪 German", callback_data="de")
        ],
        
        [
        InlineKeyboardButton(text="🇹🇷 Turkish", callback_data="tr"),
        InlineKeyboardButton(text="🇯🇵 Japanese", callback_data="ja")
        ],
        [
        InlineKeyboardButton(text="🇰🇷 Korean", callback_data="kr"),
        InlineKeyboardButton(text="🇰🇿 Kazakh", callback_data="kz")
        ],
    ],
)