from django.core.exceptions import ValidationError
from scraper.models import RSSPage

#create live scraper FT?!?!?

#scraper gets list of websites to scrape from - passed on init?? Json? DB? YAML?

#scraper iterates over those websites
    #scraper gets and save raw html page

class Scraper():
    
    def save_rss_page(html: str, url: str, website_name: str) -> None:
        rss_page = RSSPage(html=html, url=url, website_name=website_name)
        try:
            rss_page.full_clean()
            rss_page.save()
        except ValidationError as error:
            print(error)