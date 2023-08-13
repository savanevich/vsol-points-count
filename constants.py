from enum import Enum


class TeamSchool(Enum):
    RAIN = 'rain'
    SUN = 'sun'


TEAMS = [
    ('Виньялес', TeamSchool.RAIN),
    ('Колон', TeamSchool.RAIN),
    ('Азукарерос (Санта-Клара)', TeamSchool.RAIN),
    ('Сантьяго-де-Куба', TeamSchool.RAIN),
    ('Вилья-Клара (Санта-Клара)', TeamSchool.RAIN),
    ('Санкти-Спиритус', TeamSchool.RAIN),
    ('Ягуаяй', TeamSchool.SUN),
    ('Гранма (Баямо)', TeamSchool.RAIN),
    ('Гальехо (Пласетас)', TeamSchool.RAIN),
    ('Ла-Гавана', TeamSchool.RAIN),
    ('Матансас', TeamSchool.RAIN),
    ('Хигуаги', TeamSchool.SUN),
    ('Хесус-Менендес', TeamSchool.RAIN),
    ('Хатибонико', TeamSchool.SUN),
    ('Чамбас', TeamSchool.RAIN),
    ('Пуэрто Падре', TeamSchool.SUN),
    ('Реал Ибериа (Гавана)', TeamSchool.SUN),
    ('Испано Америка (Гавана)', TeamSchool.RAIN),
    ('Артемиса (Сан-Кристобаль)', TeamSchool.SUN),
    ('Пинар-дель-Рио', TeamSchool.RAIN),
    ('Камагуэй', TeamSchool.SUN),
    ('Гуане', TeamSchool.RAIN),
    ('Сьего-де-Авила', TeamSchool.SUN),
]

ALL_TOURNAMENTS_STATISTIC_URL = 'https://virtualsoccer.ru/statistics.php?act=29&full_view=0&sort=5&order=0&division=0&fin_season=0&group_stat=0&pl_min_season=66&plus_minus_type=100&country=80'
OFF_SEASON_CUP_TOURNAMENTS_STATISTIC_URL = 'https://virtualsoccer.ru/statistics.php?act=29&sort=5&continent=0&country=80&division=0&pl_min_season=66&plus_minus_type=2'
CHAMPIONSHIP_TOURNAMENTS_STATISTIC_URL = 'https://virtualsoccer.ru/statistics.php?act=29&sort=5&continent=0&country=80&division=0&pl_min_season=66&plus_minus_type=3'
COUNTRY_CUP_STATISTIC_URL = 'https://virtualsoccer.ru/statistics.php?act=29&sort=5&continent=0&country=80&division=0&pl_min_season=66&plus_minus_type=4'
CHALLENGE_CUP_STATISTIC_URL = 'https://virtualsoccer.ru/statistics.php?act=29&sort=5&continent=0&country=80&division=0&pl_min_season=66&plus_minus_type=47'

TABLE_HEADER_MARKUP = '''
[table]
[tr][th][/th][th]Клуб[/th][th]Плюс-минуc[/th][th]Разница +/-[/th][th]Школа[/th][/tr]
'''
TABLE_BOTTOM_MARKUP = '[/table]'
