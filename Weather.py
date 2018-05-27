from bs4 import BeautifulSoup
from urllib.request import urlopen  # This saves on typing later on
from urllib.request import Request  # extended to a second line for better explanation

"""Create a current Weather class that gets the current weather"""
class currentWeather:
    def openCurrentWebsite(self):
        """ Open The Weather Channel website using urllib"""
        getUrl = "https://weather.com/weather/today/l/USNY0996:1:US"  # state the base url on it's own to make it easier to access in more elaborate scripts
        user_agent = 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_4; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.472.63 Safari/534.3'

        headers = {'User-Agent': user_agent}

        weatherFile = Request(getUrl, None, headers)  # Requests the URL with the header so it looks like a browser

        weatherFile = urlopen(weatherFile)

        soup = BeautifulSoup(weatherFile, "html.parser")

        return soup

    def findTemp(self,url):
        """Gets the current temperature"""
        # finds the temperature class line with the temperature in it
        temperatureText = url.find('div', {'class': 'today_nowcard-temp'}).text

        # returns just the temperature
        return temperatureText

    def conditions(self,url):
        """Gets the current conditions"""
        # finds the sky conditions class line with the conditions in it

        conditionsText = url.find('div', {'class': 'today_nowcard-phrase'}).text

        # returns the sky conditions
        return conditionsText


def printCurrentWeather(current,url):
    """Print today's weather"""

    #print the current temperature
    print('The current temperature is ' + current.findTemp(url))

    #print the current weather conditions
    print('The current weather conditions are ' + current.conditions(url))


#create todayWeather object
current = currentWeather()

#get current weather url
url = current.openCurrentWebsite()

printCurrentWeather(current,url)


