#coding: utf-8
from django.core.urlresolvers import reverse
from django.utils.unittest import TestCase
from django.test.client import RequestFactory

from krisslee.util.templatetags.url_utils import current

class URLUtilTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_current_url_should_return_active(self):
        request = self.factory.get('/')
        self.failUnlessEqual(' class="active"', current(request, '/'))
        self.failUnlessEqual('', current(request, '/jukebox/'))

    def test_current_reverse_url_should_return_class_active(self):
        request = self.factory.get(reverse('frontpage'))
        self.failUnlessEqual(' class="active"', current(request, 'frontpage'))

    def test_missing_url_should_fail_with_blank_response(self):
        request = self.factory.get('/')
        self.failUnlessEqual('', current(request, 'frontpagezz'))
