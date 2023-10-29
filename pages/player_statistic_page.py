import re
import logging
from bs4 import BeautifulSoup

from locators.player import PlayerStatisticLocators
from parsers.player_parser import PlayerParser

logger = logging.getLogger('scraping.players_statistics_page')


class PlayersStatisticsPage:
    def __init__(self, page_content):
        """
        Initialize the PlayersStatisticsPage with the HTML page content.
        """
        self.soup = BeautifulSoup(page_content, 'html.parser')
        logger.debug('Parsed page content with BeautifulSoup HTML parser.')

    @property
    def player(self):
        """
        Find and return the player statistics from the page.
        """
        player_statistic_elements = self.find_player_statistic()

        if not player_statistic_elements:
            logger.warning("Player statistic element not found.")
            return None

        return PlayerParser(player_statistic_elements)

    def find_player_statistic(self):
        """
        Find player statistic elements on the page.
        """
        player_statistic_elements = self.soup.find_all(
            text=re.compile('Суммарно во всех матчах:'))[0].parent.parent.parent.parent
        return player_statistic_elements
