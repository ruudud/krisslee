from django.utils.unittest import TestCase
from django.test.client import RequestFactory

from krisslee.util.templatetags.url_utils import current

class URLUtilTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_current_url_should_return_active(self):
        request = self.factory.get('/')
        self.failUnlessEqual('active', current(request, '/'))
        self.failUnlessEqual('inactive', current(request, '/jukebox/'))
