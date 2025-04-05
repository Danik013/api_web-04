# Фотографии космоса в Telegram-канале.

Скрипты позволяют загружать фотографии **NASA** и **SpaseX**, а также публиковать в **Telegram**-канале при помощи бота.
1. [**`fetch_nasa_apod_images.py`**](fetch_nasa_apod_images.py) - *Astronomy Picture of the Day* Получаем фото дня в космической тематике.
2. [**`fetch_nasa_epic_images.py`**](fetch_nasa_epic_images.py) - *Earth Polychromatic Imaging Camera* Получаем полихроматические фото земли крайней даты.
3. [**`fetch_spacex_images.py`**](fetch_spacex_images.py) - Загружаем фотографии запуска **SpaseX**
4. [**`get_one_photo_of_space_bot.py`**](get_one_photo_of_space_bot.py) - Бот отправляет фото выбранное по названию. Если не нашел, отправляет случайное фото из папки.
5. [**`get_photos_of_space_bot.py`**](get_photos_of_space_bot.py) - Бот отправляет все фото из папки по порядку в бесконечном цикле по таймингу.

## Как установить 

+ Python3 должен быть уже установлен. Затем используйте pip (или pip3, есть конфликт с Python2) для установки зависимостей:
  >pip install -r requirements.txt
+ Для корректной работы `python-telegram-bot` в версии `13.2` используем python в версии не более 3.10
  >pip install python-telegram-bot==13.2

## Как пользоваться **`fetch_nasa_apod_images.py`**

+ Получите API-ключ по ссылке - [*Generate API Key*](https://api.nasa.gov/) после несложной регистрации
  >Ключ помещаем в **.env** файл
  >используем `load_dotenv` и `os`
  ```python
  load_dotenv()
  token = os.environ["NASA_API_KEY"]
  ```
+ в разделе [NASA-APOD](https://api.nasa.gov/#apod) получаем необходимы данные. В данном случае:
  >`GET https://api.nasa.gov/planetary/apod` - базовая ссылка для **HTTP-запроса** к которой применяются параметры.
  >`Query Parameters` - таблица с параметрами.

### Пример использования **`fetch_nasa_apod_images.py`**

1. Запускаем программу в командной строке:
   >C:\......>python fetch_nasa_apod_images.py
   *Результат: в директории проекта создается папка `**images**` и в ней сохранятся последнее фото дня.
2. Запускаем программу в командной строке указывая дату в формате **YYYY-MM-DD**:
   >C:\......>python fetch_nasa_apod_images.py 2025-02-25
   *Результат: в директории проекта создается папка `**images**` и в ней сохранятся фото дня указанной даты.

## Как пользоваться **`fetch_nasa_epic_images.py`**

+ Получите API-ключ по ссылке - [*Generate API Key*](https://api.nasa.gov/) после несложной регистрации
  >Ключ помещаем в **.env** файл
  >используем `load_dotenv` и `os`
  ```python
  load_dotenv()
  token = os.environ["NASA_API_KEY"]
  ```
+ в разделе [NASA-EPIC](https://api.nasa.gov/#epic) получаем необходимы данные. В данном случае:
  >`https://api.nasa.gov/EPIC/api/natural` - базовая ссылка для **HTTP-запроса** к которой применяются параметры.
  >`Querying by Date(s)` - таблица с параметрами.
  >`https://api.nasa.gov/EPIC/archive/natural` - архив откуда получаем фото, используя `id` и `date` и предыдущик пунктов

### Пример использования **`fetch_nasa_epic_images.py`**

1. Запускаем программу в командной строке:
   >C:\......>python fetch_nasa_epic_images.py
   *Результат: в директории проекта создается папка `**images**` и в ней сохранятся последние фотографии из раздела **EPIC**.

## Как пользоваться **`fetch_spacex_images.py`**

+ API-ключ в данном сервисе не нужен. 
+ в репозитарии [SpaceX REST API](https://github.com/r-spacex/SpaceX-API) получаем необходимы данные. В данном случае:
  >`https://api.spacexdata.com/v5/launches/latest` - ссылка для **HTTP-запроса** последнего запуска.
  >`https://api.spacexdata.com/v5/launches` - все запуски. используя `id` можно получить фото при их наличии.

### Пример использования **`fetch_spacex_images.py`**

1. Запускаем программу в командной строке:
   >C:\......>python fetch_spacex_images.py
   *Результат: в директории проекта создается папка `**images**` и в ней, ___если таковые имеются___, сохранятся фотографии последнего запуска **SpaseX**.
2. Запускаем программу в командной строке, указывая `id` запуска:
   >C:\......>python fetch_spacex_images.py 5eb87d42ffd86e000604b384
   *Результат: в директории проекта создается папка `**images**` и в ней, ___если таковые имеются___, сохранятся фотографии конкретного запуска **SpaseX**.

## Как пользоваться **`get_one_photo_of_space_bot.py`**

+ Получите API-токен с помошью - [*Отец ботов*](https://telegram.me/BotFather), создав бот.
+ Создаем телеграм канал, получаем `chat_id` и делаем нашего бота администратором
  >Ключ и chat_id помещаем в **.env** файл
  >используем `load_dotenv` и `os`
  ```python
  load_dotenv()
  token = os.environ["TELEGRAM_TOKEN"]
  chat_id = os.environ["TG_CHAT_ID"]
  ```

### Пример использования **`get_one_photo_of_space_bot.py`**

1. Запускаем программу в командной строке указав название фото:
   >C:\......>python get_one_photo_of_space_bot.py nasa_epic_13.png
   *Результат: бот отправляет в группу фото с соответствующим названием из папки `**images**`. Если по имени фото не найдено, отправляет случайное фото из папки

## Как пользоваться **`get_photos_of_space_bot.py`**

+ Получите API-токен с помошью - [*Отец ботов*](https://telegram.me/BotFather), создав бот.
+ Создаем телеграм канал, получаем `chat_id` и делаем нашего бота администратором
  >Ключ и chat_id помещаем в **.env** файл
  >используем `load_dotenv` и `os`
  ```python
  load_dotenv()
  token = os.environ["TELEGRAM_TOKEN"]
  chat_id = os.environ["TG_CHAT_ID"]
  ```
+ При запуске программы необходимо ввести тайминг - количество часов между публикацией фотографий.
  >По умолчанию установлен тайминг - **4 часа**.
  ```python
  DEFAULT_TIMING = 4
  ```
  

### Пример использования **`get_photos_of_space_bot.py`**

1. Запускаем программу в командной строке:
   >C:\......>python get_photos_of_space_bot.py
   *Результат: бот отправляет в группу фото раз в `4 часа` по порядку из папки `**images**`. Когда фото заканчиваются, порядок перемешивается случайным образом и отправляется в бесконечном цикле.
2.  Запускаем программу в командной строке указывая количество часов:
   >C:\......>python get_photos_of_space_bot.py 2
   *Результат: бот отправляет в группу фото раз в `2 часа` по порядку из папки `**images**`. Когда фото заканчиваются, порядок перемешивается случайным образом и отправляется в бесконечном цикле.

## Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков dvmn.org.
