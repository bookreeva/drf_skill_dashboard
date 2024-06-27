<a id="toup"></a>
<h1>Skill Dashboard API</h1>
<h2>Добро пожаловать!</h2>
<h3>Данный проект представляет собой API формирования новых здоровых привычек с интеграцией напоминаний в telegram.</h3>

<h3>Перед началом использования программы создайте файл .env и 
заполните его данными для нижеприведенных переменных (или скопируйте из .env-sample):</h3>


| Шаблон для .env |
|-----------------|

```text 
SECRET_KEY=
DEBUG=
ALLOWED_HOSTS=

POSTGRES_DB=
POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_HOST=
POSTGRES_PORT=
PGDATA=

LANGUAGE_CODE=

TG_TOKEN=
TG_URL=

CELERY_BROKER_URL=
CELERY_RESULT_BACKEND=
 ```

<h4>✔️ Клонируйте данный репозиторий</h4>
<h4>✔️ Создайте виртуальное окружение и активируйте его</h4>
<h4>✔️ Установите зависимости из файла requirements.txt</h4>

<h4>✔️ Далее выполните следующие команды: </h4>

| Описание                                        | Команды                                      |
|-------------------------------------------------|----------------------------------------------|
| Создать БД в POSTGRESQL                         | ```psql -U postgres```                       |
| Применить миграции                              | ```python3 manage.py migrate```              |
| Создать суперпользователя для доступа в админку | ```python3 manage.py createsuperuser```      |
| Для периодических задач использовать (worker)   | ```celery -A config worker -l INFO```        |
| (beat)                                          | ```celery -A config beat -l info -S django```|

<h4>✔️ Запуск с помощью DOCKER: </h4>
<h4> - установить Docker;</h4>
<h4>✔️ Далее выполните следующие команды: </h4>

| Описание                                        | Команды                                      |
|-------------------------------------------------|----------------------------------------------|
| Собрать образ                                   | ```docker-compose build```                   |
| Запустить контейнер                             | ```docker-compose up```                      |
| Либо выполнить две команды сразу                | ```docker-compose up --build -d```           |
| Остановить                                      | ```control + C```                            |


 <div style="display: flex; align-items: center;">
    <div style="display: inline-block; margin: 2px;" >


</div>
  </div>

## Ошибки и улучшения

Если вы обнаружили ошибки, у вас есть предложения по улучшению данного проекта
или у вас есть вопросы по использованию веб-приложения, пожалуйста, присылайте pull request.
