from chai_py import ChaiBot, Update, TRoom

from bs4 import BeautifulSoup
import requests


# class Bot(ChaiBot):
#     def setup(self):
#         self.logger.info("Setting up...")

#     async def on_message(self, update: Update) -> str:
#         return "I love AI." 


class Bot(ChaiBot):

    def setup(self):
        self.logger.info("Setting up...")
        self.logger.info("This bot will give you country wise-detail of the current status of COVID")
        name = input('Enter the name of the country you want to know about. ') 
        self.Name = name


    async def on_message(self, update: Update) -> str:
        country = self.Name
        Total_count = [] #index 0 for total cases, 1 for total deaths and 2 for total recovered

        html_text = requests.get(f"https://www.worldometers.info/coronavirus/country/{country}/").text
        soup = BeautifulSoup(html_text, 'lxml')

        total_count = soup.find_all('div', class_ = 'maincounter-number')
        for total in total_count:
            Total_count.append((total.text.replace("\n",'').replace(" ",'')))
        
        message_text = update.latest_message.text
        
        if message_text == 'deaths' or message_text == 'Deaths':
            return f"Deaths : {Total_count[1]}"

        elif message_text == 'total cases' or message_text == 'Total Cases' or message_text == 'cases':
            return f"Deaths : {Total_count[0]}"

        elif message_text == 'Recovered' or message_text == 'recovered':
            return f"Deaths : {Total_count[2]}" 

        else:
            return "Unrecognised input, try again!"


