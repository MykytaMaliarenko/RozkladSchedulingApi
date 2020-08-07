from typing import List, Union
import random

from djangoapps.groups.models import Group
from djangoapps.classes.models import Class
from djangoapps.rooms.models import Room
from djangoapps.teachers.models import Teacher
from djangoapps.timeslots.models import TimeSlot


group_prefixes = ('км', 'кп', 'кв')


def generate_groups(num: int) -> List[Group]:
    if num <= 0:
        raise ValueError('num should be positive and greater then 0')

    return list(map(
        lambda i: Group(id=i, name=f"{random.choice(group_prefixes)}-{i}"),
        range(num)
    ))


first_names = ('John', 'Andy', 'Joe', 'Oliver', 'Mason')
last_names = ('Johnson', 'Smith', 'Williams', 'Miller', 'Davis')


def generate_teachers(num: int) -> List[Teacher]:
    if num <= 0:
        raise ValueError('num should be positive and greater then 0')

    return list(map(
        lambda i: Teacher(
            id=i,
            name=f"{random.choice(first_names)} {random.choice(last_names)}",
            official_name=f"of. {random.choice(first_names)} {random.choice(last_names)}",
        ),
        range(num)
    ))


def generate_rooms(num: int) -> List[Room]:
    if num <= 0:
        raise ValueError('num should be positive and greater then 0')

    return list(map(
        lambda i: Room(
            id=i,
            name=str(i),
            university_building=random.randint(0, 30),
        ),
        range(num)
    ))


def generate_timeslots() -> List[TimeSlot]:
    return [
        TimeSlot(
            id=1,
            time_start='08:30:00',
            time_end='10:05:00'
        ),
        TimeSlot(
            id=2,
            time_start='10:25:00',
            time_end='12:00:00'
        ),
        TimeSlot(
            id=3,
            time_start='12:20:00',
            time_end='13:55:00'
        ),
        TimeSlot(
            id=4,
            time_start='14:15:00',
            time_end='15:50:00'
        ),
        TimeSlot(
            id=5,
            time_start='16:10:00',
            time_end='17:45:00'
        )
    ]


classes_types = ('Лек', 'Лаб', 'Прак')


def generate_classes(num: int,
                     groups: Union[List[Group], None] = None,
                     rooms: Union[List[Room], None] = None,
                     teachers: Union[List[Teacher], None] = None,
                     time_slots: Union[List[TimeSlot], None] = None) -> List[Class]:
    if num <= 0:
        raise ValueError('num should be positive and greater then 0')

    if not groups:
        groups = generate_groups(num)
        for group in groups:
            Group.save(group)

    if not rooms:
        rooms = generate_rooms(num)
        for room in rooms:
            Room.save(room)

    if not teachers:
        teachers = generate_teachers(num)
        for teacher in teachers:
            Teacher.save(teacher)

    if not time_slots:
        time_slots = generate_timeslots()
        for time_slot in time_slots:
            TimeSlot.save(time_slot)

    res = list()
    for i in range(num):
        uni_class = Class(
            id=i,
            name=f"class {i}",
            type=random.choice(classes_types),

            day_of_week=random.randint(1, 5),
            week_number=random.randint(1, 2),

            room=rooms[i] if len(rooms) > i else random.choice(rooms),
            teacher=teachers[i] if len(teachers) > i else random.choice(teachers),
            time_slot=random.choice(time_slots)
        )

        uni_class.groups.add(groups[i] if len(groups) > i else random.choice(groups))
        res.append(uni_class)

    return res
