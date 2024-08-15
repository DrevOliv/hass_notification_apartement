import requests
from config import hass_access_token


class HomeAssistantAPI:
    def __init__(self):
        self.access_token = hass_access_token
        self.HASS_URL = "http://server.local:8123/api/services/notify/notify"

        self.message = lambda url: {
            "message": "Hello, this is a test notification!",
            "title": "Test Notification",
            "data": {
                "url": url,
            }
        }

        self.hass_headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json",
        }

    def send_notification(self, apartment_url):

        response = requests.post(self.HASS_URL, headers=self.hass_headers, json=self.message(apartment_url))

        print(response.text)

if __name__ == "__main__":
    hass = HomeAssistantAPI()
    hass.send_notification("https://google.com")