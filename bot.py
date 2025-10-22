import telebot
import random
import os
from googletrans import Translator
    # Замени 'TOKEN' на токен твоего бота
    # Этот токен ты получаешь от BotFather, чтобы бот мог работать
bot = telebot.TeleBot("TOKEN")
f=["Всемирная метеорологическая организация прогнозирует 70%-ную вероятность того, что среднее глобальное потепление в 2025–2029 годах составит более 1,5 °C.",
"Метеорологическое бюро Великобритании отмечает, что 2025 год может войти в тройку самых тёплых годов за всю историю наблюдения.",
"Исследование World Weather Attribution пришло к выводу, что во время аномальной жары в феврале 2025 года изменение климата сделало экстремальную жару как минимум на 2 °C выше и как минимум в десять раз более вероятной.", 
"В России в январе 2025 года наблюдалась чрезвычайно тёплая погода: в средней полосе европейской части России фиксировалась температура на 5–7 градусов выше нормы, а в Москве январь 2025 года мог стать вторым по теплоте за всю историю наблюдений.",
"Учёные предупреждают о том, что в 2025 году и последующих годах экстремальные погодные явления начнут происходить ещё чаще: увеличится количество пожаров, обильных осадков, которые могут приводить к наводнениям, и засух."]
    
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши /hello,/fact_ru,/fact_en,/fact_fr,/fact_es")

@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет! Как дела?")

 

@bot.message_handler(commands=['fact_ru'])
def send_fact(message):
    r=random.choice(f)
    bot.reply_to(message, f" факт: {r}")
@bot.message_handler(commands=['fact_en'])
def send_fact(message):
    r=random.choice(f)
    translator=Translator()
    translated=translator.translate(r,dest="en")
    bot.reply_to(message, f" факт: {translated.text}")
@bot.message_handler(commands=['fact_fr'])
def send_fact(message):
    r=random.choice(f)
    translator=Translator()
    translated=translator.translate(r,dest="fr")
    bot.reply_to(message, f" факт: {translated.text}")  
@bot.message_handler(commands=['fact_es'])
def send_fact(message):
    r=random.choice(f)
    translator=Translator()
    translated=translator.translate(r,dest="es")
    bot.reply_to(message, f" факт: {translated.text}") 



@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)
 




bot.polling()