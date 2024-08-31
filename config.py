import dotenv
import os

dotenv.load_dotenv(dotenv.find_dotenv())

max_hyra = 5000  # kr/månad

min_yta = 25  # m^2

hass_access_token = os.getenv("hass_access_token")

homeassistant_url = "http://homeassistant.house:8123"