import requests
import logging
import json

from pages.statistic_page import StatisticsPage
from controllers.constants import CURRENT_SEASON_ALL_TOURNAMENTS_STATISTIC_URL, COUNTRY_CUP_STATISTIC_URL, \
    CHALLENGE_CUP_STATISTIC_URL, OFF_SEASON_CUP_TOURNAMENTS_STATISTIC_URL, CHAMPIONSHIP_TOURNAMENTS_STATISTIC_URL, \
    TABLE_HEADER_MARKUP, TABLE_BOTTOM_MARKUP, TABLE_HEADER_MARKUP_WITH_ADDITIONAL_POINTS
from participants import PARTICIPANTS, STATISTIC_CORRECTIONS

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


def print_statistics_table(statistics, index, statistics_file_path, with_additional_points=False):
    result = TABLE_HEADER_MARKUP if not with_additional_points else TABLE_HEADER_MARKUP_WITH_ADDITIONAL_POINTS

    try:
        with open(statistics_file_path, 'r', encoding='utf-8') as file:
            previous_data = file.read()
            previous_data = json.loads(previous_data)
    except FileNotFoundError:
        previous_data = None

    for team_num, (team_name, data) in enumerate(statistics, start=index):
        team = PARTICIPANTS.get_participant_by_name(team_name)
        minuses = data["minuses"] if data["minuses"] != 0 else ""

        diff_html = ""
        diff_num_html = ""

        if previous_data:
            for prev_participant_i, prev_participant in enumerate(previous_data):
                if prev_participant[0] == team_name:
                    prev_total = prev_participant[1]["total"]
                    prev_participant_num = prev_participant_i + 1

                    if prev_total != data["total"]:
                        if prev_total > data["total"]:
                            diff_html = f'[size=60][color=#FF0000]({data["total"] - prev_total})[/color][/size]'
                        else:
                            diff_html = f'[size=60][color=#008000](+{data["total"] - prev_total})[/color][/size]'
                    
                    if prev_participant_num != team_num:
                        if prev_participant_num > team_num:
                            diff_num_html = f'[size=60][color=#008000](+{prev_participant_num - team_num})[/color][/size]'
                        else:
                            diff_num_html = f'[size=60][color=#FF0000]({prev_participant_num - team_num})[/color][/size]'

        result += (
            f'[tr][td]{team_num} {diff_num_html}[/td][td][img]https://virtualsoccer.ru/pics/teams18/{team.id}.png[/img] [url=https://virtualsoccer.ru/roster.php?num={team.id}][color=#0000BF]{team_name}[/color][/url][/td][td]{team.division.value}[/td][td]{data["pluses"]}{minuses}[/td]{'[td]' + str(data["pluses"] + data["minuses"]) + '[/td]' + '[td]' + str(data["additional"]) + '[/td]' if with_additional_points else ''}'
            f'[td]{data["total"]} {diff_html}[/td][/tr]\n'
        )

    result += TABLE_BOTTOM_MARKUP
    print(result)


def calculate_total_result(statistics, additional_points=None):
    total_result = {}

    for team in PARTICIPANTS.participants:
        if additional_points and team.name in additional_points:
            total_result[team.name] = {"pluses": 0, "minuses": 0, "additional": additional_points[team.name], "total": 0}
        else:
            total_result[team.name] = {"pluses": 0, "minuses": 0, "additional": 0, "total": 0}

        for tournament_statistic in statistics:
            for team_statistic in tournament_statistic:
                if team_statistic.name == team.name:
                    team_name = team_statistic.name
                    total_result[team_name]["pluses"] += team_statistic.pluses
                    total_result[team_name]["minuses"] += team_statistic.minuses
                    total_result[team_name]["total"] += team_statistic.total


        total_result[team.name]["total"] += total_result[team.name]["additional"]

    sorted_total_result = sorted(
        total_result.items(), key=lambda x: x[1]["total"], reverse=True)
    return sorted_total_result

def commit_new_statistics(total_result, statistics_file_path):
    user_confirmation = input("Do you want to commit this data to the file? (yes/no): ").lower()

    if user_confirmation == 'yes':
        with open(statistics_file_path, 'w', encoding='utf-8') as file:
            file.write(json.dumps(total_result, ensure_ascii=False))
        print(f'Data has been encoded and stored in {statistics_file_path}.')
    else:
        print('Data was not saved to the file.')


def print_statistic_ciego():
    logger.info('Loading statistics for Ciego...')
    statistics_file_path = './fixtures/ciego.json'

    statistics = [
        fetch_statistics(OFF_SEASON_CUP_TOURNAMENTS_STATISTIC_URL),
        fetch_statistics(CHAMPIONSHIP_TOURNAMENTS_STATISTIC_URL)
    ]

    logger.info('Finished loading statistics for Ciego.')

    total_result = calculate_total_result(statistics)
    print_statistics_table(total_result, index=1, statistics_file_path=statistics_file_path)
    commit_new_statistics(total_result, statistics_file_path)


def print_statistic_cubanas():
    logger.info('Loading statistics for Cubanas...')
    statistics_file_path = './fixtures/cubanas.json'

    statistics = [
        fetch_statistics(CURRENT_SEASON_ALL_TOURNAMENTS_STATISTIC_URL),
    ]

    logger.info('Finished loading statistics for Cubanas.')

    total_result = calculate_total_result(statistics, additional_points=STATISTIC_CORRECTIONS['cubanas'])
    print_statistics_table(total_result, index=1, statistics_file_path=statistics_file_path, with_additional_points=True)
    commit_new_statistics(total_result, statistics_file_path)


def print_statistic_trinidad():
    logger.info('Loading statistics for Trinidad...')
    statistics_file_path = './fixtures/trinidad.json'

    statistics = [
        fetch_statistics(COUNTRY_CUP_STATISTIC_URL),
        fetch_statistics(CHALLENGE_CUP_STATISTIC_URL),
    ]

    logger.info('Finished loading statistics for Trinidad.')

    total_result = calculate_total_result(statistics)
    print_statistics_table(total_result, index=1, statistics_file_path=statistics_file_path)
    commit_new_statistics(total_result, statistics_file_path)
