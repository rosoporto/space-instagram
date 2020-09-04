import os
import logging
import argparse
from dotenv import load_dotenv
from instabot import Bot
from util import set_path, resize_and_convert
from fetch_spacex import fetch_spacex_last_launch
from fetch_hubble import get_hubble_collection
from fetch_insta import publish_in_insta


logging.basicConfig(level=logging.DEBUG)


def main():
  load_dotenv()

  parser = argparse.ArgumentParser(
    description='Описание что делает программа'
  )
  parser.add_argument('-dir', '--dir',
                       help='Имя директории для картинок',
                       default='images')
  parser.add_argument('-space', '--space',
                       action='store_true',
                       help='Фото запусков SpaceX')
  parser.add_argument('-hab', '--habble',
                       action='store_true',
                       help='Фото телескопа Habble')
  parser.add_argument('-col', '--collection',
                       help='Фото коллекции телескопа Habble',
                       default='spacecraft')
  args = parser.parse_args()
  print(args.dir, args.space, args.habble, args.collection)

  bot = Bot()
  USERNAME = os.getenv('LOGIN')
  PASSWORD = os.getenv('PASSWORD')
  bot.login(username=USERNAME, password=PASSWORD)

  images_dir = set_path(args.dir)

  if args.space:
    fetch_spacex_last_launch(images_dir)

  hubble_collections = ['holiday_cards',
                        'wallpaper',
                        'spacecraft',
                        'news',
                        'printshop',
                        'stsci_gallery']
  if args.collection in hubble_collections:     
    hubble_collection: str = args.collection

  if args.habble:
    get_hubble_collection(hubble_collection, images_dir)

  resize_and_convert(images_dir)

  publish_in_insta(bot, images_dir)


if __name__ == '__main__':
  main()
