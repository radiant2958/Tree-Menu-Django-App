# Приложение для создания древовидного меню в Django с использованием template tags. Поддерживаются следующие функции:

- Меню разворачивается согласно выбранному пункту и первому уровню вложенности.
- Меню хранится в базе данных и редактируется через админку Django.
- Определение активного пункта меню на основе текущего URL.
- Поддержка нескольких меню на одной странице, определяемых по названию.
- Переход по URL пунктов меню, заданным явно или через именованные URL.
- Эффективная отрисовка меню с одним запросом к базе данных.

## Установка
1. Клонируйте репозиторий:
   ```sh
   git clone https://github.com/radiant2958/Tree-Menu-Django-App
   cd tree_menu

2. Установите зависимости:
   ```sh
   pip install -r requirements.txt
   
3. Примените миграции:
   ```sh
   python manage.py migrate

4. Создайте суперпользователя:
   ```sh
   python manage.py createsuperuser
5. Запустите сервер разработки:
   ```sh
   python manage.py runserver

## Использование

1. Откройте http://127.0.0.1:8000/admin/ и создайте новое меню.

- Нажмите "Добавить меню".
- Введите название меню (например, "Главное меню").
- Нажмите "Сохранить".
  
2. Перейдите к созданному меню и добавьте элементы меню:

- Введите название элемента меню (например, "Главная страница").
- Введите URL или именованный URL для пункта меню.
- Введите имя URL, если необходимо
- Если элемент меню является дочерним, выберите его родительский пункт(parent).
- Укажите порядок отображения (меньшие числа отображаются первыми)(Order).
- Нажмите "Сохранить и добавить другой", чтобы продолжить добавление пунктов меню, или "Сохранить", чтобы завершить.

## Интеграция в шаблон
 ```sh
 {% load menu_tags %}
 {% draw_menu 'main_menu' %}


