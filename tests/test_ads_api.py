import pytest
from django.urls import reverse
from rest_framework import status
from ads.models import Ad

@pytest.mark.django_db
class TestAdsAPI:

    @pytest.fixture(autouse=True)
    def create_ad(self, user1):
        # создаём объявление до каждого теста
        return Ad.objects.create(
            user=user1,
            title='Test Ad',
            description='Desc',
            category='cat1',
            condition='new'
        )

    def test_create_ad(self, client1):
        url = reverse('ad-list')
        data = {
            'title': 'New Ad',
            'description': 'Some description',
            'category': 'cat2',
            'condition': 'used'
        }
        resp = client1.post(url, data, format='json')
        assert resp.status_code == status.HTTP_201_CREATED
        assert Ad.objects.filter(title='New Ad').exists()

    def test_update_ad_by_owner(self, client1, create_ad):
        url = reverse('ad-detail', args=[create_ad.pk])
        resp = client1.patch(url, {'title': 'Updated'}, format='json')
        assert resp.status_code == status.HTTP_200_OK
        create_ad.refresh_from_db()
        assert create_ad.title == 'Updated'

    def test_update_ad_by_non_owner_forbidden(self, client2, create_ad):
        url = reverse('ad-detail', args=[create_ad.pk])
        resp = client2.patch(url, {'title': 'Hack'}, format='json')
        assert resp.status_code == status.HTTP_403_FORBIDDEN

    def test_delete_ad(self, client1, create_ad):
        url = reverse('ad-detail', args=[create_ad.pk])
        resp = client1.delete(url)
        assert resp.status_code == status.HTTP_204_NO_CONTENT
        assert not Ad.objects.filter(pk=create_ad.pk).exists()

    def test_search_and_filter(self, client1, user1):
        # создаём дополнительные объявления
        Ad.objects.create(user=user1, title='Foo Bar', description='baz', category='cat1', condition='used')
        Ad.objects.create(user=user1, title='Another', description='something', category='cat2', condition='new')

        url = reverse('ad-list')
        r1 = client1.get(f"{url}?search=Foo")
        assert r1.status_code == status.HTTP_200_OK
        assert len(r1.data['results']) == 1

        r2 = client1.get(f"{url}?category=cat1")
        assert all(item['category'] == 'cat1' for item in r2.data['results'])
