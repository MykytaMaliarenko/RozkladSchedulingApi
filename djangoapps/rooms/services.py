from djangoapps.classes.models import Class
from djangoapps.rooms.models import Room
from djangoapps.rooms.types import EmptyRooms
from typing import List


class FreeRoomsInBuildingService(object):

    @staticmethod
    def get_all_empty_rooms(all_classes: List[Class], all_rooms: List[Room]) -> List[EmptyRooms]:

        all_empty_rooms_list: List[EmptyRooms] = list()
        for week_number in (1, 2):
            for day_of_week in range(1, 7):
                for time_slot in range(1, 6):
                    all_empty_rooms_list.append(
                        FreeRoomsInBuildingService.get_empty_rooms_at(
                            all_classes, all_rooms,
                            week_number, day_of_week,
                            time_slot
                        )
                    )

        return all_empty_rooms_list

    @staticmethod
    def get_empty_rooms_at(all_classes: List[Class], all_rooms: List[Room], week_number: int,
                           day_of_week: int, time_slot: int) -> EmptyRooms:

        empty_rooms_list: List[Room] = all_rooms.copy()
        for university_class in all_classes:
            if university_class.week_number == week_number \
                    and university_class.day_of_week == day_of_week \
                    and university_class.time_slot_id == time_slot:

                for index, room in enumerate(empty_rooms_list):
                    if room.id == university_class.room_id:
                        empty_rooms_list.pop(index)
                        break

        return EmptyRooms(
            week_number=week_number,
            day_of_week=day_of_week,
            time_slot=time_slot,
            rooms=empty_rooms_list
        )
