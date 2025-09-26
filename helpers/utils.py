from bs4 import BeautifulSoup as bs
import requests
from loguru import logger


def make_soup(url: str) -> bs:
    try:
        page = requests.get(url)
    except FileNotFoundError:
        logger.info("trouble loading the url")
    soup_ = bs(page.text, "html.parser")
    return soup_


def parse_page(hats_: list, results_: list) -> list:
    for hat in hats_:
        result = {
            "name": hat.find("h3").text.strip(),
            "price": hat.find(
                "span", class_="price-item price-item--sale price-item--last"
            ).text.strip(),
            "manufacturer": hat.find(
                "div", class_="caption-with-letter-spacing light"
            ).text,
        }
        results_.append(result)
    return results_
