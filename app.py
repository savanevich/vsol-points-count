import requests
import logging

from pages.all_books_page import AllBooksPage

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S',
                    filename='logs.txt')

logger = logging.getLogger('scraping')

logger.info('Loading statistics...')

page_content = requests.get('https://virtualsoccer.ru/statistics.php?act=29&full_view=0&sort=5&order=0&division=0&fin_season=0&group_stat=0&pl_min_season=66&plus_minus_type=100&country=80').content

page = AllBooksPage(page_content)

books = page.books

for page_num in range(1, page.page_count):
    url = f'http://books.toscrape.com/catalogue/page-{page_num + 1}.html'
    page_content = requests.get(url).content
    page = AllBooksPage(page_content)
    books.extend(page.books)

print(len(books))
