from config import OWNER_ID

admins = []

def is_owner(user_id):
    return user_id == OWNER_ID

@bot.on_message(filters.command("auth"))
def auth(_, msg):
    if not is_owner(msg.from_user.id):
        return msg.reply("❌ مو مسموح")

    user = msg.text.split()[1]
    admins.append(int(user))
    msg.reply("✅ تم إضافة الأدمن")

@bot.on_message(filters.command("block"))
def block(_, msg):
    msg.reply("🚫 تم الحظر (نظام تجريبي)")
