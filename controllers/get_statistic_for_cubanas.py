import requests
import logging

from pages.statistic_page import StatisticsPage
from constants import TEAMS, ALL_TOURNAMENTS_STATISTIC_URL, TABLE_HEADER_MARKUP, TABLE_BOTTOM_MARKUP

logger = logging.getLogger('scraping.get_statistic_for_cubanas')
logging.basicConfig(level=logging.INFO)


def load_statistics(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.content
    except requests.RequestException as e:
        logger.error(f"Error loading statistics from {url}: {e}")
        return None


def generate_team_row(index, team, team_data):
    return f'[tr][td]{index}[/td][td]{team}[/td][td]{team_data["pluses"]}{team_data["minuses"]}[/td][td]{team_data["total"]}[/td][td][img]https://virtualsoccer.ru/styles/school_{dict(TEAMS)[team].value}_1.png[/img][/td][/tr]\n'


def print_team_statistics(teams):
    result = TABLE_HEADER_MARKUP

    index = 1

    for team in teams:
        if team.name in dict(TEAMS):
            result += generate_team_row(index, team.name, {
                "pluses": team.pluses,
                "minuses": team.minuses,
                "total": team.total
            })
            index += 1

    result += TABLE_BOTTOM_MARKUP

    print(result)


def print_statistic_cubanas():
    logger.info('Loading statistics for Cubanas...')

    page_content = load_statistics(ALL_TOURNAMENTS_STATISTIC_URL)
    if not page_content:
        return

    logger.info('Finished loading statistics for Cubanas...')

    page = StatisticsPage(page_content)
    teams = page.teams

    print_team_statistics(teams)
