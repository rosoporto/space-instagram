import requests
from pathlib import Path
from util import get_file_extension, save_pictures


def get_hubble_image(foto_id: int, images_dir: Path) -> None:
  response: Response = requests.get('http://hubblesite.org/api/v3/image/{}'.format(foto_id))
  response.raise_for_status()
  picture_link: str = response.json()['image_files'][-1]['file_url']
  picture_link = picture_link.replace('//', 'https://')
  ext: str = get_file_extension(picture_link)
  filename: str = 'hubble{}.{}'.format(foto_id, ext)
  save_pictures(filename, picture_link, images_dir)


def get_hubble_collection(name_collection: str, images_dir: Path) -> None:
  params = {'page':'all'}
  response: Response = requests.get(
    f'http://hubblesite.org/api/v3/images/{name_collection}',
    params=params)
  response.raise_for_status()
  for image in response.json():
    get_hubble_image(image['id'], images_dir)
