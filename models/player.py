from models.participants import Participants


class Player:
    def __init__(self, id: int, name: str, team_id: int):
        self.id = id
        self.name = name
        self.team_id = team_id

    def team(self, teams_participants: Participants):
        return teams_participants.get_participant_by_id(self.team_id)
