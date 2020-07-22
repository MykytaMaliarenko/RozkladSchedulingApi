from django.urls import reverse
from rest_framework import status
from rest_framework.test import APILiveServerTestCase


class ClassesTest(APILiveServerTestCase):
    def test_get_classes_by_group_name(self):
        """
            Testing ClassesByGroupList view.
        """
        url = reverse('classes-by-group', kwargs={'group': 'км-92'})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(type(response.data), type(list))
        self.assertGreater(len(response.data), 0)
