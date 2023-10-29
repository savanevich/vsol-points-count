import re
import logging

from locators.player import PlayerStatisticLocators

logger = logging.getLogger('scraping.player_parser')


class PlayerParser:
    """A class for parsing player statistics."""

    def __init__(self, parent):
        """
        Initialize the PlayerParser.

        :param parent: The parent element to parse.
        """
        logger.debug(f'New player parser created from `{parent}`.')
        self.parent = parent

    def __repr__(self):
        return '<Player>'

    @property
    def pluses(self):
        """
        Find and return the number of pluses for the player.

        :return: The number of pluses (or None if not found).
        """
        logger.debug('Finding pluses for player...')
        non_national_team_row = self.parent.find_all(
            text=re.compile('Во всех матчах за команды:'))

        if not non_national_team_row:
            logger.debug('Did not play for the national team.')
            non_national_team_row = self.parent.find_all(
                text=re.compile('Суммарно во всех матчах:'))

        team_pluses = non_national_team_row[0].parent.parent.select_one(
            PlayerStatisticLocators.PLUS_LOCATOR)

        if not team_pluses:
            logger.debug('Did not find pluses.')
            return 0

        logger.debug(f'Found player has {team_pluses} pluses.')

        return int(team_pluses.string) if team_pluses.string.isdigit() else 0
