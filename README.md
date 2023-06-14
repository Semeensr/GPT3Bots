<!DOCTYPE html>
<html>
<head>
  <style>
    body {
      font-family: Arial, sans-serif;
      line-height: 1.6;
    }
    
    h1 {
      color: #333;
      font-size: 24px;
      font-weight: bold;
      margin-bottom: 10px;
    }
    
    h2 {
      color: #333;
      font-size: 18px;
      font-weight: bold;
      margin-bottom: 5px;
    }
    
    ol {
      margin-left: 20px;
      margin-bottom: 20px;
    }
    
    li {
      margin-bottom: 5px;
    }
    
    pre {
      background-color: #f5f5f5;
      padding: 10px;
    }
  </style>
</head>
<body>
  <h1>Развертывание бота на сервере</h1>
  
  <h2>Шаг 1: Настройка сервера</h2>
  <ol>
    <li>Зарегистрируйтесь на платформе облачного хостинга или получите доступ к серверу.</li>
    <li>Установите операционную систему на сервер (например, Ubuntu).</li>
    <li>Убедитесь, что на сервере установлен Python версии 3.x.</li>
  </ol>
  
  <h2>Шаг 2: Клонирование проекта</h2>
  <ol>
    <li>Откройте терминал на сервере.</li>
    <li>Перейдите в каталог, в котором вы хотите разместить проект.</li>
    <li>Выполните следующую команду для клонирования проекта на сервер:</li>
  </ol>
  <pre><code>git clone https://github.com/Semeensr/GPT3Bots.git</code></pre>
  
  <h2>Шаг 3: Установка зависимостей</h2>
  <ol>
    <li>Установите зависимости, указанные в файле requirements.txt, с помощью команды:</li>
  </ol>
  <pre><code>pip install -r requirements.txt</code></pre>
  
  <h2>Шаг 4: Настройка токенов</h2>
  <p>В файле data.json замените telegram_token и openai_token на свои, которые получили при создании бота и OpenAI аккаунта.</p>
  
  <h2>Шаг 5: Запуск бота</h2>
  <p>Запустите бота с помощью команды:</p>
  <pre><code>python GPT3Bots.py</code></pre>
  
  <p>После выполнения этих шагов ваш бот должен успешно запуститься на сервере. Убедитесь, что ваш сервер имеет доступ к Интернету, чтобы бот мог связываться с платформой Telegram и API OpenAI.</p>
</body>
</html>
