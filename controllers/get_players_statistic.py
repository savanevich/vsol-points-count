import requests
import logging
import json

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


def print_players_statistics_table(statistics: List[Dict[str, Any]], index: int, statistics_file_path: str):
    table_header = '''
[table]
[tr][th][/th][th]Игрок[/th][th]Клуб[/th][th][img]https://virtualsoccer.ru/pics/up.gif[/img][/th][/tr]
'''

    result = [table_header]

    try:
        with open(statistics_file_path, 'r', encoding='utf-8') as file:
            previous_data = file.read()
            previous_data = json.loads(previous_data)
    except FileNotFoundError:
        previous_data = None

    for player_num, (player_id, data) in enumerate(statistics, start=index):
        player = PLAYERS_PARTICIPANTS.get_participant_by_id(player_id)
        player_team = player.team(PARTICIPANTS)

        if not player_team:
            logger.error(
                f'Cannot find team for player {player.name} ({player_id})')
            continue

        diff_html = ""
        diff_num_html = ""
        
        if previous_data:
            for prev_participant_i, prev_participant  in enumerate(previous_data):
                if prev_participant[0] == player_id:
                    prev_total = prev_participant[1]["total"]
                    prev_participant_num = prev_participant_i + 1

                    if prev_total != data["total"]:
                        if prev_total > data["total"]:
                            diff_html = f'[size=60][color=#FF0000]({data["total"] - prev_total})[/color][/size]'
                        else:
                            diff_html = f'[size=60][color=#008000](+{data["total"] - prev_total})[/color][/size]'

                    if prev_participant_num != player_num:
                        if prev_participant_num > player_num:
                            diff_num_html = f'[size=60][color=#008000](+{prev_participant_num - player_num})[/color][/size]'
                        else:
                            diff_num_html = f'[size=60][color=#FF0000]({prev_participant_num - player_num})[/color][/size]'

        row = (
            f'[tr][td]{player_num} {diff_num_html}[/td][td][url=https://virtualsoccer.ru/player.php?num={player_id}][color=#0000BF]{player.name}[/color][/url][/td]'
            f'[td][img]https://virtualsoccer.ru/pics/teams18/{player_team.id}.png[/img] [url=https://virtualsoccer.ru/roster.php?num={player_team.id}]'
            f'[color=#0000BF]{player_team.name}[/color][/url][/td][td]{data["total"]} {diff_html}[/td][/tr]\n'
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


def commit_new_statistics(total_result, statistics_file_path):
    user_confirmation = input("Do you want to commit this data to the file? (yes/no): ").lower()

    if user_confirmation == 'yes':
        with open(statistics_file_path, 'w', encoding='utf-8') as file:
            file.write(json.dumps(total_result, ensure_ascii=False))
        print(f'Data has been encoded and stored in ./fixtures/cubanas.json')
    else:
        print('Data was not saved to the file.')


def print_statistic_olivares():
    logger.info('Loading statistics for Olivares...')
    statistics_file_path = './fixtures/olivares.json'
    statistics = []

    for player in PLAYERS_PARTICIPANTS.participants:
        player_statistic = fetch_player_statistics(
            PLAYER_STATISTIC_URL.format(player_id=player.id))

        if player_statistic:
            statistics.append(
                {'id': player.id, 'statistics': player_statistic})

    logger.info('Finished loading statistics for Olivares.')

    total_result = calculate_players_total_result(statistics)

    print_players_statistics_table(total_result, index=1, statistics_file_path=statistics_file_path)
    commit_new_statistics(total_result, statistics_file_path)
