from config.settings import DATABASES
from utils.my_sql_manager.manager import MySqlManager


mysql = MySqlManager(**DATABASES['default']['OPTIONS']['read_default_file'])
from applications.db_upload.db_upload import DbUpload

files_directory = "./data_frame_files/"
DbUpload.file_read(files_directory)
