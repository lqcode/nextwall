import json
import random
import requests
import subprocess


API_URL = 'https://browser.yandex.ru/wallpapers/api/desktop/recent/'
API_SKIP_STEP = 50

WALLPAPERS_DIR = "/home/nikita/wallpapers/"
WALLPAPER_PROP = "/backdrop/screen0/monitorHDMI-0/workspace0/last-image"

CMD = ["xfconf-query", 
    "-c", "xfce4-desktop", 
    "--property", WALLPAPER_PROP, 
    "--set"]


def next_wallpaper():
    wall_url = get_random_wallpaper_url()
    wall_path = download_wallpaper(wall_url)

    success, sp = set_wallpaper(wall_path)
    if not success:
        print("---------------------------------")
        print("Failed to install new wallpaper!")
        print(f"URL: {wall_url}\nPath: {wall_path}\nsp: {sp}")
        print("---------------------------------")


def download_wallpaper(wall_url):
    response = requests.get(wall_url)
    path = WALLPAPERS_DIR + get_filename_by_url(wall_url)

    with open(path, "wb") as fp:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                fp.write(chunk)

    return path


def get_random_wallpaper_url():
    response = requests.get(API_URL + str(random.randint(0, 10) * API_SKIP_STEP))

    if response.status_code != 200:
        return ''

    backgrounds = json.loads(response.content)["backgrounds"]

    while (random_background := random.choice(backgrounds))["video"] is not None:
        pass

    return random_background["thumbnails"]["desktop2560"]["jpeg"]


def set_wallpaper(wall_path):
    sp = subprocess.run(CMD + [wall_path])
    return sp.returncode == 0, sp


def get_filename_by_url(url):
    return url.split('/')[-1]


if __name__ == "__main__":
    next_wallpaper()
