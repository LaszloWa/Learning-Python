import requests
import bs4
import collections


WeatherReport = collections.namedtuple("WeatherReport", "loc, temp, scale, cond")


def main():
    print_header()
    user_input = input("For what zip code would you like to know the current weather? ")
    html = get_html_from_web(user_input)
    report = get_info_from_html(html)
    print_weather(report)


def print_header():
    print("---------------------------")
    print("       Weather App")
    print("---------------------------")
    print()


def get_html_from_web(data):
    url = "https://www.wunderground.com/weather-forecast/{}".format(data)

    html = requests.get(url)

    return html.text


def get_info_from_html(data):
    soup = bs4.BeautifulSoup(data, "html.parser")

    # loc = id: "inner-content" h1
    # temp = id: "inner-content" "wu-value wu-value-to"
    # scale = id: "inner-content" "wu-label"
    # cond = id: "inner-content" "condition-icon small-6 medium-12 columns"

    loc = soup.find(id="inner-content").find("h1").get_text()
    temp = soup.find(id="inner-content").find(class_="wu-value wu-value-to").get_text()
    scale = soup.find(id="inner-content").find(class_="wu-label").get_text()
    cond = soup.find(id="inner-content").find(class_="condition-icon small-6 medium-12 columns").get_text()

    loc = loc_clean_up(loc)
    temp = clean_up(temp)
    scale = clean_up(scale)
    cond = clean_up(cond).lower()

    report = WeatherReport(loc=loc, temp=temp, scale=scale, cond=cond)
    return report


def print_weather(data):
    print("The weather in {} is currently {} °{} and {}.".format(
        data.loc,
        data.temp,
        data.scale,
        data.cond
    ))


def loc_clean_up(data : str):
    text = data.split("\n")
    return text[0]


def clean_up(data):
    if not data:
        return data

    text = data.strip()
    return text


if __name__ == "__main__":
    main()