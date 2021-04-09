import requests
from bs4 import BeautifulSoup
import sys
import csv

def Max_Numbers():
    URL = 'http://www.bom.gov.au/act/forecasts/canberra.shtml'
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')

    results = soup.find_all("em", class_='max')
    results_string = str(results)
    return results_string

print(Max_Numbers())

with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["temp", "date", "weather"])
    writer.writerow([Max_Numbers()[17:19], "Friday", "Partly Cloudy"])
    writer.writerow([Max_Numbers()[42:44], "Saturday"])
    writer.writerow([Max_Numbers()[67:69], "Saturday"])
    writer.writerow([Max_Numbers()[92:94], "Saturday"])
    writer.writerow([Max_Numbers()[117:119], "Saturday"])
    writer.writerow([Max_Numbers()[142:144], "Saturday"])
    writer.writerow([Max_Numbers()[167:169], "Saturday"])
    