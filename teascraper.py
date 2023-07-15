import requests
from bs4 import BeautifulSoup
import csv
# we are defining the URL Pattern here
url_pattern = "https://www.teaboard.gov.in/WEEKLYPRICES/{}"
# here we define the years for which data needs to be scraped
start_year = 2008
end_year = 2023

data = []
for year in range(start_year, end_year + 1):
    print("Scraping data for year", year)
    url = url_pattern.format(year)
    response = requests.get(url)# we send a GET request to the URL
    soup = BeautifulSoup(response.content, 'html.parser')# parsing the HTML content using BeautifulSoup
    table = soup.find("table")# finding the table containing the data
    rows = table.find_all("tr")[1:]#here we find all the rows in the table

    #to iterate over each row and extract the required data
    for row in rows:
        columns = row.find_all("td")
        week = columns[0].text.strip()
        location = columns[1].text.strip()
        average_price = columns[2].text.strip()
        data.append([week, location, average_price])

# output CSV file path
csv_file_path = "./tea_prices.csv"

# Writing the data to the CSV file
with open(csv_file_path, "w", newline="") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["week", "location", "average_price"])
    writer.writerows(data)

print("Data scraping and consolidation complete")

