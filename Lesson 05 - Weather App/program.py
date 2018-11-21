import requests
import bs4
import collections


WeatherReport = collections.namedtuple("WeatherReport", "loc, temp, unit, cond")


def main():
    print_header()
    zip_code = input("For what zip-code would you like the weather forecast? ")

    html = get_html_from_web(zip_code)
    report = get_weather_from_html(html)
    print_weather(report)


def print_header():
    print("---------------------------------")
    print("          Weather App")
    print("---------------------------------")
    print()


def get_html_from_web(zip_code):
    url = "https://www.wunderground.com/weather-forecast/{}".format(zip_code)

    response = requests.get(url)

    return response.text


def get_weather_from_html(html):
    # cityCSS = ".region-content-header h1"
    # weatherScaleCSS = ".wu-unit-temperature .wu-label"
    # weatherTemCSS = ".wu-unit-temperature .wu-value"
    # weatherConditionCSS = ".condition-icon"

    soup = bs4.BeautifulSoup(html, "html.parser")
    loc = soup.find(id="inner-content").find("h1").get_text()
    temp = soup.find(id="inner-content").find(class_="wu-value wu-value-to").get_text()
    unit = soup.find(id="inner-content").find(class_="wu-label").get_text()
    condition = soup.find(id="inner-content").find(class_="condition-icon small-6 medium-12 columns").get_text()

    loc = clean_up(loc)
    loc = loc_clean_up(loc)
    temp = clean_up(temp)
    unit = clean_up(unit)
    condition = clean_up(condition.lower())


    report = WeatherReport(loc=loc, temp=temp, unit=unit, cond=condition)
    return report


def print_weather(report):
    print("The weather in {} is {}°{} and {}.".format(
        report.loc,
        report.temp,
        report.unit,
        report.cond
    ))

def loc_clean_up(text : str):
    parts = text.split("\n")
    return parts[0].strip()


def clean_up(text):
    if not text:
        return text

    text = text.strip()
    return text


main()