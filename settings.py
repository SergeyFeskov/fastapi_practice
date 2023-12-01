from envparse import Env
from dotenv import load_dotenv

load_dotenv(".env")

env = Env()

DATABASE_URL = env("DATABASE_URL")
