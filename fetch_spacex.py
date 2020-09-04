import requests
from pathlib import Path
from util import get_file_extension, save_pictures


def fetch_spacex_last_launch(images_dir: Path) -> None:
  response: Response = requests.get('https://api.spacexdata.com/v4/launches/latest')
  response.raise_for_status()
  images: list = response.json()['links']['flickr']['original']
  for image_number, image_url in enumerate(images):
    ext: str = get_file_extension(image_url)
    save_pictures('spacex{}.{}'.format(image_number, ext), image_url, images_dir)