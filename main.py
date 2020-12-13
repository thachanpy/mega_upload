from mega import Mega
from dotenv import load_dotenv
import os

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
load_dotenv(dotenv_path=os.path.join(SCRIPT_DIR, ".env"))

def get_mega_credentials():
    return {
        "email": os.getenv('MEGA_EMAIL'),
        "password": os.getenv('MEGA_PASSWORD')
    }

def get_mega_folder():
    return os.getenv('MEGA_BACKUP_FOLDER')

def get_backup_folder():
    return os.getenv('BACKUP_FOLDER')

mega = Mega()

mega_credential = get_mega_credentials()

m = mega.login(
    mega_credential['email'],
    mega_credential['password']
)

folder = m.find(get_mega_folder())
if folder is None:
    m.create_folder(get_mega_folder())
    folder = m.find(get_mega_folder())

for file in os.scandir(get_backup_folder()):
    if os.path.isfile(file.path) and file.name.endswith('.tar'):
        m.upload(file.path, folder[0])
