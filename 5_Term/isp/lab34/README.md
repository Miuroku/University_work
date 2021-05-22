# Интернет магазин на Django

Для запуска проекта необходимо:
1) Запустить (Установить и запустить) виртуальную среду (venv);
2) Установить все зависимости командой: 'pip install -r requirements.txt' (On linux: if package 'psycopg2' couldn't be installed use this command : 'pip install psycopg2-binary');
3) Добавить файл 'web-store/my_config.py' и занести туда настройки почты и БД (конкретно нужные настройки можно посмотреть в web_store/web_store/settings.py);
4) Запустить сервер командой: '/web_store python manage.py runserver'.
