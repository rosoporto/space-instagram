import requests
from pathlib import Path
from PIL import Image


def take_file_extension(url: str) -> str:
  return url.split('.')[-1]


def path_image_folder(images_dir: str) -> Path:
  Path(images_dir).mkdir(parents=True, exist_ok=True)
  return Path(Path.cwd()).joinpath(images_dir)


def save_pictures(filename: str, url: str, images_dir: Path) -> None:
  response: Response = requests.get(url, verify=False)
  response.raise_for_status()
  with open(Path(Path.cwd()).joinpath(images_dir, filename), 'wb') as file:
    file.write(response.content) 


def clean_folder(images_dir: Path, file_format: str ='jpg') -> None:
  '''Удалить в директории все файлы 'all' или только с расширением *.jpg'''  
  for image_file in images_dir.glob('**/*'):
    if file_format == 'jpg':
      if not str(image_file).endswith(file_format):
        image_file.unlink()
    elif file_format == 'all':
      image_file.unlink()


def resize_and_convert(images_dir: Path) -> None:
  for image_file in images_dir.iterdir():
    image: Image = Image.open(image_file.absolute().__str__())
		
    if image.mode != 'RGB':
      image = image.convert('RGB')

    if image.width > image.height:
      cropped_left = cropped_right = (image.width - image.height) / 2
      coordinates: tuple = (cropped_left, 0, image.width - cropped_right, image.height)
    else:
      cropped_up = cropped_down = (image.height - image.width) / 2
      coordinates: tuple = (0, cropped_up, image.width, image.height - cropped_down)
			
    cropped = image.crop(coordinates)
		
    new_name_image: str = image_file.absolute().__str__().split('\\')[-1].split('.')[0] + '.jpg'
    new_name_image = Path(Path.cwd()).joinpath(images_dir, new_name_image)    
		
    cropped.save(new_name_image, format('JPEG'))

  clean_folder(images_dir)
  