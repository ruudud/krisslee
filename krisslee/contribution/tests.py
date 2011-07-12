from django.test import TestCase
from django.core.urlresolvers import reverse

from krisslee.contribution.models import Contribution

class ContributionTests(TestCase):
    def setUp(self):
        self.client.post(reverse('contributions'),
                {'name': 'Dolly Duck', 'amount': 200.0})

    def test_good_contribution(self):
        before = Contribution.objects.count()

        response = self.client.post(reverse('contributions'),
                {'name': 'Donald Duck', 'amount': 200.0})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(before + 1, Contribution.objects.count())

    def test_total_sum_and_number_in_context(self):
        self.client.post(reverse('contributions'),
                {'name': 'Doffen Duck', 'amount': 200.0})

        response = self.client.get(reverse('contributions'))
        self.assertTrue('total' in response.context)
        self.assertEqual(400.0, response.context['total']['amount__sum'])

    def test_that_names_and_amount_are_in_context(self):
        response = self.client.get(reverse('contributions'))
        self.assertTrue('contributions' in response.context)
        contrib_1 = response.context['contributions'][0]

        self.assertEqual('Dolly Duck', contrib_1.name)
        self.assertEqual(200.0, contrib_1.amount)
