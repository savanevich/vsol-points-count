import re
import logging
from bs4 import BeautifulSoup

from locators.team_vs import TeamVsStatisticLocators
from parsers.team_vs_parser import TeamAverageAgeParser

logger = logging.getLogger('scraping.teams_vs_page')


class TeamVsPage:
    def __init__(self, page_content):
        logger.debug('Parsing page content with BeautifulSoup HTML parser.')
        self.soup = BeautifulSoup(page_content, 'html.parser')

    @property
    def teams(self):
        logger.debug(
            f'Finding all teams in the page using `{TeamVsStatisticLocators.TEAM}`.')

        return [TeamAverageAgeParser(e) for e in self.soup.select(TeamVsStatisticLocators.TEAM)]
