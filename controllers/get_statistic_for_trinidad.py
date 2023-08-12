import requests
import logging

from pages.statistic_page import StatisticsPage
from constants import TEAMS, COUNTRY_CUP_STATISTIC_URL, CHALLENGE_CUP_STATISTIC_URL, TABLE_HEADER_MARKUP, TABLE_BOTTOM_MARKUP

logger = logging.getLogger('scraping.get_statistic_for_trininad')
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
        result += f'[tr][td]{team_num}[/td][td]{team}[/td][td]{data["pluses"]}{data["minuses"]}[/td][td]{data["total"]}[/td][td][img]https://virtualsoccer.ru/styles/school_{dict(TEAMS)[team].value}_1.png[/img][/td][/tr]\n'

    result += TABLE_BOTTOM_MARKUP
    print(result)


def print_statistic_trinidad():
    logger.info('Loading statistics for Trinidad...')

    # Load statistics for country cup tournament
    country_cup_page_content = load_statistics(
        COUNTRY_CUP_STATISTIC_URL)
    if not country_cup_page_content:
        return

    country_cup_page = StatisticsPage(country_cup_page_content)
    country_cup_statistic = country_cup_page.teams

    # Load statistics for challenge cup tournament
    challenge_cup_page_content = load_statistics(
        CHALLENGE_CUP_STATISTIC_URL)
    if not challenge_cup_page_content:
        return

    challenge_cup_page = StatisticsPage(challenge_cup_page_content)
    challenge_cup_statistic = challenge_cup_page.teams

    logger.info('Finished loading statistics for Trinidad.')

    # Combine statistics for each team
    total_result = {}
    for team in dict(TEAMS).keys():
        total_result[team] = {"pluses": 0, "minuses": 0, "total": 0}

        for team_off_season in country_cup_statistic:
            if team_off_season.name == team:
                total_result[team]["pluses"] += team_off_season.pluses
                total_result[team]["minuses"] += team_off_season.minuses
                total_result[team]["total"] += team_off_season.total

        for team_championship in challenge_cup_statistic:
            if team_championship.name == team:
                total_result[team]["pluses"] += team_championship.pluses
                total_result[team]["minuses"] += team_championship.minuses
                total_result[team]["total"] += team_championship.total

    # Sort and print statistics
    sorted_total_result = sorted(
        total_result.items(), key=lambda x: x[1]["total"], reverse=True)

    print_statistics_table(sorted_total_result, index=1)
