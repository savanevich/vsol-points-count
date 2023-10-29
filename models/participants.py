class Participants:
    def __init__(self, participants: list):
        self._participans = participants

    @property
    def participants(self):
        return self._participans

    def get_participant_by_name(self, name: str):
        for participant in self._participans:
            if participant.name == name:
                return participant
        return None

    def get_participant_by_id(self, id: int):
        for participant in self._participans:
            if participant.id == id:
                return participant
        return None
