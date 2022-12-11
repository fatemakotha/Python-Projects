from bs4 import BeautifulSoup #installed BeautifulSoup4 instead of BeautifulSoup ****
import requests
import os


GOOGLEFORM = "https://docs.google.com/forms/d/e/1FAIpQLSfjsQ5c7jFZhPVgIMNgN-crhJ5ElLbLyzf8-oveEIL-cwEamQ/viewform?usp=sf_link"
ZILLOW_FILTERED = "https://www.zillow.com/new-york-ny/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22north%22%3A40.90783632092015%2C%22east%22%3A-73.21063803125003%2C%22south%22%3A40.47780203658845%2C%22west%22%3A-74.01401327539065%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A411273%2C%22min%22%3A411273%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A2000%2C%22min%22%3A2000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22baths%22%3A%7B%22min%22%3A1%7D%2C%22apco%22%3A%7B%22value%22%3Afalse%7D%2C%22apa%22%3A%7B%22value%22%3Afalse%7D%2C%22con%22%3A%7B%22value%22%3Afalse%7D%2C%22tow%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A6181%2C%22regionType%22%3A6%7D%5D%2C%22mapZoom%22%3A11%7D"

response = requests.get(ZILLOW_FILTERED)
print(response.text)
