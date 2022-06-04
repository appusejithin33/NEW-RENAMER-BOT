from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ForceReply, CallbackQuery
import humanize
from Translation import mr
from helper.database import  insert 
from helper.utils import not_subscribed 

@Client.on_message(filters.private & filters.create(not_subscribed))
async def is_not_subscribed(client, message):
    await message.reply_text(
       text="**Sᴏʀʀʏ Bʀᴏ Yᴏᴜ Hᴀᴠᴇ Nᴏᴛ Jᴏɪɴᴇᴅ Oᴜʀ Cʜᴀɴɴᴇʟ Cʟɪᴄᴋ Oɴ Tʜᴇ Bᴜᴛᴛᴏɴ Bᴇʟᴏᴡ Aɴᴅ Jᴏɪɴ Tʜᴇɴ Sᴛᴀʀᴛ Aɢᴀɪɴ 🙏**",
       reply_markup=InlineKeyboardMarkup([
           [ InlineKeyboardButton(text="✪ Jᴏɪɴ Mʏ Uᴘᴅᴀᴛᴇ Cʜᴀɴɴᴇʟ ✪", url=client.invitelink)]
           ])
       )
    
@Client.on_message(filters.private & filters.command(["start"]))
async def start(client, message):
    insert(int(message.chat.id))
    await message.reply_photo(
       photo="https://telegra.ph/file/e954574ef60c1790caa79.jpg",
       caption=f"""👋 <b> Iᴛ's PᴏᴡᴇʀFᴜʟ {message.from_user.mention} 🧛‍♂️ Fɪʟᴇs Rᴇɴᴀᴍᴇʀ Bᴏᴛ ➕ Fɪʟᴇ 2 Vɪᴅᴇᴏ Cᴏɴᴇʀᴛᴇʀ BOT Wɪᴛʜ Pᴇʀᴍᴀɴᴇɴᴛ Tʜᴜᴍʙɴᴀɪʟ 💞....!!
 Sʜᴀʀᴇ Aɴᴅ Sᴜᴘᴘᴏʀᴛ Us......!!! 🦋 </b> 🤩""",
       reply_markup=InlineKeyboardMarkup( [[
          InlineKeyboardButton("♡︎ Cᴏɴᴛᴀᴄᴛ 🧛‍♂️ Aᴅᴍɪɴ ♡︎", url='https://t.me/KR_Admin_Bot')
          ],[
          InlineKeyboardButton('📢 Uᴘᴅᴀᴛᴇs', url='https://t.me/KR_botz'),
          InlineKeyboardButton('ℹ️ Sᴜᴘᴘᴏʀᴛ', url='https://t.me/+9o1NJzs67xc5ODA1')
          ],[
          InlineKeyboardButton('🛡️ Aʙᴏᴜᴛ', callback_data='about'),
          InlineKeyboardButton('ℹ️ Hᴇʟᴘ', callback_data='help')
          ]]
          )
       )
    return

@Client.on_message(filters.private &( filters.document | filters.audio | filters.video ))
async def send_doc(client, message):
    file = getattr(message, message.media.value)
    filename = file.file_name
    filesize = humanize.naturalsize(file.file_size)
    fileid = file.file_id
    await message.reply_text(
        f"__What do you want me to do with this file?__\n**File Name** :- `{filename}`\n**File Size** :- `{filesize}`",
        reply_to_message_id = message.id,
        reply_markup = InlineKeyboardMarkup([[ InlineKeyboardButton("📝 Rᴇɴᴀᴍᴇ ",callback_data = "rename"),
        InlineKeyboardButton("❌ Cᴀɴᴄᴇʟ ❌",callback_data = "cancel")  ]]))


@Client.on_callback_query()
async def cb_handler(client, query):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text=mr.ABOUT_TXT.format(client.username),
            disable_web_page_preview = True,
            reply_markup=InlineKeyboardMarkup( [[
               InlineKeyboardButton("🔒Cʟᴏsᴇ", callback_data = "close")
               ]]
            )
        )

    elif data == "help":
        await query.message.edit_text(
            text=mr.HELP_TXT.format(client.username),
            disable_web_page_preview = True,
            reply_markup=InlineKeyboardMarkup( [[
               InlineKeyboardButton("🔒Cʟᴏsᴇ", callback_data = "close")
               ]]
            )
        )

    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
