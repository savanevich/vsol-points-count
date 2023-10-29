from models.team import Team, TeamSchool
from models.participants import Participants
from models.player import Player


PARTICIPANTS = Participants([
    Team(10923, 'Колон', TeamSchool.RAIN,),
    Team(8138, 'Сантьяго-де-Куба', TeamSchool.RAIN,),
    Team(8160, 'Пинар-дель-Рио', TeamSchool.RAIN,),
    Team(10927, 'Виньялес', TeamSchool.RAIN,),
    Team(8967, 'Испано Америка (Гавана)', TeamSchool.RAIN,),
    Team(8965, 'Мордасо (Сагуа-ла-Гранде)', TeamSchool.RAIN,),
    Team(8140, 'Санкти-Спиритус', TeamSchool.RAIN,),
    Team(8985, 'Азукарерос (Санта-Клара)', TeamSchool.RAIN,),
    Team(8963, 'Гальехо (Пласетас)', TeamSchool.RAIN,),
    Team(8143, 'Ла-Гавана', TeamSchool.RAIN,),
    Team(18588, 'Хесус-Менендес', TeamSchool.RAIN,),
    Team(8139, 'Вилья-Клара (Санта-Клара)', TeamSchool.RAIN,),
    Team(8176, 'Гранма (Баямо)', TeamSchool.RAIN,),
])

PLAYERS_PARTICIPANTS = Participants([
    Player(6418920, 'Хорхе Фигуэрас', 8143),
    Player(6277010, 'Минни Мигель', 8143),
    Player(6422841, 'Эдуард Мартинез', 8143),
    Player(6460092, 'Рейнери Гамбоа', 8139),
    Player(6288655, 'Рейчарлес Фолх', 10927),
    Player(6277351, 'Йордан Францис', 8967),
    Player(6510694, 'Дарвин Казанова', 8985),
    Player(6549813, 'Серхио Рейс', 8140),
    Player(6460091, 'Луис Сюидад', 8160),
    Player(6577271, 'Сантос Бумелахо', 8143),
    Player(6556790, 'Сальвадор Лисама', 8143),
    Player(6419281, 'Карел Плаза', 8138),
    Player(6284804, 'Йениер Росабал', 8176),
])
