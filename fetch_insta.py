import logging
import time
from instabot import Bot
from pathlib import Path
from util import clean_folder

def publish_in_insta(bot: Bot, images_dir: Path) -> None:
  for image_file in images_dir.iterdir():
    image_file: str = str(image_file)
    caption: str = image_file.split('\\')[-1].split('.')[0]
    bot.upload_photo(image_file, caption=caption)
    if bot.api.last_response.status_code != 200:
      logging.info(bot.api.last_response)

  time.sleep(2)
  clean_folder(images_dir)
  