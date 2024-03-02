from enum import Enum


class TeamSchool(Enum):
    RAIN = 'rain'
    SUN = 'sun'

class TeamDivision(Enum):
    D1 = 'D1'
    D2 = 'D2'
    D3A = 'D3'
    D3B = 'D3'


class Team:
    def __init__(self, id: int, name: str, school: TeamSchool, division: TeamDivision):
        self.id = id
        self.name = name
        self.school = school
        self.division = division
