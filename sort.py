import argparse
import shutil
from pathlib import Path
from Home_Work_6.normalize import normalize

parser = argparse.ArgumentParser(description="Sorting folder")
parser.add_argument("--source", "-s", required=True, help="Source folder")
args = vars(parser.parse_args())
source = args.get("source")

file_type = {
    'audio': ('mp3', 'ogg', 'wav', 'amr'),
    'video': ('avi', 'mp4', 'MOV', 'mkv'),
    'images': ('jpeg', 'png', 'jpg', 'svg'),
    'archives': ('zip', 'gz', 'tar'),
    'documents': ('doc', 'docx', 'txt', 'pdf', 'xlsx', 'pptx')
}

folders = []
audio = []
video = []
images = []
archives = []
documents = []
extension = []
other_extension = []


def read_folder(path: Path):
    for el in path.iterdir():
        if el.is_dir():
            if el.name not in file_type.keys() or 'other_files':
                folders.append(el)
                read_folder(el)
        else:
            replace_file(el)


def replace_file(file: Path):
    ext = file.suffix[1:]
    if ext in file_type.get('audio'):
        new_path = output_folder / 'audio'
        new_path.mkdir(exist_ok=True, parents=True)
        file.replace(new_path / normalize(file.name))
        audio.append(normalize(file.name))
        if file.suffix not in extension:
            extension.append(file.suffix)
    elif ext in file_type.get('video'):
        new_path = output_folder / 'video'
        new_path.mkdir(exist_ok=True, parents=True)
        file.replace(new_path / normalize(file.name))
        video.append(normalize(file.name))
        if file.suffix not in extension:
            extension.append(file.suffix)
    elif ext in file_type.get('images'):
        new_path = output_folder / 'images'
        new_path.mkdir(exist_ok=True, parents=True)
        file.replace(new_path / normalize(file.name))
        images.append(normalize(file.name))
        if file.suffix not in extension:
            extension.append(file.suffix)
    elif ext in file_type.get('documents'):
        new_path = output_folder / 'documents'
        new_path.mkdir(exist_ok=True, parents=True)
        file.replace(new_path / normalize(file.name))
        documents.append(normalize(file.name))
        if file.suffix not in extension:
            extension.append(file.suffix)
    elif ext in file_type.get('archives'):
        new_path = output_folder / 'archives'
        archives.append(normalize(file.name))
        if file.suffix not in extension:
            extension.append(file.suffix)
        new_path.mkdir(exist_ok=True, parents=True)
        folder_for_file = output_folder / 'archives' / \
            normalize(file.name.replace(file.suffix, ''))
        folder_for_file.mkdir(exist_ok=True, parents=True)
        try:
            shutil.unpack_archive(str(file.resolve()),
                                  str(folder_for_file.resolve()))
        except shutil.ReadError:
            print(f'Це не архів {file}!')
            folder_for_file.rmdir()
            return None
        file.unlink()
    elif ext not in file_type.values():
        new_path = output_folder / 'other_files'
        new_path.mkdir(exist_ok=True, parents=True)
        file.replace(new_path / normalize(file.name))
        if file.suffix not in other_extension:
            other_extension.append(file.suffix)


def delete_folder(folder: Path):
    try:
        folder.rmdir()
    except OSError:
        print(f'Помилка видалення папки {folder}')


sort_folder = Path(source)
output_folder = sort_folder
read_folder(Path(source))

print(f'Сортуємо папку: {sort_folder}')

for folder in folders[::-1]:
    delete_folder(folder)

print(f'Аудіо файли: {audio}')
print(f'Відео файли: {video}')
print(f'Зображення: {images}')
print(f'Документи: {documents}')
print(f'Архіви: {archives}')
print(f'Розширення файлів: {extension}')
print(f'Невідомі розширення файлів: {other_extension}')

print(f'Сортування папки: {sort_folder} завершено!')
