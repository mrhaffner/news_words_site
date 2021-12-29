from django.core.exceptions import ValidationError
from scraper.models import RSS_Page

#scraper gets list of websites to scrape from - passed on init?? Json? DB? YAML?

#scraper iterates over those websites
    #scraper gets and save raw html page

class Scraper():
    
    def save_rss_page(html, url) -> None:
        rss_page = RSS_Page(html=html, url=url)
        try:
            rss_page.full_clean()
            rss_page.save()
        except ValidationError as error:
            print(error)