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
