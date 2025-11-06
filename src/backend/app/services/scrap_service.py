from bs4 import BeautifulSoup

import requests
from abc import ABC, abstractmethod
from typing import List
from async_lru import alru_cache

from uttils import try_except


class AbstractParser(ABC):
    def __init__(self):
        self.quotes = []
        self.authors = []
        self.full_quotes = {}
        
    @abstractmethod
    async def parse(self):
        pass

class Parser(AbstractParser):
    @try_except
    @alru_cache
    async def parse(self) -> List[str]:
        for i in range(1, 11):
            soup = BeautifulSoup(requests.get(f"https://quotes.toscrape.com/page/{i}").text, "html.parser")
            for quote in soup.findAll('span', class_='text'):
                for author in soup.findAll('small', class_='author'):
                    self.authors.append(author.text)
                self.quotes.append(quote.text)
                
            for i in range(len(self.quotes)):
                self.full_quotes[self.quotes[i]] = self.authors[i]
                
        return self.full_quotes
                
                
parser = Parser()