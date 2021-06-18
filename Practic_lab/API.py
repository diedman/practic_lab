import json
import check_mail
from bottle import post, request
from datetime import date

# Функция для получения всех новинок
def get_all_news(): 
    news = []
    # Получение данных из json файла
    with open('news.json') as file: 
        file_content = file.read()
        news = json.loads(file_content)
    return news

# Функция для добавления новинки
def create_new(new): 
    news = []
    try:
        # Получение данных из json файла
        with open('news.json') as f: 
            file_content = f.read()
            news = json.loads(file_content)
    except Exception:
        news = []
    news.append(new) 
    # Запись в файл
    file = open("news.json", 'w') 
    file.write(json.dumps(news))
    file.close()

@post('/newsAdd', method='post')
def prepare_new():
    title = request.forms.get('TITLE')
    email = request.forms.get('EMAIL')
    author = request.forms.get('NICK')
    text = request.forms.get('NEW_TEXT')
    
    # Проверка заполнености полей и mail стандарту
    if not title:
        return "Enter title"
    if not check_mail.mail_check(email):
        return "Enter correct email!"
    if not author:  
        return "Enter Nick"
    if not text:
        return "Enter text for new"
    # Создание объекта новинки
    new = {
    "title": title,
    "date": date.today().strftime('%d.%m.%Y'),
    "new_text": text,
    "author": author,
    "email": email
    }
    # Занесениt в файл
    create_new(new)
    return "Your new was created"

