from config import max_hyra, min_yta
from home_assistant_api import HomeAssistantAPI
from api import API


class DataHandler:
    def __init__(self):
        self.ha = HomeAssistantAPI()

    def handle_data(self, list):
        for apartment in list:
            hyra = apartment['hyra']
            typ = apartment['typ']
            yta = apartment['yta']
            detaljUrl = apartment["detaljUrl"]

            vaning = apartment['vaning']

            # hyra = hyra.replace(' ', '_')
            hyra = hyra.replace(" ", '_')

            self.__check_apartment(hyra, typ, yta, detaljUrl)

    def __check_apartment(self, hyra, typ, yta, detaljUrl):

        if int(hyra) <= max_hyra:
            if yta >= min_yta:

                self.ha.send_notification(f"https://www.studentbostader.se{detaljUrl}")


if __name__ == "__main__":
    api = API()

    dataHandler = DataHandler()

    dataHandler.handle_data(api.get_list_of_apartments())

