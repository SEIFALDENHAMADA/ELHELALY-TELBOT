import os
from telebot import TeleBot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from api import get_gpt_response

BOT_TOKEN = os.environ['BOT_TOKEN']
bot = TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    chat_username = message.chat.first_name
    text = f"""حياك الله ( {chat_username} )
  اسمي الهلالي ..
 انا نموذج مشتق من شركة OPEN
تم تطويري من قبل مطور مصري ( سيف الدين ) وانا دائماً موجود لمساعدتك بما استطيع ان اساعدك به 
كيف يمكنني مساعدتك اليوم؟ 

God bless you ( {chat_username} )
My name is ELHELALY .. I am a model derived from the OPEN company. It was developed by the Egyptian developer (Seif Alden) and I am always available to help you with what I can help you with.
How can I help you today?"""

    #Create a share button
    keyboard = InlineKeyboardMarkup()
    share_button = InlineKeyboardButton("SHARE WITH YOUR FRINDS 👬", switch_inline_query="")
    keyboard.add(share_button)

    bot.send_message(chat_id, text, reply_markup=keyboard)

    return

@bot.message_handler()
def massage(message):
    chat_id = message.chat.id
    prompt = message.text
    bot.send_chat_action(chat_id, action='typing')
    res_text = get_gpt_response(prompt)
    bot.send_message(chat_id, res_text)

    return

bot.infinity_polling()
