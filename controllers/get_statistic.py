import requests
import logging

from pages.statistic_page import StatisticsPage
from constants import TEAMS, ALL_TOURNAMENTS_STATISTIC_URL, COUNTRY_CUP_STATISTIC_URL, CHALLENGE_CUP_STATISTIC_URL, OFF_SEASON_CUP_TOURNAMENTS_STATISTIC_URL, CHAMPIONSHIP_TOURNAMENTS_STATISTIC_URL, TABLE_HEADER_MARKUP, TABLE_BOTTOM_MARKUP

logger = logging.getLogger('scraping.get_statistic')
logging.basicConfig(level=logging.INFO)


def load_statistics(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.content
    except requests.RequestException as e:
        logger.error(f"Error loading statistics from {url}: {e}")
        return None


def fetch_statistics(url):
    statistic_page_content = load_statistics(url)
    if not statistic_page_content:
        return

    statistic_page = StatisticsPage(statistic_page_content)
    return statistic_page.teams


def print_statistics_table(statistics, index):
    result = TABLE_HEADER_MARKUP

    for team_num, (team, data) in enumerate(statistics, start=index):
        minuses = data["minuses"] if data["minuses"] != 0 else ""
        team_image_url = f'https://virtualsoccer.ru/styles/school_{dict(TEAMS)[team].value}_1.png'
        result += (
            f'[tr][td]{team_num}[/td][td]{team}[/td][td]{data["pluses"]}{minuses}[/td]'
            f'[td]{data["total"]}[/td][td][img]{team_image_url}[/img][/td][/tr]\n'
        )

    result += TABLE_BOTTOM_MARKUP
    print(result)


def calculate_total_result(statistics):
    total_result = {}

    for team in dict(TEAMS).keys():
        total_result[team] = {"pluses": 0, "minuses": 0, "total": 0}

        for tournament_statistic in statistics:
            for team_statistic in tournament_statistic:
                if team_statistic.name == team:
                    team_name = team_statistic.name
                    total_result[team_name]["pluses"] += team_statistic.pluses
                    total_result[team_name]["minuses"] += team_statistic.minuses
                    total_result[team_name]["total"] += team_statistic.total

    sorted_total_result = sorted(
        total_result.items(), key=lambda x: x[1]["total"], reverse=True)
    return sorted_total_result


def print_statistic_ciego():
    logger.info('Loading statistics for Ciego...')

    statistics = [
        fetch_statistics(OFF_SEASON_CUP_TOURNAMENTS_STATISTIC_URL),
        fetch_statistics(CHAMPIONSHIP_TOURNAMENTS_STATISTIC_URL)
    ]

    logger.info('Finished loading statistics for Ciego.')

    total_result = calculate_total_result(statistics)
    print_statistics_table(total_result, index=1)


def print_statistic_cubanas():
    logger.info('Loading statistics for Cubanas...')

    statistics = [
        fetch_statistics(ALL_TOURNAMENTS_STATISTIC_URL),
    ]

    logger.info('Finished loading statistics for Cubanas.')

    total_result = calculate_total_result(statistics)
    print_statistics_table(total_result, index=1)


def print_statistic_trinidad():
    logger.info('Loading statistics for Trinidad...')

    statistics = [
        fetch_statistics(COUNTRY_CUP_STATISTIC_URL),
        fetch_statistics(CHALLENGE_CUP_STATISTIC_URL),
    ]

    logger.info('Finished loading statistics for Trinidad.')

    total_result = calculate_total_result(statistics)
    print_statistics_table(total_result, index=1)
