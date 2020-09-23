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

