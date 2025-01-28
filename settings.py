import os

from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("token_bot")
FILE_STATISTICS_NAME = os.getenv("file_statistic")
