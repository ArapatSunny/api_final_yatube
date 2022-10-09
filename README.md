## Проект «API для Yatube»

### Описание: 
Проект «API для Yatube». "Yatube" - социальная сеть для публикации личных дневников. Где есть авторы, пользователи, возможности подписки на любимого автора, комментирования записей, размещения записей с привязкой к группе.

### О проекте:
Для аутентификации используются JWT-токены.
У неаутентифицированных пользователей доступ к API только на чтение. 
Аутентифицированным пользователям разрешено изменение и удаление своего контента; в остальных случаях доступ предоставляется только для чтения.
Исключение — эндпоинт /follow/: доступ к нему предоставляется только аутентифицированным пользователям.

### Технологии:
Python 3.8.5\
Django==2.2.16\
djangorestframework==3.12.4\
djangorestframework-simplejwt==4.7.2

Модели: Post, Group, Comment, Follow\

Для авторизованных пользователей:\
Обработка запросов\
модель Post: GET, POST, PUT, PATCH, DELETE\
модель Group: GET\
модель Comment: GET, POST, PUT, PATCH, DELETE\
модель Follow: GET, POST


### Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/ArapatSunny/api_final_yatube.git
```
```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:
```
python3 -m venv env
```
```
source env/bin/activate
```

Установить зависимости и перейти в корень проекта
```
pip install -r requirements.txt
```
```
cd yatube/
```

Создать файл .env с секретным ключом по примеру из .env.example
```
touch .env
```

Выполнить миграции и запустить проект:
```
python3 manage.py migrate
```
```
python3 manage.py runserver
```


### Примеры. Некоторые примеры запросов к API.

Запрос на получение постов:

```
http://127.0.0.1:8000/api/v1/posts/
```

Запрос на получение списка групп
```
http://127.0.0.1:8000/api/v1/groups/
```
