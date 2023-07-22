import requests
import logging

from pages.statistic_page import StatisticsPage
from constants import TEAMS

ALL_TOURNAMENTS_STATISTIC_URL = 'https://virtualsoccer.ru/statistics.php?act=29&full_view=0&sort=5&order=0&division=0&fin_season=0&group_stat=0&pl_min_season=66&plus_minus_type=100&country=80'

logger = logging.getLogger('scraping.get_statistic_for_all')


def print_statistic_all():
    logger.info('Loading statistics...')

    page_content = requests.get(ALL_TOURNAMENTS_STATISTIC_URL).content
    page = StatisticsPage(page_content)

    teams = page.teams

    result = '''
[table]
[tr][th][/th][th]Клуб[/th][th]Плюс-минуc[/th][th]Разница +/-[/th][th]Школа[/th][/tr]
'''

    index = 1

    for team_num in range(0, len(teams)):
        if teams[team_num].name in dict(TEAMS).keys():
            result += f'[tr][td]{index}[/td][td]{teams[team_num].name}[/td][td]{teams[team_num].pluses}{teams[team_num].minuses}[/td][td]{teams[team_num].total}[/td][td][img]https://virtualsoccer.ru/styles/school_{dict(TEAMS)[teams[team_num].name].value}_1.png[/img][/td][/tr]\n'
            index = index + 1

    result += '[/table]'

    print(result)