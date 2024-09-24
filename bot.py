import telebot
import os
import requests
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TELEGRAM_TOKEN')

BACKEND_URL = os.getenv('BACKEND_URL')

bot = telebot.TeleBot(TOKEN)

def get_test_data_from_backend(data_id):
    try:
        response = requests.get(f"{BACKEND_URL}test/{data_id}")
        if response.status_code == 200:
            return response.json()
        else:
            return f"Ошибка: {response.status_code}"
    except Exception as e:
        return f"Ошибка при запросе данных: {str(e)}"

@bot.message_handler(commands=['get_data'])
def get_data(message):
    try:
        data_id = message.text.split()[1]
        backend_data = get_test_data_from_backend(data_id)
        bot.reply_to(message, f"Данные с бэкенда: {backend_data}")
    except IndexError:
        bot.reply_to(message, "Пожалуйста, укажи ID после команды /get_data")
    except Exception as e:
        bot.reply_to(message, f"Ошибка: {str(e)}")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "2dac68fb-4c53-4edf-91f8-f36f29e8227f   74d361f4-edfd-4446-99eb-561d151a0cda   9a53ac90-a086-4dec-9924-67d3fd3980f3")

if __name__ == '__main__':
    print("Бот запущен...")
    bot.infinity_polling()
