## YamDB

### О проекте:

Данный проект представляет собой `API` для приложения отзывов `YamDB`.

### Как развернуть и запустить проект в контейнере:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:Kirill-Drozdov/infra_sp2.git
```

```
cd infra_sp2
```

В папке infra создать файл .env и заполнить его по шаблону .env.template,
используя свои данные для проекта:


Перейти в папку infra и запустить сборку контейнера:

```
cd infra
```

Далее все команды выполнять из текущей директории.

```
docker-compose up -d
```

Выполнить миграции:

```
docker-compose exec web python manage.py migrate
```

Создать суперпользователя:

```
docker-compose exec web python manage.py createsuperuser
```

Собрать статику в одну папку:

```
docker-compose exec web python manage.py collectstatic --no-input
```

Заполнить базу тестовыми данными:

```
docker-compose exec web python manage.py load_csv
```

Ваш проект запущен и готов к работе!


### Примеры запросов:

После запуска проекта пройти по адресу:

```
http://127.0.0.1:80/redoc/

```
Там будет доступна документация для проекта `API YamDB`,
представленая в формате `Redoc`.
В документации описано, как должен работать `API`.


### Об авторах проекта:
Проект выполнили: [Кирилл](https://github.com/Kirill-Drozdov), [Пётр](https://github.com/Kroks4502) 
и [Вячеслав](https://github.com/TikhomiroVyacheslav) -
студенты `Яндекс.Практикума`, готорые готовы с энтузиазмом учиться всему новому.


### Лицензия:

Данный проект имеет лицензию `MIT`.

Настоящим предоставляется бесплатное разрешение любому лицу, получившему
копию данного программного обеспечения и связанных с ним файлов документации
"Программное обеспечение", для действий в программном обеспечении без ограничений, включая,
помимо прочего, права использовать, копировать, изменять, объединять, публиковать,
распространять, сублицензировать и/или подавать копии программного обеспечени, а
также разрешить лицам, которым программное обеспечение предоставляется для этого при 
соблюдении следующих условий:

Вышеприведенные уведомления об авторских правах и это уведомление о разрешении должны быть включены во все
копии или существенные части программного обеспечения.
