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
        
        non_national_team_row = self._find_team_row([
            'Во всех матчах за команды:',
            'Суммарно во всех матчах:'
        ])
        
        if not non_national_team_row:
            logger.debug('Did not play for the national team.')
            return 0

        team_pluses = non_national_team_row.select_one(
            PlayerStatisticLocators.PLUS_LOCATOR
        )

        if not team_pluses:
            logger.debug('Did not find pluses.')
            return 0

        sign = non_national_team_row.select_one(
            PlayerStatisticLocators.SIGN_LOCATOR
        )

        pluses = int(team_pluses.string) if team_pluses.string.isdigit() else 0

        if sign and sign['src'] == 'pics/down.gif':
            pluses = -pluses

        logger.debug(f'Found player has {pluses} pluses.')
        return pluses

    def _find_team_row(self, patterns):
        for pattern in patterns:
            row = self.parent.find_all(text=re.compile(pattern))
            if row:
                return row[0].parent.parent
        return None
