from api import API
from datahandler import DataHandler
import schedule
import time
from home_assistant_api import HomeAssistantAPI
# importing the module
import logging

logging.basicConfig(filename='./logs/logs.log', level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s')
logger = logging.getLogger(__name__)


class CheckApartment:
    def __init__(self):

        self.api = API()
        self.datahandler = DataHandler()
        self.home_assistant_api = HomeAssistantAPI()

    def check_apartment(self):
        list_of_apartments = self.api.get_list_of_apartments()

        self.datahandler.handle_data(list_of_apartments)

    def run(self):
        # check if it works
        self.check_apartment()
        self.home_assistant_api.send_start_message()

        schedule.every().day.at("11:30").do(self.check_apartment)

        while True:
            schedule.run_pending()
            time.sleep(1)


if __name__ == '__main__':
    apartment = CheckApartment()

    try:
        apartment.run()
    except Exception as Argument:
        logging.exception("Error occurred while running the script")
