from api import API
from datahandler import DataHandler
import schedule
import time
from home_assistant_api import HomeAssistantAPI


class CheckApartment:
    def __init__(self):

        self.api = API()
        self.datahandler = DataHandler()
        self.home_assistant_api = HomeAssistantAPI()

    def check_apartment(self):
        list_of_apartments = self.api.get_list_of_apartments()

        self.datahandler.handle_data(list_of_apartments)

    def run(self):
        schedule.every().day.at("11:30").do(self.check_apartment)


        while True:
            schedule.run_pending()
            time.sleep(1)


if __name__ == '__main__':
    apartment = CheckApartment()

    apartment.run()