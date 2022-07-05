# linkservices

1. Установить и запустить виртуальное окружение
2. pip install -r requirements.txt
3. python manage.py migrate
4. python manage.py runserver

Запустить celery если требуется
1. celery -A config worker -l info
2. celery -A config beat -l info

Запустить бота если требуется
1. python manage.py bot


Вход в админку http://127.0.0.1:8000/superuser/ 
1. admin@admin.ru
2. пароль: admin

Пользователь
1. extra-kent@mail.ru
2. admin

(ПРОЕКТ не доделан )
Основное
1. Переодический перевод баланса
2. Парсер
3. Всё из этих пунктов вытекающее

Не основное
1. работу по фронту (пополнение,перевод, график)
2. рефакторинг кода,мб вынос бизнес логики (когда всё будет готово)
3. докер желательно




