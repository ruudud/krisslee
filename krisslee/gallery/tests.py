#coding: utf-8
from django.core.urlresolvers import reverse
from django.test import TestCase

from krisslee.gallery.models import Picture

class GalleryTests(TestCase):
    fixtures = ['pictures_testdata.json']

    def setUp(self):
        pass

    def test_good_fixtures(self):
        self.assertEqual(Picture.objects.count(), 25)

    def test_pictures_should_be_sent_to_template(self):
        response = self.client.get(reverse('frontpage'))
        self.assertTrue('pictures' in response.context)

    def test_all_pictures_should_be_returned(self):
        response = self.client.get(reverse('frontpage'))

        self.assertEqual(Picture.objects.count(),
                         len(response.context['pictures']))

    def test_picture_URL_should_contain_jpg(self):
        response = self.client.get(reverse('frontpage'))

        self.assertEqual(response.context['pictures'][0].url[-4:], '.jpg')

