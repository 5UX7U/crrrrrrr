
import asyncio
import os

from AnonX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonX import app
import requests
import pyrogram
from pyrogram import Client, emoji 
from config import *
from pyrogram import filters
from strings.filters import command
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from pyrogram.errors import MessageNotModified








@app.on_message(command(["الاوامر", "اوامر"]) & filters.group & ~filters.edited) 
async def zdatsr(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/be8fb2f02cf57e1725ccd.jpg",
        caption=f"""**✨ ¦ اليك قائمة اوامر من سورس\n│ \n└: [★᚜⌞ 𝘾𝙍 • 𝙎𝙊𝙐𝙍𝘾𝙀 ⌝᚛★](https://t.me/pp_g3)**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "★᚜ اوامر اساسيه ᚛★", callback_data="vegax"),
                ],[
                    InlineKeyboardButton(
                        "★᚜ اوامر الادمن ᚛★", callback_data="honakks"),
                    InlineKeyboardButton(
                        "★᚜ اوامر القناه ᚛★", callback_data="alskksks"),
                ],[
                    InlineKeyboardButton(
                        "★᚜⌞ 𝙏َِ𝙊َِ𝙈ِ༄► ⌝᚛★️", url=f"https://t.me/DEV_TOM"),                        
                ],[
                    InlineKeyboardButton(
                       "★᚜⌞ 𝘾𝙍 • 𝙎𝙊𝙐𝙍𝘾𝙀 ⌝᚛★", url=f"https://t.me/pp_g3"),                        
                ],
            ]
        ),
    )



@app.on_callback_query(filters.regex("vegax"))
async def vegax(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""**⩹━★⊷⌯⌞ 𝘾𝙍 • 𝙎𝙊𝙐𝙍𝘾𝙀 ⌝⌯⊶★━⩺**
       
اليك قائمة اوامر التشغيل فالجروب او القناه✅

★¦ لتشغيل اغنيه اكتب : تشغيل او شغل او /play
★¦ لتشغيل فيديو اكتب : /vplay او فيديو او فديو
★¦ لأنهاء الاغنيه اكتب : انهاء او اسكت او ايقاف /end
★¦ لايقاف الاغنيه مؤقت اكتب : وقف او توقف او /pause
★¦ لتكملة الاغنيه من الايقاف المؤقت اكتب : كمل او استئناف او /resume
★¦ لتخطي الاغنيه اكتب : تخطي او /skip
★¦ لكتم البوت في الكول اكتب : ميوت او /mute
★¦ لألغاء كتم البوت في الكول اكتب : فك ميوت او /unmute
★¦ لاعادة تشغيل البوت اكتب : ريستارت او /restart 
★¦ لمعرفه كلمات اي اغنيه : /lyrics او كلمات
★¦ لتحميل موسيقي او فيديو : /song او تحميل او اغنيه
★¦ لمعرفه الاغاني الموجوده في قائمه الانتظار : /queue
★¦ لعرض سرعه البوت : بنج او /ping
★¦ لتحويل لغه البوت : اللغه او /lang او language

**⩹━★⊷⌯⌞ 𝘾𝙍 • 𝙎𝙊𝙐𝙍𝘾𝙀 ⌝⌯⊶★━⩺**""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "◁", callback_data="hpdtsnju"),
               ],
          ]
        ),
    )




@app.on_callback_query(filters.regex("honakks"))
async def honakks(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""**⩹━★⊷⌯⌞ 𝘾𝙍 • 𝙎𝙊𝙐𝙍𝘾𝙀 ⌝⌯⊶★━⩺**
       
✅ اليك قائمة اوامر الادمن ,

★¦ جميع الاوامر خاصه ب الادمن فقط .

★¦ لعرض سرعه البوت اكتب : بنج .
★¦ للتحكم في لغه البوت اكتب : /اللغه .
★¦ لعرض اعدادات البوت اكتب : الاعدادات .

★¦ ثانيا اليك اوامر الرتب .

★¦ لرفع ادمن في الجروب اكتب : رفع مطور . 
★¦ لتنزيل ادمن في الجروب اكتب : تنزيل مطور . 
★¦ لعرض قائمه الادمنيه اكتب : المطورين .

★¦ ثالثا اليك اوامر الحظر .

★¦ لحظر عضو من الجروب اكتب : حظر ميوزك. 
★¦ لالغاء حظر عضو من الجروب اكتب : الغاء حظر. 
★¦ لعرض قائمه المحظورين اكتب : المحظورين . 

**⩹━★⊷⌯⌞ 𝘾𝙍 • 𝙎𝙊𝙐𝙍𝘾𝙀 ⌝⌯⊶★━⩺**""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "◁", callback_data="hpdtsnju"),
               ],
          ]
        ),
    )



@app.on_callback_query(filters.regex("alskksks"))
async def alskksks(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""**⩹━★⊷⌯⌞ 𝘾𝙍 • 𝙎𝙊𝙐𝙍𝘾𝙀 ⌝⌯⊶★━⩺**

✅ اوامر تشغيل البوت في القناه

★¦ قم برفع البوت مشرف بالقناه وبالجروب
او 
★¦ استخدم /channelplay او ربط + معرف القناه للربط
★¦ ثم استخدم الاوامر بالاسفل للتشغيل
★¦ لتشغيل اغنيه اكتب : تشغيل او شغل او /play
★¦ لتشغيل فيديو اكتب : /vplay : فيديو : فديو
★¦ لأنهاء الاغنيه اكتب : ايقاف او اسكت او /end
★¦ لايقاف الاغنيه مؤقت اكتب : وقف او توقف او /pause
★¦ لتكملة الاغنيه من الايقاف المؤقت اكتب : كمل او استئناف او /resume
★¦ لتخطي الاغنيه اكتب : تخطي او /skip
★¦ لكتم البوت في الكول اكتب : ميوت او /mute
★¦ لألغاء كتم البوت في الكول اكتب : فك ميوت او /unmute
★¦ لتشغيل اغنيه : /cplay
★¦ لتشغيل فيديو : /cvplay
★¦ لأنهاء الاغنيه  : /cstop
★¦ لايقاف الاغنيه مؤقت : /cpause
★¦ لتكملة الاغنيه  : /cresume
★¦ لتخطي الاغنيه : /cskip
★¦ لكتم البوت في الكول  : /cmute
★¦ لألغاء كتم البوت في الكول  :  /cunmute
★¦ لتقديم الاغنيه للامام /seek و الرقم

**⩹━★⊷⌯⌞ 𝘾𝙍 • 𝙎𝙊𝙐𝙍𝘾𝙀 ⌝⌯⊶★━⩺**""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "◁", callback_data="hpdtsnju"),
               ],
          ]
        ),
    )


