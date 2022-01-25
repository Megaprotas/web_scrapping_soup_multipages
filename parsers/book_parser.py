import re

from locators.book import Book


class BookParser:

    RATING_CONVERTER = {
        'One': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5
    }

    def __init__(self, parent):
        self.parent = parent

    def __repr__(self):
        return f'Content: {self.name} for {self.price} rating {self.rating} star(s).'

    @property
    def name(self):
        name = Book.NAME
        item_link =  self.parent.select_one(name)
        item_name = item_link.attrs['title']
        return item_name

    @property
    def link(self):
        link = Book.LINK
        item_link = self.parent.select_one(link).attrs['href']
        return item_link

    @property
    def price(self):
        price = Book.PRICE
        item_price = self.parent.select_one(price).string

        regex_pattern = '£([0-9]+\.[0-9]+)'
        matcher = re.search(regex_pattern, item_price)
        return float(matcher.group(1))

    @property
    def rating(self):
        rating = Book.RATING
        star_rating = self.parent.select_one(rating)
        class_finder = star_rating.attrs['class']
        rating_remaining_classes = [r for r in class_finder if r != 'star-rating']    # try filter instead

        # convert 'Three' to 3. Print not found if rating is not found
        rating_conversion = BookParser.RATING_CONVERTER.get(rating_remaining_classes[0], 'Not found')
        return rating_conversion
