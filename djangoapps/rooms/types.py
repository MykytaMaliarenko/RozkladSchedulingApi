from djangoapps.rooms.models import Room
from typing import NamedTuple, List


class EmptyRooms(NamedTuple):
    week_number: int
    day_of_week: int
    time_slot: int
    rooms: List[Room]
