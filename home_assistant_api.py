from config import ha_api_key


class HomeAssistantAPI:
    def __init__(self, hass):
        self.api_key = ha_api_key
        self.HA_URL = "http://<home_assistant_ip>:8123/api/services/notify/mobile_app_phone1"

    def home_assistant(self):
        pass
