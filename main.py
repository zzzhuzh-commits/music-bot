from pyrogram import Client, filters
from pytgcalls import PyTgCalls
from pytgcalls.types import InputAudioStream

vc = PyTgCalls(bot)
from config import *

bot = Client(
    "musicbot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

vc = PyTgCalls(bot)

# START
@bot.on_message(filters.command("start"))
def start(_, msg):
    msg.reply("🎵 بوت ميوزك احترافي شغال!")

# HELP
@bot.on_message(filters.command("help"))
def help_cmd(_, msg):
    msg.reply("""
🎵 أوامر البوت:

/play اسم الاغنية
/pause
/resume
/skip
/stop
/queue

👮 حماية:
/auth
/block
/unblock
""")

# PING
@bot.on_message(filters.command("ping"))
def ping(_, msg):
    msg.reply("🏓 Online!")

bot.start()
vc.start()
print("Bot Started 🚀")
bot.idle()
