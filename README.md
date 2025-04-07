# Фотографии космоса в Telegram-канале.

Скрипты позволяют загружать фотографии **NASA** и **SpaseX**, а также публиковать в **Telegram**-канале при помощи бота.
1. [**`fetch_nasa_apod_images.py`**](fetch_nasa_apod_images.py) - *Astronomy Picture of the Day* Получаем фотографии дня в космической тематике.
2. [**`fetch_nasa_epic_images.py`**](fetch_nasa_epic_images.py) - *Earth Polychromatic Imaging Camera* Получаем полихроматические фото земли крайней даты.
3. [**`fetch_spacex_images.py`**](fetch_spacex_images.py) - Загружаем фотографии запуска **SpaseX**
4. [**`publish_one_photo_of_space_bot.py`**](publish_one_photo_of_space_bot.py) - Бот отправляет фото выбранное по названию. Если не нашел, отправляет случайное фото из папки.
5. [**`publish_photos_of_space_bot.py`**](publish_photos_of_space_bot.py) - Бот отправляет все фото из папки по порядку в бесконечном цикле по таймингу.
6. [**`utils_functions.py`**](utils_functions.py) - Набор служебных функций, испозьзуемых скриптами.

## Как установить 

+ Python3 должен быть уже установлен. Затем используйте pip (или pip3, есть конфликт с Python2) для установки зависимостей:
  ```
  pip install -r requirements.txt
  ```
+ Для корректной работы `python-telegram-bot` в версии `13.2` используем python в версии не более 3.10
  ```
  pip install python-telegram-bot==13.2
  ```

## Как пользоваться **`fetch_nasa_apod_images.py`**

+ Получите API-ключ по ссылке - [*Generate API Key*](https://api.nasa.gov/) после несложной регистрации
  >Ключ помещаем в **.env** файл  
  >используем:
  ```python
  import os
  from dotenv import load_dotenv
  load_dotenv()
  token = os.environ["NASA_API_KEY"]
  ```
+ в разделе [NASA-APOD](https://api.nasa.gov/#apod) получаем необходимы данные. В данном случае:
  >`GET https://api.nasa.gov/planetary/apod` - базовая ссылка для **HTTP-запроса** к которой применяются параметры.
  >`Query Parameters` - таблица с параметрами.
  >Программа по умолчанию скачивает 10 случайно выбранных фото. Пользователь может ввести нужно количество фото

### Пример использования **`fetch_nasa_apod_images.py`**

1. Запускаем программу в командной строке:
   ```
   python fetch_nasa_apod_images.py
   ```
   >Результат: в директории проекта создается папка **`images`** и в ней сохранятся по молчанию 10 фото дня.
3. Запускаем программу в командной строке указывая количество скачиваемых фото:
   ```
   python fetch_nasa_apod_images.py 2025-02-25
   ```
   >Результат: в директории проекта создается папка **`images`** и в ней сохранятся указанное количество фото дня.

## Как пользоваться **`fetch_nasa_epic_images.py`**

+ Получите API-ключ по ссылке - [*Generate API Key*](https://api.nasa.gov/) после несложной регистрации
  >Ключ помещаем в **.env** файл  
  >используем:
  ```python
  import os
  from dotenv import load_dotenv
  load_dotenv()
  token = os.environ["NASA_API_KEY"]
  ```
+ в разделе [NASA-EPIC](https://api.nasa.gov/#epic) получаем необходимы данные. В данном случае:
  >`https://api.nasa.gov/EPIC/api/natural` - базовая ссылка для **HTTP-запроса** к которой применяются параметры.
  >`Querying by Date(s)` - таблица с параметрами.
  >`https://api.nasa.gov/EPIC/archive/natural` - архив откуда получаем фото, используя `id` и `date` и предыдущик пунктов

### Пример использования **`fetch_nasa_epic_images.py`**

1. Запускаем программу в командной строке:
   ```
   python fetch_nasa_epic_images.py
   ```
   >Результат: в директории проекта создается папка **`images`** и в ней сохранятся последние фотографии из раздела **EPIC**.

## Как пользоваться **`fetch_spacex_images.py`**

+ API-ключ в данном сервисе не нужен. 
+ в репозитарии [SpaceX REST API](https://github.com/r-spacex/SpaceX-API) получаем необходимы данные. В данном случае:
  >`https://api.spacexdata.com/v5/launches/latest` - ссылка для **HTTP-запроса** последнего запуска.
  >`https://api.spacexdata.com/v5/launches` - все запуски. используя `id` можно получить фото при их наличии.

### Пример использования **`fetch_spacex_images.py`**

1. Запускаем программу в командной строке:
   ```
   python fetch_spacex_images.py
   ```
   >Результат: в директории проекта создается папка **`images`** и в ней, ___если таковые имеются___, сохранятся фотографии последнего запуска **SpaseX**.
2. Запускаем программу в командной строке, указывая `id` запуска:
   ```
   python fetch_spacex_images.py 5eb87d42ffd86e000604b384
   ```
   >Результат: в директории проекта создается папка **`images`** и в ней, ___если таковые имеются___, сохранятся фотографии конкретного запуска **SpaseX**.

## Как пользоваться **`publish_one_photo_of_space_bot.py`**

+ Получите API-токен с помошью - [*Отец ботов*](https://telegram.me/BotFather), создав бот.
+ Создаем телеграм канал, получаем `chat_id` и делаем нашего бота администратором
  >Ключ помещаем в **.env** файл  
  >используем:
  ```python
  import os
  from dotenv import load_dotenv
  load_dotenv()
  token = os.environ["NASA_API_KEY"]
  ```

### Пример использования **`publish_one_photo_of_space_bot.py`**

1. Запускаем программу в командной строке указав название фото:
   ```
   python publish_one_photo_of_space_bot.py nasa_epic_13.png
   ```
   >Результат: бот отправляет в группу фото с соответствующим названием из папки **`images`**. Если по имени фото не найдено, отправляет случайное фото из папки

## Как пользоваться **`publish_photos_of_space_bot.py`**

+ Получите API-токен с помошью - [*Отец ботов*](https://telegram.me/BotFather), создав бот.
+ Создаем телеграм канал, получаем `chat_id` и делаем нашего бота администратором
  >Ключ помещаем в **.env** файл  
  >используем:
  ```python
  import os
  from dotenv import load_dotenv
  load_dotenv()
  token = os.environ["NASA_API_KEY"]
  ```
+ При запуске программы необходимо ввести тайминг - количество часов между публикацией фотографий.
  >По умолчанию установлен тайминг - **4 часа**.
    
### Пример использования **`publish_photos_of_space_bot.py`**

1. Запускаем программу в командной строке:
   ```
   python publish_photos_of_space_bot.py
   ```
   >Результат: бот отправляет в группу фото раз в `4 часа` по порядку из папки **`images`**. Когда фото заканчиваются, порядок перемешивается случайным образом и отправляется в бесконечном цикле.
2.  Запускаем программу в командной строке указывая количество часов:
    ```
    python publish_photos_of_space_bot.py 2
    ```
   >Результат: бот отправляет в группу фото раз в `2 часа` по порядку из папки **`images`**. Когда фото заканчиваются, порядок перемешивается случайным образом и отправляется в бесконечном цикле.

## Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков dvmn.org.
