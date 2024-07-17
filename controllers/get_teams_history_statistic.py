import requests
import logging
import json

from pages.statistic_page import StatisticsPage
from controllers.constants import CURRENT_SEASON, ALL_TOURNAMENTS_STATISTIC_URL
from participants import PARTICIPANTS

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

def calculate_total_result(statistics):
    total_result = {}

    for team in PARTICIPANTS.participants:
        season = int(CURRENT_SEASON) - 5
        total_result[team.name] = {"total": 0}

        for season_statistic in statistics:
            for team_statistic in season_statistic:
                if team_statistic.name == team.name:
                    team_name = team_statistic.name
                    total_result[team_name][season] = {"pluses": 0, "minuses": 0, "total": 0}

                    total_result[team_name][season]["pluses"] = team_statistic.pluses
                    total_result[team_name][season]["minuses"] = team_statistic.minuses
                    total_result[team_name][season]["total"] = team_statistic.total
                    total_result[team_name]["total"] += team_statistic.total

            season += 1

    sorted_total_result = sorted(
        total_result.items(), key=lambda x: x[1]["total"], reverse=True)
    return sorted_total_result

def print_statistics_table(total_result, index):
    seasons_header = "".join([f'[th]{str(i)}[/th]' for i in range(int(CURRENT_SEASON) - 5, int(CURRENT_SEASON))])

    result = f'''
[table]
[tr][th][/th][th]Команда[/th]{seasons_header}[th]Средний[/th][/tr]
'''

    for team_num, (team_name, data) in enumerate(total_result, start=index):
        team = PARTICIPANTS.get_participant_by_name(team_name)

        result += f'[tr][td]{team_num}[/td][td][img]https://virtualsoccer.ru/pics/teams18/{team.id}.png[/img] [url=https://virtualsoccer.ru/roster.php?num={team.id}][color=#0000BF]{team_name}[/color][/url][/td]'
        for i in range(int(CURRENT_SEASON) - 5, int(CURRENT_SEASON)):
            result += f'[td]{data.get(i, {"total": 0})["total"]}[/td]'
        result += f'[td]{int(data["total"]) / 5}[/td][/tr]'

    result += '[/table]'

    print(result)

def print_teams_history_statistic():
    logger.info('Loading statistics for Teams History...')

    seasons = [str(i) for i in range(int(CURRENT_SEASON) - 5, int(CURRENT_SEASON))]

    statistics = [
        fetch_statistics(ALL_TOURNAMENTS_STATISTIC_URL + season)
        for season in seasons
    ]

    logger.info('Finished loading statistics for for Teams History.')

    total_result = calculate_total_result(statistics)

    print_statistics_table(total_result, index=1)
