import telebot
import requests
import unicodedata
from bs4 import BeautifulSoup
from datetime import datetime
from time import sleep

token ="5876070267:AAGrxdWNq5IN7oKy1M7oBfo8jdzZYcBCDb4"
bot = telebot.TeleBot(token)
# @BRoK8 @Crrazy_8

@bot.message_handler(commands=['start'])
def Welcome(message):
    
    bot.reply_to(message,"Welcome to the TikTok account information bot",reply_markup=telebot.types.InlineKeyboardMarkup([
                     [telebot.types.InlineKeyboardButton(text='Dev',url='@SourceAzoth')]]))

@bot.message_handler(content_types=["text"])
def info(message):
    username = message.text.strip()
    if username.startswith('@'):
        username = username[1:]
    
    data = get_tiktok_user_info(username)
    if data:
        id = data['user_id']
        name = data['name']
        followers = data['followers']
        following = data['following']
        time = data['user_create_time']
        last = data['last_change_name']
        acc = data['account_region']
        
        country_emoji = unicodedata.lookup(f"REGIONAL INDICATOR SYMBOL LETTER {acc[0]}")
        country_emoji += unicodedata.lookup(f"REGIONAL INDICATOR SYMBOL LETTER {acc[1]}")
        
        
        keyboard = telebot.types.InlineKeyboardMarkup(row_width=1)
        keyboard.add(
        telebot.types.InlineKeyboardButton(f'- name ({name})â¢', callback_data='1'),
        telebot.types.InlineKeyboardButton(f'- followers ({followers})â¢', callback_data='2'),
        telebot.types.InlineKeyboardButton(f'- following ({following})â¢',callback_data='3'),
        telebot.types.InlineKeyboardButton(f'- Last name change ({last})â¢',callback_data='4'),
        telebot.types.InlineKeyboardButton(f'- id ({id})â¢',callback_data="5"),
        telebot.types.InlineKeyboardButton(f'- date ({time})â¢',callback_data="6"),
        telebot.types.InlineKeyboardButton(f'- country ({country_emoji} - {acc})â¢',callback_data="7")
        )
        b = bot.reply_to(message,'wait ...')
        bot.delete_message(chat_id=message.chat.id, message_id=b.message_id)
        bot.reply_to(message,'''- Done sir .
- By : @BRoK8 ($) Ch : @Crrazy_8 .''',reply_markup=keyboard)
    else:
        bot.reply_to(message,"-There are problems with the search.")

def get_tiktok_user_info(username):
    headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"}
    r = requests.get(f"https://www.tiktok.com/@{username}", headers=headers)
    server_log = str(r.text)

    try:
        soup = BeautifulSoup(server_log, 'html.parser')
        script = soup.find(id='SIGI_STATE').contents
        data = str(script).split('},"UserModule":{"users":{')[1]
        
        user_info = {}
        user_info['user_id'] = data.split('"id":"')[1].split('",')[0]
        user_info['name'] = data.split(',"nickname":"')[1].split('",')[0]
        user_info['followers'] = data.split('"followerCount":')[1].split(',')[0]
        user_info['following'] = data.split('"followingCount":')[1].split(',')[0]
        user_info['user_create_time'] = user_create_time(int(user_info['user_id']))
        user_info['last_change_name'] = datetime.fromtimestamp(int(data.split('"nickNameModifyTime":')[1].split(',')[0]))
        user_info['account_region'] = data.split('"region":"')[1].split('"')[0]
        
        return user_info
    except IndexError:
        return None

def user_create_time(url_id):
    binary = "{0:b}".format(url_id)
    i = 0
    bits = ""
    while i < 31:
        bits += binary[i]
        i += 1
    timestamp = int(bits, 2)
    dt_object = datetime.fromtimestamp(timestamp)
    return dt_object
# @BRoK8 @Crrazy_8

bot.infinity_polling()
