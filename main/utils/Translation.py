# This file is a part of TG-Direct-Link-Generator
from main.vars import Var
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


class Language(object):
    class en(object):
        START_TEXT = """
**👋 Hola. Bienvenido al bot {}**\n
<i>Soy un bot generador de enlaces directos con solo reenviarme un archivo </i>\n
<i>Toca Help para más Info</i>\n
<b><i><u>Warning 🚸</u></i></b>\n
<b>🔞 Pron Contents Leads To Permanenet Ban You.</b>"""

        HELP_TEXT = """🔰 **Cómo usarme ?**

<i>- Envíame un archivo de telegram </i>
<i>- Luego te proporcionare un link directo del archivo  !</i>

        ABOUT_TEXT = """
<b>⚜ My Name : File Yo Links Pro Generator</b>\n
<b>⚜ Username : @FileToLinksPro_bot</b>\n
<b>🔸Version : 2.0</b>\n
<b>🔹Last Updated : [ 27-Jun-22 ]</b>
"""

        stream_msg_text ="""
<u>**Links Creado Con Éxito  !**</u>\n
<b>📂 Nombre del Archivo :</b> {}\n
<b>📦 Tamaño del Archivo :</b> {}\n
<b>📥 Descargar :</b> {}\n
<b>🖥 Watch :</b> {}"""

        ban_text="__Sᴏʀʀʏ Sɪʀ, Yᴏᴜ ᴀʀᴇ Bᴀɴɴᴇᴅ ᴛᴏ ᴜsᴇ ᴍᴇ.__\n\n**[Cᴏɴᴛᴀᴄᴛ Dᴇᴠᴇʟᴏᴘᴇʀ](https://t.me/TechZBots_Support) Tʜᴇʏ Wɪʟʟ Hᴇʟᴘ Yᴏᴜ**"

# ------------------------------------------------------------------------------

class BUTTON(object):
    START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Help', callback_data='help'),
        InlineKeyboardButton('About', callback_data='about')
        ],        
        [InlineKeyboardButton("Updates Channel", url='https://t.me/TechZBots'),
        InlineKeyboardButton("Repo", url='https://github.com/TechShreyash/TG-Direct-Link-Generator')]
        ]
    )
    HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Home', callback_data='home'),
        InlineKeyboardButton('About', callback_data='about')
        ],
        [
        InlineKeyboardButton('Close', callback_data='close'),
        ],        
        ]
    )
    ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Home', callback_data='home'),
        InlineKeyboardButton('Help', callback_data='help')
        ],
        [
        InlineKeyboardButton('Close', callback_data='close'),
        ]        
        ]
    )
