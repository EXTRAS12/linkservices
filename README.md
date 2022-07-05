# linkservices

Установить и запустить виртуальное окружение
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

Запустить celery если требуется
celery -A config worker -l info
celery -A config beat -l info

Запустить бота если требуется
python manage.py bot


Вход в админку http://127.0.0.1:8000/superuser/ 
admin@admin.ru
пароль: admin

Пользователь
extra-kent@mail.ru
admin

(ПРОЕКТ не доделан )
Основное
-Переодический перевод баланса
-Парсер
-Всё из этих пунктов вытекающее

Не основное
-работу по фронту (пополнение,перевод, график)
-рефакторинг кода,мб вынос бизнес логики (когда всё будет готово)
-докер желательно




