CURRENT_SEASON = '71'
ALL_TOURNAMENTS_STATISTIC_URL = 'https://virtualsoccer.ru/statistics.php?act=29&full_view=0&sort=5&order=0&division=0&fin_season=0&group_stat=0&plus_minus_type=100&country=80&pl_min_season='
CURRENT_SEASON_ALL_TOURNAMENTS_STATISTIC_URL = ALL_TOURNAMENTS_STATISTIC_URL + CURRENT_SEASON
OFF_SEASON_CUP_TOURNAMENTS_STATISTIC_URL = 'https://virtualsoccer.ru/statistics.php?act=29&sort=5&continent=0&country=80&division=0&pl_min_season=' + CURRENT_SEASON + '&plus_minus_type=2'
CHAMPIONSHIP_TOURNAMENTS_STATISTIC_URL = 'https://virtualsoccer.ru/statistics.php?act=29&sort=5&continent=0&country=80&division=0&pl_min_season=' + CURRENT_SEASON + '&plus_minus_type=3'
COUNTRY_CUP_STATISTIC_URL = 'https://virtualsoccer.ru/statistics.php?act=29&sort=5&continent=0&country=80&division=0&pl_min_season=' + CURRENT_SEASON + '&plus_minus_type=4'
CHALLENGE_CUP_STATISTIC_URL = 'https://virtualsoccer.ru/statistics.php?act=29&sort=5&continent=0&country=80&division=0&pl_min_season=' + CURRENT_SEASON + '&plus_minus_type=47'
PLAYER_STATISTIC_URL = 'https://virtualsoccer.ru/player_stats.php?num={player_id}&season=' + CURRENT_SEASON
TEAMS_VS_STATISTIC_URL = 'https://virtualsoccer.ru/statistics.php?act=0&full_view=0&sort=5&order=0&division=0&fin_season=0&group_stat=0&pl_min_season=0&plus_minus_type=0&country=80'

TABLE_HEADER_MARKUP = '''
[table]
[tr][th][/th][th]Клуб[/th][th]Див[/th][th]Плюс-минуc[/th][th]Разница +/-[/th][/tr]
'''
TABLE_HEADER_MARKUP_WITH_ADDITIONAL_POINTS = '''
[table]
[tr][th][/th][th]Клуб[/th][th]Див[/th][th]Плюс-минуc[/th][th]Разница +/-[/th][th]Баллы ТЦ[/th][th]Сумма[/th][/tr]
'''

TABLE_BOTTOM_MARKUP = '[/table]'
