import requests
from config import hass_access_token


class HomeAssistantAPI:
    def __init__(self):
        self.access_token = hass_access_token
        self.HASS_URL = "http://server.local:8123/api/services/notify/notify"

        self.message_apartment_found = lambda url: {
            "message": "Apartment found",
            "title": "Apartment finder",
            "data": {
                "url": url,
            }
        }

        self.start_message = {
            "message": "Script has started",
            "title": "Apartment finder",
        }

        self.hass_headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json",
        }

    def send_start_message(self):
        requests.post(self.HASS_URL, headers=self.hass_headers, json=self.start_message)

    def send_notification(self, apartment_url):

        response = requests.post(self.HASS_URL, headers=self.hass_headers, json=self.message_apartment_found(apartment_url))

        # print(response.text)


if __name__ == "__main__":
    hass = HomeAssistantAPI()
    hass.send_notification("https://google.com")