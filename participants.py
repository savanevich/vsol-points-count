from models.team import Team, TeamDivision, TeamSchool
from models.participants import Participants
from models.player import Player


PARTICIPANTS = Participants([
    Team(10927, 'Виньялес', TeamSchool.RAIN, TeamDivision.D1),
    # Team(10924, 'Пуэрто Падре', TeamSchool.RAIN, TeamDivision.D2),
    Team(18588, 'Хесус-Менендес', TeamSchool.RAIN, TeamDivision.D1),
    # Team(8985, 'Азукарерос (Санта-Клара)', TeamSchool.RAIN, TeamDivision.D2),
    Team(21374, 'Санта-Клара', TeamSchool.RAIN, TeamDivision.D2),
    # Team(18593, 'Пальмира', TeamSchool.RAIN, TeamDivision.D3A),
    Team(8143, 'Ла-Гавана', TeamSchool.RAIN, TeamDivision.D2),
    # Team(18587, 'Чамбас', TeamSchool.RAIN, TeamDivision.D2),
    # Team(8963, 'Гальехо (Пласетас)', TeamSchool.RAIN, TeamDivision.D3A),
    # Team(8172, 'Сьенфуэгос', TeamSchool.RAIN, TeamDivision.D3A),
    # Team(10917, 'Тринидад', TeamSchool.RAIN, TeamDivision.D2),
    # Team(10920, 'Морон', TeamSchool.RAIN, TeamDivision.D3A),
    Team(8965, 'Мордасо (Сагуа-ла-Гранде)', TeamSchool.RAIN, TeamDivision.D2),
    # Team(8962, 'Провинция-ла-Гавана', TeamSchool.RAIN, TeamDivision.D3A),
    # Team(18599, 'Ягуаяй', TeamSchool.RAIN, TeamDivision.D3A),
    # Team(21066, 'Хиро де Пьелес (Гавана)', TeamSchool.RAIN, TeamDivision.D3B),
    # Team(21106, 'Батабано', TeamSchool.RAIN, TeamDivision.D3B),
    # Team(10921, 'Минерос (Лас-Тунас)', TeamSchool.RAIN,),
    # Team(8140, 'Санкти-Спиритус', TeamSchool.RAIN,),
    Team(8155, 'Лас-Тунас', TeamSchool.RAIN, TeamDivision.D1),
    Team(18590, 'Артемиса (Сан-Кристобаль)', TeamSchool.RAIN, TeamDivision.D1),
    # Team(8961, 'Фортуна (Гьюнес)', TeamSchool.RAIN,),
    Team(10923, 'Колон', TeamSchool.RAIN, TeamDivision.D1),
    # Team(10925, 'Сан-Кристобаль', TeamSchool.RAIN,),
    # Team(21141, 'Казино Эспаньол (Гавана)', TeamSchool.RAIN, TeamDivision.D3B),
    # Team(8956, 'Реал Ибериа (Гавана)', TeamSchool.RAIN,),
    Team(8967, 'Испано Америка (Гавана)', TeamSchool.RAIN, TeamDivision.D1),
    # Team(18600, 'Мансанилло (Гуаканаябо)', TeamSchool.RAIN,),
    # Team(18586, 'Моа', TeamSchool.RAIN,),
    # Team(18598, 'Маябеке (Гавана)', TeamSchool.RAIN, TeamDivision.D3A),
    # Team(18652, 'Консоласион-дель-Сур', TeamSchool.RAIN,),
    # Team(8959, 'Депортиво Эспаньол (Майари)', TeamSchool.RAIN,),
    Team(8160, 'Пинар-дель-Рио', TeamSchool.RAIN, TeamDivision.D1),
    # Team(10916, 'Гуане', TeamSchool.RAIN,),
    Team(8138, 'Сантьяго-де-Куба', TeamSchool.RAIN, TeamDivision.D1),
    # Team(8178, 'Камагуэй', TeamSchool.RAIN,),
    # Team(18589, 'Эсмеральда', TeamSchool.RAIN,),
    # Team(18601, 'Палма-Сориано', TeamSchool.RAIN,),
    # Team(10926, 'Крусес', TeamSchool.RAIN,),
    # Team(8165, 'Сьюдад-де-ла-Гавана', TeamSchool.RAIN,),
    # Team(8148, 'Гуантанамо', TeamSchool.RAIN,),
    # Team(8139, 'Вилья-Клара (Санта-Клара)', TeamSchool.RAIN, TeamDivision.D1),
    # Team(8975, 'Серро (Гавана)', TeamSchool.RAIN,),
    # Team(10928, 'Хатибонико', TeamSchool.RAIN,),
    # Team(21109, 'Фуэрсас Армадас (Сьенфуэгос)', TeamSchool.RAIN,),
    # Team(8153, 'Исла-де-ла-Ювентуд (Нуэва-Жерона)', TeamSchool.RAIN,),
    # Team(10930, 'Куманаягуа', TeamSchool.RAIN,),
    # Team(10919, 'Вертьентес', TeamSchool.RAIN,),
    # Team(10929, 'Кабайгуан', TeamSchool.RAIN,),
    # Team(8146, 'Матансас', TeamSchool.RAIN,),
    # Team(8957, 'Дьяблос Рохос (Сантьяго-де-Куба)', TeamSchool.RAIN,),
    # Team(8176, 'Гранма (Баямо)', TeamSchool.RAIN,),
    # Team(18640, 'Контрамаестре', TeamSchool.RAIN,),
    # Team(8177, 'Ольгин (Банес)', TeamSchool.RAIN,),
    # Team(10910, 'Флорида', TeamSchool.RAIN,),
    # Team(8171, 'Сьего-де-Авила', TeamSchool.RAIN,),
    # Team(8968, 'Гранхерос', TeamSchool.RAIN,),
    # Team(8955, 'Олимпия (Манзанильо)', TeamSchool.RAIN,),
    # Team(8971, 'Атуэй (Контрамаэстре)', TeamSchool.RAIN,),
    # Team(10915, 'Депортиво Сентрал (Гавана)', TeamSchool.RAIN,),
    Team(10918, 'Ховельянос', TeamSchool.RAIN, TeamDivision.D2),
    # Team(8960, 'Хувентуд Астуриана (Гавана)', TeamSchool.RAIN,),
    # Team(18611, 'Хигуаги', TeamSchool.RAIN,),
    # Team(21068, 'Сан Франциско (Гавана)', TeamSchool.RAIN,),
    # Team(18595, 'Банес', TeamSchool.RAIN,),
    # Team(8966, 'Пуэнтес Грандес (Палма-Сориано)', TeamSchool.RAIN,),
    # Team(18596, 'Карденас', TeamSchool.RAIN,),
    Team(18639, 'Баракоа', TeamSchool.RAIN, TeamDivision.D2),
    # Team(21127, 'Консепсьон Аренал (Санкти-Спиритус)', TeamSchool.RAIN,),
    # Team(8969, 'Роверс (Гавана)', TeamSchool.RAIN,),
    # Team(21415, 'Кубанитро (Гавана)', TeamSchool.RAIN,),
    # Team(21069, 'Юнион (Сьенфуэгос)', TeamSchool.RAIN,),
    # Team(8174, 'Индустриалес (Гавана)', TeamSchool.RAIN,),
    # Team(21070, 'Уракан (Ольгин)', TeamSchool.RAIN, TeamDivision.KLK),
])

PLAYERS_PARTICIPANTS = Participants([
    Player(6556790, 'Сальвадор Лисама', 8143),
    Player(6549820, 'Лейниер Хуанес', 8155),
    Player(6550871, 'Ромарио Агуэро', 8143),
    Player(6789300, 'Рей Ангел Родригес', 8143),
    Player(6648035, 'Арлей Хинохоса', 8985),
    Player(6553591, 'Арнольдо Альварос', 8160),
    Player(6698751, 'Клэй Кастро', 18588),
    Player(6737170, 'Жаде Куньонес', 8138),
    Player(6737167, 'Вильфредо Корралес', 8138),
    Player(6699481, 'Эрнан Ларринага', 21141),
])

STATISTIC_CORRECTIONS = {
    'cubanas': {
        "Уракан (Ольгин)": {"pluses": -2, "minuses": 13, "total": 11}
    }
}