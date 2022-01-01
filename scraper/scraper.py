import json
import requests
from django.core.exceptions import ValidationError
from scraper.models import RSSPage
from typing import TypedDict

#create live scraper FT?!?!?

#scraper gets list of websites to scrape from - passed on init?? Json? DB? YAML?

#scraper iterates over those websites
    #scraper gets and save raw html page

WebsiteParameters = TypedDict(
    'WebsiteParameters', 
    {'name': str, 'url': str}
)

class Scraper:
    
    def scrape_all() -> None:
        with open('scraper/static/websites_to_scrape.json') as file:
            data = json.load(file)
        website_list = data['websites']
        for website in website_list:
            Scraper.scrape_rss_page(website)

    
    def scrape_rss_page(website_params: WebsiteParameters) -> None:
        #needs headers
        url, website_name = website_params['url'], website_params['name']
        page = requests.get(website_params['url'])
        Scraper.save_rss_page(page, url, website_name)


    def save_rss_page(html: str, url: str, website_name: str) -> None:
        rss_page = RSSPage(html=html, url=url, website_name=website_name)
        try:
            rss_page.full_clean()
            rss_page.save()
        except ValidationError as error:
            print(error)