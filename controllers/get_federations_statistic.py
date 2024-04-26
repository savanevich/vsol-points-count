import requests
import logging
import json

from typing import Any, Union

logger = logging.getLogger('scraping.get_statistic')
logging.basicConfig(level=logging.INFO)

## Loads all the federations and their statistics and order them by the total number of points.

def load_statistics(url: str) -> Union[None, Any]:
    try:
        response = requests.get(url)
        return response.content
    except requests.RequestException as e:
        logger.error(f"Error loading statistics from {url}: {e}")
        return None
    
def fetch_federations_statistics(url: str) -> Union[None, Any]:
    statistic_page_content = load_statistics(url)
    if not statistic_page_content:
        return None
    statistic_page = FederationsStatisticsPage(statistic_page_content)
    return statistic_page.federations

def print_federations_statistics_table(statistics: Any, index: int, statistics_file_path: str) -> None:
    table_header = '''
[table]
[tr][th][/th][th]Федерация[/th][th]Кол-во участников[/th][th]Сумма очков[/th][/tr]
'''
    result = [table_header]
    try:
        with open(statistics_file_path, 'r', encoding='utf-8') as file:
            previous_data = file.read()
            previous_data = json.loads(previous_data)
    except FileNotFoundError:
        previous_data = None
    for federation_num, (federation_id, data) in enumerate(statistics, start=index):
        federation = FEDERATIONS_PARTICIPANTS.get_participant_by_id(federation_id)
        diff_html = ""
        diff_num_html = ""
        if previous_data:
            for prev_participant_i, prev_participant  in enumerate(previous_data):
                if prev_participant[0] == federation_id:
                    prev_total = prev_participant[1]["total"]
                    prev_participant_num = prev_participant_i + 1
                    if prev_total != data["total"]:
                        if prev_total > data["total"]:
                            diff_html = f'[size=60][color=#FF0000]({data["total"] - prev_total})[/color][/size]'
                        else:
                            diff_html = f'[size=60][color=#008000](+{data["total"] - prev_total})[/color][/size]'
                    if prev_participant_num != federation_num:
                        if prev_participant_num > federation_num:
                            diff_num_html = f'[size=60][color=#008000](+{prev_participant_num - federation_num})[/color][/size]'
                        else:
                            diff_num_html = f'[size=60][color=#FF0000]({prev_participant_num - federation_num})[/color][/size]'
        result.append(f'[tr][td]{federation_num}[/td][td]{federation.name}[/td][td]{data["total"]}[/td][td]{data["total"]}[/td][/tr]{diff_html}{diff_num_html}')
    result.append('[/table]')
    
    with open(statistics_file_path, 'w', encoding='utf-8') as file:
        file.write(json.dumps(statistics))
    return result