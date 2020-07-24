import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from djangoapps.tests_data_setup import generate_classes

from djangoapps.groups.models import Group
from djangoapps.classes.models import Class
from djangoapps.rooms.models import Room
from djangoapps.teachers.models import Teacher


class ClassesTest(APITestCase):

    @classmethod
    def setUpTestData(cls):
        test_group = Group(
            id=0,
            name='км-92',
        )
        Group.save(test_group)

        test_room = Room(
            id=0,
            name='0',
            university_building=0,
        )
        Room.save(test_room)

        test_teacher = Teacher(
            id=0,
            name='teacher',
            official_name='off teacher',
        )
        Teacher.save(test_teacher)

        classes = generate_classes(1,
                                   groups=[test_group],
                                   rooms=[test_room],
                                   teachers=[test_teacher])
        for test_class in classes:
            Class.save(test_class)

    def test_get_classes_by_group_name(self):
        """
            Testing ClassesByGroupList view by name.
        """
        url = reverse('classes-by-group', kwargs={'group': 'км-92'})
        response = self.client.get(url, format='json')
        self.default_classes_assert(response)

    def test_get_classes_by_group_id(self):
        """
            Testing ClassesByGroupList view by id.
        """
        url = reverse('classes-by-group', kwargs={'group': 0})
        response = self.client.get(url, format='json')
        self.default_classes_assert(response)

    def test_get_classes_by_room_id(self):
        """
            Testing ClassesByRoom view.
        """
        url = reverse('classes-by-room', kwargs={'room': 0})
        response = self.client.get(url, format='json')
        self.default_classes_assert(response)

    def test_get_classes_by_teacher_id(self):
        """
            Testing ClassesByTeacher view.
        """
        url = reverse('classes-by-teacher', kwargs={'teacher': 0})
        response = self.client.get(url, format='json')
        self.default_classes_assert(response)

    def default_classes_assert(self, resp):
        json_response = json.loads(resp.content)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(type(json_response), list)
        self.assertGreater(len(json_response), 0)
