from pyrogram import filters
from utils.youtube import download_audio

@bot.on_message(filters.command("play"))
def play(_, msg):
    query = msg.text.split(None, 1)[1]

    msg.reply("🎵 جاري التشغيل...")

    audio = download_audio(query)

    msg.reply_audio(audio, caption="🎶 يتم التشغيل الآن")
