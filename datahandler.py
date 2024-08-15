from config import max_hyra, min_yta
from home_assistant_api import HomeAssistantAPI

class DataHandler:
    def __init__(self):
        self.ha = HomeAssistantAPI()

    def handle_data(self, list):
        for apartment in list:
            hyra = apartment['hyra']
            typ = apartment['typ']
            yta = apartment['yta']

            vaning = apartment['vaning']

            self.__check_apartment(hyra, typ, yta)

    def __check_apartment(self, hyra, typ, yta):

        if int(hyra) <= max_hyra:
            if int(yta) >= min_yta:
                pass

