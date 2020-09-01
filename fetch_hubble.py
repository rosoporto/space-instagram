import requests
from pathlib import Path
from util import take_file_extension, save_pictures


def get_hubble_image(foto_id: int, images_dir: Path) -> None:
  response: Response = requests.get('http://hubblesite.org/api/v3/image/{}'.format(foto_id))
  response.raise_for_status()
  foto_url: str = response.json()['image_files'][-1]['file_url']
  foto_url = foto_url.replace('//', 'https://')
  ext: str = take_file_extension(foto_url)
  filename: str = 'hubble{}.{}'.format(foto_id, ext)
  save_pictures(filename, foto_url, images_dir)


def get_hubble_collection(name_collection: str, images_dir: Path) -> None:
  response: Response = requests.get(f'http://hubblesite.org/api/v3/images/{name_collection}?page=all')
  response.raise_for_status()
  for foto_id in response.json():
    get_hubble_image(foto_id['id'], images_dir)
