import telebot
import openai
import json

# Загрузка данных из файла "data.json"
with open('data.json', 'r') as file:
    data = json.load(file)

# Извлечение токенов
API_TOKEN = data['telegram_token']
OPENAI_API_KEY = data['openai_token']

# Инициализация бота
bot = telebot.TeleBot(API_TOKEN)

# Установка ключа API для OpenAI
openai.api_key = OPENAI_API_KEY

# Приветственное сообщение
welcome_message = "Привет! Я бот, созданный на базе модели GPT-3 от OpenAI. Я готов отвечать на ваши вопросы и помочь вам. Просто задайте мне свой вопрос, и я постараюсь дать вам наилучший ответ."

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.reply_to(message, welcome_message)

# Обработчик входящих сообщений
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    # Загрузка истории переписки из файла
    chat_history = []
    try:
        with open('chat_history.json', 'r') as file:
            for line in file:
                data = json.loads(line)
                if 'user_message' in data:
                    chat_history.append(data['user_message'])
    except FileNotFoundError:
        pass
    
    # Добавление нового сообщения пользователя
    chat_history.append(message.text)
    
    # Генерация ответа с помощью модели GPT-3 от OpenAI
    prompt = '\n'.join(chat_history[-6:]) 
    response = openai.Completion.create(
        engine='davinci',
        prompt=prompt,
        max_tokens=75,  
        temperature=0.6,
        n=1,
        stop=None
    )
    reply = response.choices[0].text.strip()
    
    # Сохранение истории переписки в файл
    with open('chat_history.json', 'a') as file:
        json.dump({'user_message': message.text}, file)
        file.write('\n')
        json.dump({'bot_reply': reply}, file)
        file.write('\n')
    
    # Отправка ответа пользователю
    bot.reply_to(message, reply)

# Запуск бота
bot.polling()