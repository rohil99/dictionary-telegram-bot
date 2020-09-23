import telebot
from bs4 import BeautifulSoup
import requests
from pprint import pprint

bot=telebot.TeleBot('ENTER YOUR BOT KEY HERE')

@bot.message_handler(commands=['getmeaning','start'])
def greeting_message(message):
    bot.reply_to(message, "Here u can get the meaning and pronunciation of the words\n\nType any word to get its meaning and pronunciation.")

@bot.message_handler(func=lambda message:True)
def get_meaning(message):
    url='https://www.oxfordlearnersdictionaries.com/us/definition/english/'+message.text.lower()
    page=requests.get(url)
    soup=BeautifulSoup(page.text, 'html.parser')
    pprint(soup)
    try:
        try:
            mp3link=soup.find('div', {'class':'sound audio_play_button pron-uk icon-audio'}).get('data-src-mp3')
            bot.reply_to(message, mp3link)
        except:
            bot.reply_to(message, 'Pronunciation not found')
            
        try:
            definition=soup.find('span',{'class':'def'}).text
            bot.reply_to(message, definition)
        except:
            bot.reply_to(message, 'Meaning not found')
    except:
        bot.reply_to(message, 'Something went wrong')

bot.polling()

# import asyncio
# import telepot
# import telepot.aio
# from telepot.aio.loop import MessageLoop
# import requests
# from pprint import pprint
# from bs4 import BeautifulSoup

# async def handle(msg):
#     global chat_id
#     content_type, chat_type, chat_id = telepot.glance(msg)
#     print(content_type, chat_type, chat_id)
#     pprint(msg)
#     username=msg['chat']['first_name']
#     if content_type=='text':
#         if msg['text']!='/start':
#             text=msg['text']
#             text=text.strip()
#             await get_meaning(text.lower())
#     # await bot.sendMessage(chat_id,msg)


# async def get_meaning(text):
#     url='https://www.oxfordlearnersdictionaries.com/us/definition/english/'+text
#     page=requests.get(url)
#     soup=BeautifulSoup(page.text, 'html.parser')
#     pprint(soup)
#     try:
#         try:
#             mp3link=soup.find('div', {'class':'sound audio_play_button pron-uk icon-audio'}).get('data-src-mp3')
#             await bot.sendAudio(chat_id=chat_id, audio=mp3link)

#         except:
#             await bot.sendMessage(chat_id, 'Pronunciation not found')
            
#         try:
#             definition=soup.find('span',{'class':'def'}).text
#             await bot.sendMessage(chat_id, definition)
#         except:
#             await bot.send_Message(chat_id, 'Meaning not found')
#     except:
#         await bot.sendMessage(chat_id, 'Something went wrong')

# TOKEN='1343300119:AAH-pXs4Saf74nHF1PG_qTnwyfg36UaH_Kk'
# bot=telepot.aio.Bot(TOKEN)
# loop=asyncio.get_event_loop()
# loop.create_task(MessageLoop(bot, handle).run_forever())
# print('listening')
# loop.run_forever()










# import requests
# from pprint import pprint
# from bs4 import BeautifulSoup

# def get_meaning(text):
#     url='https://www.oxfordlearnersdictionaries.com/us/definition/english/'+text
#     page=requests.get(url)
#     soup=BeautifulSoup(page.text, 'html.parser')
#     pprint(soup)
#     try:
#         try:
#             mp3link=soup.find('div', {'class':'sound audio_play_button pron-uk icon-audio'}).get('data-src-mp3')
#             pprint(mp3link)
#         except:
#             pprint('pronunciation not found')
#         try:
#             definition=soup.find('span',{'class':'def'}).text
#             pprint(definition)
#         except:
#             pprint("meaning not found")
#     except:
#         pprint("something went wrong")





# word='beautiful'
# word=word.strip()
# get_meaning(word.lower())
