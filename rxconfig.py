import reflex as rx
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
config = rx.Config(
    app_name="reflex_template",
)
