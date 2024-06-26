from .content_reader import CamdenContentReader, IslingtonContentReader
from .scraper import Scraper
from .helpers import replace_url

class Categories():
    def __init__(self):
        self.main_collection_name="main_categories"
        self.subcategory_name="subcategories"
    
    def get_main_categories(self, region, from_db=False, db=None):
        if from_db:
           categories=db.get_main_regional_categories(region)   
        else: 
            category_page=Scraper().get_category_page(region)
            if region=="camden":
                categories=CamdenContentReader(category_page).get_main_categories()
            elif region=="islington":
                categories=IslingtonContentReader(category_page).get_main_categories()
        return categories

    def get_subcategories(self, request_url, region, from_db=False, db=None):
        url=replace_url(request_url)
        if from_db:
            subcategories=db.get_regional_subcategories(url, region)
        else:
            html=Scraper().scrape(url)[0]
            if region=="camden":
                subcategories=CamdenContentReader(html).get_subcategories()
            elif region=="islington":
                subcategories=IslingtonContentReader(html).get_subcategories()
        print(subcategories)
        return subcategories
    
    def get_subcategory_content(self, request_url, region):
        html, title=Scraper().scrape(request_url)
        data={
            "sub-subcategory_link": request_url, 
            "region": region, 
            "html": html, 
            "sub-subcategory_name": title
        }
        print(f"data for {request_url}, {title} scraped successfully")
        return data

    

        