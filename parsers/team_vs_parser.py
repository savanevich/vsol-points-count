import re
import logging

from locators.team import TeamStatisticLocators
from locators.team_vs import TeamVsStatisticLocators

logger = logging.getLogger('scraping.team_average_age_parser')


class TeamAverageAgeParser:
    def __init__(self, parent):
        logger.debug(f'New team parser created from `{parent}`.')
        self.parent = parent

    def __repr__(self):
        return f'<Team {self.name}>'

    @property
    def name(self):
        logger.debug('Finding team name...')
        locator = TeamVsStatisticLocators.NAME_LOCATOR
        team_name = self.parent.select_one(locator).string
        logger.debug(f'Found team name, `{team_name}`.')
        return team_name

    @property
    def vs(self):
        logger.debug('Finding team VS...')
        locator = TeamVsStatisticLocators.VS_LOCATOR
        vs = self.parent.select_one(locator).string
        logger.debug(f'Found team has {vs} VS.')
        return int(vs)

    @property
    def cost(self):
        logger.debug('Finding team cost...')
        locator = TeamVsStatisticLocators.COST_LOCATOR
        cost = self.parent.select_one(locator).string
        logger.debug(f'Found team has {cost} cost.')
        return int(cost.replace(' ', ''))
