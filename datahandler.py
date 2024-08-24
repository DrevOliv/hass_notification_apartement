from config import max_hyra, min_yta
from home_assistant_api import HomeAssistantAPI
from api import API
import logging


class DataHandler:
    def __init__(self):
        self.ha = HomeAssistantAPI()

    def __log_yellow(self, *args, **kwargs):
        logging.warning("".join(map(str,args)))

    def __log_green(self, *args, **kwargs):
        logging.debug(" ".join(map(str,args)))

    def handle_data(self, list):
        for apartment in list:
            hyra = apartment['hyra']
            typ = apartment['typ']
            yta = apartment['yta']
            detaljUrl = apartment["detaljUrl"]

            vaning = apartment['vaning']

            hyra = ''.join(char for char in hyra if char.isalnum())

            self.__check_apartment(hyra, typ, yta, detaljUrl)

    def __check_apartment(self, hyra, typ, yta, detaljUrl):

        self.__log_yellow("Hyra: ", hyra, ", typ:", typ, ", yta:", yta)

        if int(hyra) <= max_hyra:
            if yta >= min_yta:
                self.__log_green("Hitta lägenhet:", " Hyra: ", hyra, ", typ:", typ, ", yta:", yta, ", detaljUrl:", f"https://www.studentbostader.se{detaljUrl}")
                self.ha.send_notification(f"https://www.studentbostader.se{detaljUrl}")


if __name__ == "__main__":
    import urllib3

    urllib3.disable_warnings()

    logging.basicConfig(filename='./logs/logs.log', level=logging.DEBUG,
                        format='%(asctime)s %(levelname)s %(message)s')
    logger = logging.getLogger(__name__)

    api = API()

    dataHandler = DataHandler()

    dataHandler.handle_data(api.get_list_of_apartments())

