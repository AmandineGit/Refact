from models.urls import UrlIndex
from controllers.base import Controller

link = UrlIndex("https://books.toscrape.com/")


UrlIndex.extract_urls_sidebar(link)
Controller.createListPagesCategory("Temp_name_links_catego.json")