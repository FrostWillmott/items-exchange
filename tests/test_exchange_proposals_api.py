import pytest
from django.urls import reverse
from rest_framework import status
from ads.models import Ad, ExchangeProposal

@pytest.mark.django_db
class TestExchangeProposalAPI:

    @pytest.fixture(autouse=True)
    def setup_ads(self, user1, user2):
        self.ad1 = Ad.objects.create(user=user1, title='A1', description='d1', category='c', condition='n')
        self.ad2 = Ad.objects.create(user=user2, title='A2', description='d2', category='c', condition='n')

    def test_create_proposal(self, client1):
        url = reverse('exchangeproposal-list')
        data = {'ad_sender': self.ad1.pk, 'ad_receiver': self.ad2.pk, 'comment': 'Swap?'}
        r = client1.post(url, data, format='json')
        assert r.status_code == status.HTTP_201_CREATED
        ep = ExchangeProposal.objects.get(pk=r.data['id'])
        assert ep.status == 'ожидает'

    def test_update_status_by_receiver(self, client1, client2):
        ep = ExchangeProposal.objects.create(ad_sender=self.ad1, ad_receiver=self.ad2, status='ожидает')
        url = reverse('exchangeproposal-detail', args=[ep.pk])
        r_bad = client1.patch(url, {'status': 'принята'}, format='json')
        assert r_bad.status_code == status.HTTP_403_FORBIDDEN
        r_good = client2.patch(url, {'status': 'принята'}, format='json')
        assert r_good.status_code == status.HTTP_200_OK
        ep.refresh_from_db()
        assert ep.status == 'принята'

    def test_filter_by_status(self, client1):
        ExchangeProposal.objects.create(ad_sender=self.ad1, ad_receiver=self.ad2, status='ожидает')
        ExchangeProposal.objects.create(ad_sender=self.ad1, ad_receiver=self.ad2, status='принята')
        url = reverse('exchangeproposal-list') + '?status=принята'
        r = client1.get(url)
        assert r.status_code == status.HTTP_200_OK
        assert len(r.data['results']) == 1
