import telebot

bot = telebot.TeleBot('YOUR_BOT_API_TOKEN_HERE')

@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    bot.reply_to(message, "Hello! How can I assist you today?")


@bot.message_handler(content_types=['document', 'photo', 'sticker', 'video', 'audio', 'voice'])
def handle_media(message):
    if message.document:
        bot.reply_to(message, "You sent a document.")

    elif message.photo:
        bot.reply_to(message, "You sent a photo.")

    elif message.sticker:
        bot.reply_to(message, "You sent a sticker.")

    elif message.video:
        bot.reply_to(message, "You sent a video.")

    elif message.audio:
        bot.reply_to(message, "You sent an audio file.")

    elif message.voice:
        bot.reply_to(message, "You sent a voice message.")

    
@bot.message_handler(regexp='2024')
def handle_regexp(message):
    bot.reply_to(message, "You mentioned 2024!")


bot.polling()
