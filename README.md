# Космический Инстаграм

Проект для публикации фотографий в [Инстраграм](https://instagram.com) с запусками ракет [SpaceX](https://www.spacex.com/) и/или снимков сделаные телескопом [Habble](https://hubblesite.org/).
### Как установить

Python3 должен быть уже установлен. Затем используйте pip (или pip3, есть есть конфликт с Python2) для установки зависимостей:

```python
pip install -r requirements.txt
```
### Как запустить

В корне проекта создайте файл `.env` с данными (логин м пароль) для авторизации в Инстаграм:

```
LOGIN=ЛОГИН
PASSWORD=ПАРОЛЬ
```
В терминале запустите скрипт с параметрами:

```python
python main.py [-dir images] [-space] [-hab] [-col wallpaper]
```

Где:
* __dir__ - параметр с именем директории для фотографий проекта (по умолчанию будет создана папка "images")
* __space__ - брать фотографии с запусками ракет SpaceX
* __hab__ - брать фотографии сделаные телескопом Habble
* __col__ - параметр с именем коллекции фотографий телескопа Habble (по умолчанию фотографии будут браться из коллекции "spacecraft"). На момент написания проекта, у телескопа Habble имеется шесть коллекций, откуда можно брать фотографии: "holiday_cards, wallpaper, spacecraft, news, printshop, stsci_gallery"
### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org).