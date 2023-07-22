import re
import logging

from locators.team import TeamStatisticLocators

logger = logging.getLogger('scraping.team_parser')


class TeamParser:
    def __init__(self, parent):
        logger.debug(f'New team parser created from `{parent}`.')
        self.parent = parent

    def __repr__(self):
        return f'<Team {self.name}>'

    @property
    def name(self):
        logger.debug('Finding team name...')
        locator = TeamStatisticLocators.NAME_LOCATOR
        team_name = self.parent.select_one(locator).string
        logger.debug(f'Found team name, `{team_name}`.')
        return team_name

    @property
    def minuses(self):
        logger.debug('Finding team minuses...')
        locator = TeamStatisticLocators.MINUS_LOCATOR
        team_minuses = self.parent.select_one(locator).string
        logger.debug(f'Found team has {team_minuses} minuses.')
        return team_minuses

    @property
    def pluses(self):
        logger.debug('Finding pluses...')
        locator = TeamStatisticLocators.PLUS_LOCATOR
        team_pluses = self.parent.select_one(locator).string
        logger.debug(f'Found team has {team_pluses} minuses.')
        return team_pluses

    @property
    def total(self):
        logger.debug('Finding total...')
        locator = TeamStatisticLocators.TOTAL_LOCATOR
        team_total = self.parent.select_one(locator).string
        logger.debug(f'Found team has {team_total} total.')
        return team_total
