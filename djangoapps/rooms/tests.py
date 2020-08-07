import json
from typing import Set

from django.urls import reverse
from rest_framework.test import APITestCase

from djangoapps.tests_data_setup import generate_classes

from djangoapps.rooms.models import Room
from djangoapps.classes.models import Class


class RoomsTest(APITestCase):

    @classmethod
    def setUpTestData(cls):
        rooms = [
            Room(
                id=0,
                name='1',
                university_building=1
            ),
            Room(
                id=1,
                name='2',
                university_building=1
            ),
            Room(
                id=2,
                name='3',
                university_building=2
            ),
            Room(
                id=3,
                name='4',
                university_building=3
            ),
        ]
        for room in rooms:
            Room.save(room)

        classes = generate_classes(1, rooms=rooms)
        for test_class in classes:
            Class.save(test_class)

    def test_buildings(self):
        """
            Testing BuildingsViewSet.
        """
        url = reverse('rooms-buildings')
        response = self.client.get(url, format='json')
        json_response = json.loads(response.content)

        self.assertEqual(set(json_response), {1, 2, 3})

    def test_rooms_in_building(self):
        """
            Testing RoomsInBuildingList.
        """
        url = reverse('rooms-in-building', kwargs={"building": 1})
        response = self.client.get(url, format='json')
        json_response = json.loads(response.content)

        self.assertEqual(set(map(lambda v: v['id'], json_response)), {0, 1})
