import csv
from datetime import datetime
import requests
from bs4 import BeautifulSoup

def get_url(position, location):
    """ Generate a url frm position and location"""
    template = 'https://www.simplyhired.co.in/search?q={}&l={}'
    url = template.format(position, location)
    return url

def get_record(card):
    atag = card.h3.a

    job_title = card.find('h3','jobposting-title').text
    job_url = 'https://www.simplyhiered.co.in' + atag.get('href')

    company = card.find('span', 'JobPosting-labelWithIcon jobposting-company').text
    location = card.find('span', 'JobPosting-labelWithIcon jobposting-location').text
    summary = card.find('div', 'SerpJob-snippetContainer').text
    date = card.find('span' , 'SerpJob-timestamp').text
    today = datetime.today().strftime('%d-%m-%Y')

    record=(job_title, company, location, summary, date, today, job_url)
    return (record)

def main(position, location):
    records = []
    url = get_url(position, location)


    while True:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        cards = soup.find_all('div', 'SerpJob-jobCard card')


        for card in cards:
            record = get_record(card)
            records.append(record)

        try:
            url = 'https://www.simplyhired.co.in' + soup.find('a', {'aria-label': 'Next page'}).get('href')
        except AttributeError:
            break

    with open('results.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['JobTitle', 'Company', 'Location', 'Summary', 'PstDate', 'ExtarctDate', 'JobUrl'])
        writer.writerows(records)

role = input("Enter the role you want: ")
place = input("Enter the place where you are looking for your job:")
main(role, place)



