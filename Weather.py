from bs4 import BeautifulSoup
from urllib.request import urlopen  # This saves on typing later on
from urllib.request import Request  # extended to a second line for better explanation
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.keys import Keys


"""Create a current Weather class that gets the current weather"""
class currentWeather:
    def openCurrentWebsite(self,url):
        """ Open The Weather Channel website using urllib"""
          # state the base url on it's own to make it easier to access in more elaborate scripts
        user_agent = 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_4; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.472.63 Safari/534.3'

        headers = {'User-Agent': user_agent}

        weatherFile = Request(url, None, headers)  # Requests the URL with the header so it looks like a browser

        weatherFile = urlopen(weatherFile)

        soup = BeautifulSoup(weatherFile, "html.parser")

        return soup

    def findTemp(self,url):
        """Gets the current temperature"""
        # finds the temperature class line with the temperature in it
        temperatureText = url.find('p', {'class': 'myforecast-current-lrg'}).text
        # returns just the temperature
        return temperatureText

    def conditions(self,url):
        """Gets the current conditions"""
        # finds the sky conditions class line with the conditions in it

        conditionsText = url.find('p', {'class': 'myforecast-current'}).text

        # returns the sky conditions
        return conditionsText
def getWebsiteUrl(area):
    """find the url with the weather of where the user is"""

    options = Options()
    options.set_headless(headless=True)
    #add a path to the chromedriver so the program can open up chrome
    driver = webdriver.Chrome(options=options, executable_path=r'/path/to/chromedriver')
    driver.get('https://www.weather.gov/')


    driver.get('https://www.weather.gov/')
    location = driver.find_element_by_id('inputstring')

    location.clear()
    location.click()

    location.send_keys(area)

    #click the go button to get to the next page
    go = driver.find_element_by_id('btnSearch')
    time.sleep(2)
    go.click()
    time.sleep(2)

    url = driver.current_url
    driver.quit

    return url


def printCurrentWeather(current,url):
    """Print today's weather"""

    #print the current temperature
    print('The current temperature is ' + current.findTemp(url))

    #print the current weather conditions
    print('The current weather conditions is ' + current.conditions(url))

#ask user for area
area = input('What Area would you like to know the weather of?')

#get the url of the website
getUrl = getWebsiteUrl(area)

#create todayWeather object
current = currentWeather()

#get current weather url
url = current.openCurrentWebsite(getUrl)

printCurrentWeather(current,url)
