from bs4 import BeatfulSoap

import requests

site = requests.get("source").content

soup = BeatfulSoap(site, 'html.parser')

print(soup.prettify())