import json
import test
from bottle import post, request
from datetime import date

def get_all_news(): # Функция для получения всех заказов
    news = []
    with open('news.json') as file: # Получение данных из json файла
        file_content = file.read()
        news = json.loads(file_content)
    return news

