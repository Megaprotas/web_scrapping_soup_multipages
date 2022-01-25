import re
from bs4 import BeautifulSoup

from locators.all_books import AllBooksLocator
from parsers.book_parser import BookParser


class AllBooksPage:
    def __init__(self, page):
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def books(self):
        return [BookParser(e) for e in self.soup.select(AllBooksLocator.BOOKS)]

    @property
    def page_count(self):
        page_num = AllBooksLocator.PAGE_NUM
        content = self.soup.select_one(page_num).string
        page_num_regex = "Page [0-9]+ of ([0-9]+)"
        matcher = re.search(page_num_regex, content)
        final_page = int(matcher.group(1))
        return final_page

