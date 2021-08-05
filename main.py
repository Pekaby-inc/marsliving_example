import requests
import os

# Просим пользователя ввести интересующий id
ID = input('Enter ID: ')

# Вставляем полученый id в ссылку
url = 'https://marsliving.ru/api/frame?id='+ID 

# Делаем запрос к api
r = requests.get(url)

# Проверяем, что запрос прошел успешно
if r.status_code != 200: exit('Didn\'t find')

response = r.text

# Записываем ответ формата JSON в переменную
data = r.json()

# Создаем папку с одноименным ID
try:
    os.mkdir(ID)
except:
    exit("Данная директория уже существует!")

# Создаем функцию для загрузки картинок
def download(image, name):
    r = requests.get(image) # Получаем картинку
    f = open(ID + '/' + name + '.jpg', 'wb') # Создаем файл
    f.write(r.content) # Записываем содержимое (бинарный код)
    f.close() # Закрываем файл

# Скачиваем главное изображение
download(data['image'], data['frame'])

# Перебираем ответ API и загружаем дополнительные кадры
for additional in data['additional_frames']:
    download(additional['image'], additional['frame'])

# Перебираем ответ API и загружаем исходные кадры
for full in data['full_frames']:
    download(full['image'], full['frame'])