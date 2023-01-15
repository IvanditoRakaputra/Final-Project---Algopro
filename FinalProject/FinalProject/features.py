import os
import wikipedia
import datetime
from quote import quote
import requests

class Features():
    """
        This class contains all the features that Jake
        can do.
    """

    #search wikipedia for a topic
    def searchWithWikipedia(self, topic_to_search):
        searchResult = wikipedia.summary(topic_to_search, sentences=1)
        return searchResult
    

    def tellDate(self):
        #get current time
        now = datetime.datetime.now()

        #convert time to date, month, and year.
        date = now.strftime("%d")
        month = now.strftime("%B")
        year = now.strftime("%Y")

        #format date result
        date_result = "Today's date is " + date + " " + month + " " + year
        return date_result
    
    #search for a random quote
    def tellQuote(self):
        result = quote('family', limit=1)
        return result[0]["quote"]

    
    def getCurrentWeather(self, city):
        #send request to weather API with city name as a parameter
        api_key = "80abe25a3f6941a985281843231301"
        request_url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no"
        fetch_weather = requests.get(request_url).json()

        #get current condition from API respond
        condition = fetch_weather["current"]["condition"]["text"]
        temperature_celsius = fetch_weather["current"]["temp_c"]

        #format weather message
        final_message = f"The current temperature in {city} is, {temperature_celsius} degrees celsius. And the " \
                        f"current weather condition is, {condition}"

        return final_message

    #open notepad using windows notepad command
    def openNotepad(self):
        os.system("notepad .")