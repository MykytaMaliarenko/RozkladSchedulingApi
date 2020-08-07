import json
from typing import Set

from django.urls import reverse
from rest_framework.test import APITestCase

from djangoapps.tests_data_setup import generate_classes

from djangoapps.groups.models import Group
from djangoapps.classes.models import Class


class GroupsTest(APITestCase):

    def test_search_by_name(self):
        """
            Testing GroupSearchByNameList view.
        """
        groups = [
            Group(
                id=0,
                name='abc'
            ),
            Group(
                id=1,
                name='bbc'
            ),
            Group(
                id=2,
                name='cbc'
            ),
            Group(
                id=3,
                name='abb'
            ),
        ]
        for group in groups:
            Group.save(group)

        classes = generate_classes(1, groups=groups)
        for test_class in classes:
            Class.save(test_class)

        self.assert_search_results('a', {'abc', 'abb'})
        self.assert_search_results('b', {'bbc'})
        self.assert_search_results('c', {'cbc'})

    def assert_search_results(self, request: str, expected_names: Set[str]):
        url = reverse('groups-search', kwargs={'searchRequest': request})
        response = self.client.get(url, format='json')
        json_response = json.loads(response.content)
        self.assertEqual(set(map(lambda v: v['name'], json_response)), expected_names)
