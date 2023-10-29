from enum import Enum


class TeamSchool(Enum):
    RAIN = 'rain'
    SUN = 'sun'


class Team:
    def __init__(self, id: int, name: str, school: TeamSchool):
        self.id = id
        self.name = name
        self.school = school
