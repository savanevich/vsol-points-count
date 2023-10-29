import requests
import logging

from pages.player_statistic_page import PlayersStatisticsPage
from controllers.constants import TABLE_BOTTOM_MARKUP, PLAYER_STATISTIC_URL
from participants import PARTICIPANTS, PLAYERS_PARTICIPANTS

from typing import List, Dict, Any, Union, Tuple

logger = logging.getLogger('scraping.get_statistic')
logging.basicConfig(level=logging.INFO)


def load_statistics(url: str) -> Union[bytes, None]:
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.content
    except requests.RequestException as e:
        logger.error(f"Error loading statistics from {url}: {e}")
        return None


def fetch_player_statistics(url: str) -> Union[None, Any]:
    statistic_page_content = load_statistics(url)
    if not statistic_page_content:
        return None

    statistic_page = PlayersStatisticsPage(statistic_page_content)
    return statistic_page.player


def print_players_statistics_table(statistics: List[Dict[str, Any]], index: int):
    table_header = '''
[table]
[tr][th][/th][th]Игрок[/th][th]Клуб[/th][th][img]https://virtualsoccer.ru/pics/up.gif[/img][/th][/tr]
'''

    result = [table_header]

    for player_num, (player_id, data) in enumerate(statistics, start=index):
        player = PLAYERS_PARTICIPANTS.get_participant_by_id(player_id)
        player_team = player.team(PARTICIPANTS)

        row = (
            f'[tr][td]{player_num}[/td][td][url=https://virtualsoccer.ru/player.php?num={player_id}][color=#0000BF]{player.name}[/color][/url][/td]'
            f'[td][img]https://virtualsoccer.ru/pics/teams18/{player_team.id}.png[/img] [url=https://virtualsoccer.ru/roster.php?num={player_team.id}]'
            f'[color=#0000BF]{player_team.name}[/color][/url][/td][td]{data["total"]}[/td][/tr]\n'
        )
        result.append(row)

    result.append(TABLE_BOTTOM_MARKUP)
    print(''.join(result))


def calculate_players_total_result(statistics: List[Dict[str, Any]]) -> List[Tuple[str, Dict[str, Any]]]:
    total_result = {}

    for player in statistics:
        total_result[player['id']] = {"total": player['statistics'].pluses}

    sorted_total_result = sorted(
        total_result.items(), key=lambda x: x[1]["total"], reverse=True)
    return sorted_total_result


def print_statistic_olivares():
    logger.info('Loading statistics for Olivares...')
    statistics = []

    for player in PLAYERS_PARTICIPANTS.participants:
        player_statistic = fetch_player_statistics(
            PLAYER_STATISTIC_URL.format(player_id=player.id))

        if player_statistic:
            statistics.append(
                {'id': player.id, 'statistics': player_statistic})

    logger.info('Finished loading statistics for Olivares.')

    total_result = calculate_players_total_result(statistics)

    print_players_statistics_table(total_result, index=1)
