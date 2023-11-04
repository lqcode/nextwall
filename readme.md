# nextwall.py 

nextwall - небольшой скрипт на Python, который загружает случайное изображение с `browser.yandex.ru/wallpapers` и устанавливает его как фоновое изображение **Xfce4**. 

*Python script for automatically download and install new wallpapers on Xfce4.*

## Внимание

Скрипт работает только на Xfce4. Для работы нужен `requests` (`pip install requests`).

## Установка

Закидываем `nextwall.py` в любой каталог, где он не будет мешать. 

## Настройка

### 1. WALLPAPER_PROP

В терминале вводим `xfconf-query -c xfce4-desktop -m`.

```bash
Начать следить за каналом "xfce4-desktop":

```

Меняем фоновое изображение через настройки.

В консоле появится нужноe свойство:

```bash
Начать следить за каналом "xfce4-desktop":

установить: /backdrop/screen0/monitorHDMI-0/workspace/last-image
```

Меняем значение константы **WALLPAPER_PROP** на `/backdrop/screen0/monitorHDMI-0/workspace/last-image`  
*(В вашем случае путь может отличаться)*

### 2. WALLPAPERS_DIR

**WALLPAPERS_DIR** - каталог, в который будут скачиваться изображения. Меняем на любой удобный.

*Если вы всё сделали правильно, то после запуска скрипта (`python3 nextwall.py`), ваше фоновое изображение будет изменено на случайное, а в указаном каталоге появится новое изображение.* 

### 3. Cron

Конечно, быстро надоест запускать скрипт вручную, чтобы увидеть новое изображение на рабочем столе, поэтому мы используем Cron для автоматизации.

В терминале вводим `echo $DBUS_SESSION_BUS_ADDRESS`. Получим примерно такой путь `unix:path=/run/user/1000/bus` - запоминаем или копируем.

Вводим `crontab -e`. Добавляем в конец файла строчку:

```bash
*/10 * * * * env DBUS_SESSION_BUS_ADDRESS=***ПУТЬ КОТОРЫЙ МЫ ПОЛУЧИЛИ ВЫШЕ*** /usr/bin/python3 /полный/путь/до/nextwall.py

 // в моём случае получилось
*/10 * * * * env DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/1000/bus /usr/bin/python3 /home/nikita/workspace/nextwall/nextwall.py
```

Сохраняем. Теперь каждые десять минут у нас должно меняться фоновое изображение.



