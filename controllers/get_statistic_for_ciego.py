import requests
import logging

from pages.statistic_page import StatisticsPage
from constants import TEAMS, OFF_SEASON_CUP_TOURNAMENTS_STATISTIC_URL, CHAMPIOSHIP_TOURNAMENTS_STATISTIC_URL, TABLE_HEADER_MARKUP, TABLE_BOTTOM_MARKUP

logger = logging.getLogger('scraping.get_statistic_for_ciego')
logging.basicConfig(level=logging.INFO)


def load_statistics(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.content
    except requests.RequestException as e:
        logger.error(f"Error loading statistics from {url}: {e}")
        return None


def print_statistics_table(statistics, index):
    result = TABLE_HEADER_MARKUP

    for team_num, (team, data) in enumerate(statistics, start=index):
        result += f'[tr][td]{team_num}[/td][td]{team}[/td][td]{data["pluses"]}{data["minuses"] if data["minuses"] != 0 else ""}[/td][td]{data["total"]}[/td][td][img]https://virtualsoccer.ru/styles/school_{dict(TEAMS)[team].value}_1.png[/img][/td][/tr]\n'

    result += TABLE_BOTTOM_MARKUP
    print(result)


def print_statistic_ciego():
    logger.info('Loading statistics for Ciego...')

    # Load statistics for off-season cup tournaments
    off_season_page_content = load_statistics(
        OFF_SEASON_CUP_TOURNAMENTS_STATISTIC_URL)
    if not off_season_page_content:
        return

    off_season_page = StatisticsPage(off_season_page_content)
    off_season_statistic = off_season_page.teams

    # Load statistics for championship tournaments
    championship_page_content = load_statistics(
        CHAMPIOSHIP_TOURNAMENTS_STATISTIC_URL)
    if not championship_page_content:
        return

    championship_page = StatisticsPage(championship_page_content)
    championship_statistic = championship_page.teams

    logger.info('Finished loading statistics for Ciego.')

    # Combine statistics for each team
    total_result = {}
    for team in dict(TEAMS).keys():
        total_result[team] = {"pluses": 0, "minuses": 0, "total": 0}

        for team_off_season in off_season_statistic:
            if team_off_season.name == team:
                total_result[team]["pluses"] += team_off_season.pluses
                total_result[team]["minuses"] += team_off_season.minuses
                total_result[team]["total"] += team_off_season.total

        for team_championship in championship_statistic:
            if team_championship.name == team:
                total_result[team]["pluses"] += team_championship.pluses
                total_result[team]["minuses"] += team_championship.minuses
                total_result[team]["total"] += team_championship.total

    # Sort and print statistics
    sorted_total_result = sorted(
        total_result.items(), key=lambda x: x[1]["total"], reverse=True)

    print_statistics_table(sorted_total_result, index=1)
