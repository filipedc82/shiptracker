from bs4 import BeautifulSoup
from datetime import datetime
import requests
import csv

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '\
           'AppleWebKit/537.36 (KHTML, like Gecko) '\
           'Chrome/75.0.3770.80 Safari/537.36'}

ships = []
with open('shiplist.txt', 'r') as shiplist:
    for line in shiplist:
        # print(line, end="")
        ships.append(line)

# print(ships)
# print("\n")
for ship in ships:
    ship_imo = ship.split(',')[0].strip()
    ship_final_destination = ship.split(',')[1].strip()
    ship_url = ship.split(',')[2].strip()
    ship_name = ship.split(',')[3].strip()

    print(ship_imo)
    print(ship_final_destination)

    source_html = requests.get(ship_url, headers=headers).text
    # print(source_html)


    soup = BeautifulSoup(source_html, 'html.parser')

    destination_port = soup.find('div', class_='vi__r1 vi__sbt').a.contents[0]
    destination_eta_text = soup.find('span', class_='_mcol12').text.split(':')[1].split(',')[0].strip()
    status = soup.find('table', class_='aparams').find_all("td")[5].contents[0] #get the 6th td entry and extract the contents
    print(status)
    print(destination_port)
    print(destination_eta_text)
    destination_eta = datetime.strptime(destination_eta_text + " " + str(datetime.now().year), '%b %d %Y')
    print(destination_eta)
    print("\n")
    # dataset[0] = str(datetime.now()) + "," + destination_port + "," + destination_eta_text


    with open('trackingdata.csv','a', newline="") as datafile:

        rowdata = (str(datetime.now()), ship_imo, ship_final_destination, ship_name, destination_port, destination_eta_text)
        csv_writer = csv.writer(datafile)
        csv_writer.writerow(rowdata)
        # csv_writer.writerow(str(datetime.now()) + "," + destination_port + "," + destination_eta_text)
        # for line in dataset:
        #     file.write(line)
        #     file.write('\n')
