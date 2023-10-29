import re
import logging
from bs4 import BeautifulSoup

from locators.statistic_page import PointsStatisticLocators
from parsers.team_parser import TeamParser

logger = logging.getLogger('scraping.points_statistics_page')


class StatisticsPage:
    def __init__(self, page_content):
        logger.debug('Parsing page content with BeautifulSoup HTML parser.')
        self.soup = BeautifulSoup(page_content, 'html.parser')

    @property
    def teams(self):
        logger.debug(
            f'Finding all teams in the page using `{PointsStatisticLocators.TEAM}`.')

        return [TeamParser(e) for e in self.soup.select(PointsStatisticLocators.TEAM)]
