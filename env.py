import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

discord_webhook_url = os.environ.get("DISCORD_WEBHOOK_URL")
debug = os.environ.get("DEBUG")