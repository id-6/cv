import telebot
import requests
import re
from datetime import datetime

bot = telebot.TeleBot('6044876527:AAH9DdgcP9xhAK2HcWu9HGgw_Dx4qjF4P7E')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'مرحبا، يمكنك إرسال اسم المستخدم الخاص بحساب تيك توك للحصول على معلومات عن الحساب')

@bot.message_handler(func=lambda message: True)
def get_info(message):
    try:
        response = requests.get(f'https://www.tiktok.com/@{message.text}')
        patrek = response.text

        getting = str(patrek.split('"UserModule":')[1]).split('"RecommendUserList"')[0]
        
        try:
            id = str(getting.split('id":"')[1]).split('",')[0]
        except:
            id = ""
        
        try:
            name = str(getting.split('nickname":"')[1]).split('",')[0]
        except:
            name = ""
        
        try:
            bio = str(getting.split('signature":"')[1]).split('",')[0]
        except:
            bio = ""
        
        try:
            country = str(getting.split('region":"')[1]).split('",')[0]
        except:
            country = ""
        
        try:
            private = str(getting.split('privateAccount":')[1]).split(',"')[0]
        except:
            private = ""
        
        try:
            verified = str(getting.split('"verified":')[1]).split(',')[0]
        except:
            verified = ""
        
        try:
            secuid = re.search(r'"secUid":"(.+?)"', patrek).group(1)
        except:
            secuid = ""
            
        try:
            user_created_time = re.search(r'"createTime":"(.+?)"', patrek).group(1)
            user_created_time = datetime.fromtimestamp(int(user_created_time)).strftime('%Y-%m-%d %H:%M:%S')
        except:
            user_created_time = ""
            
        try:
            account_region = re.search(r'"accountRegion":"(.+?)"', patrek).group(1)
        except:
            account_region = ""
        
        try:
            followers = str(getting.split('followerCount":')[1]).split(',"')[0]
        except:
            followers = ""
        
        try:
            following = str(getting.split('followingCount":')[1]).split(',"')[0]
        except:
            following = ""
        
        try:
            like = str(getting.split('heart":')[1]).split(',"')[0]
        except:
            like = ""
        
        try:
            video = str(getting.split('videoCount":')[1]).split(',"')[0]
        except:
            video = ""
        
        kls = f"""───────────────
ᴜѕᴇʀɴᴀᴍᴇ ➢ {message.text}
ɴᴀᴍᴇ ➢ {name}
ғᴏʟʟᴏᴡᴇʀѕ ➢ {followers}
ғᴏʟʟᴏᴡɪɴɢ ➢ {following}
ʟɪᴋᴇ ➢ {like}
ᴠɪᴅᴇᴏ ➢ {video}
ᴘʀɪᴠᴀᴛᴇ ➢ {private}
ᴠᴇʀɪғɪᴇᴅ ➢ {verified}
sᴇᴄᴜɪᴅ ➢ {secuid}
ᴜsᴇʀ ᴄʀᴇᴀᴛᴇᴅ ᴛɪᴍᴇ ➢ {user_created_time}
ᴀᴄᴄᴏᴜɴᴛ ʀᴇɢɪᴏɴ➢ {account_region}
ʙɪᴏɢʀᴀᴘʜʏ ➢ {bio}
ᴄᴏᴜɴᴛʀʏ ➢ {country}
───────────────"""
        
        bot.reply_to(message, kls)
    
    except:
        bot.reply_to(message, 'حدث خطأ في الحصول على المعلومات. تأكد من صحة اسم المستخدم وحاول مرة أخرى')

bot.polling()
